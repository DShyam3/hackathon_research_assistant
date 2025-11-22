from dotenv import load_dotenv
import json
import asyncio
from datetime import datetime
from pathlib import Path

from livekit import agents, rtc
from livekit.agents import AgentServer, AgentSession, Agent, room_io, UserInputTranscribedEvent, ConversationItemAddedEvent

from livekit.plugins import (
    noise_cancellation,
)

from research_handler import ResearchSession, ResearchState
import os

load_dotenv(".env.local")

# Verify required API keys
if not os.getenv("VALYU_API_KEY"):
    print("⚠️  WARNING: VALYU_API_KEY not found in environment!")
if not os.getenv("OPENAI_API_KEY"):
    print("⚠️  WARNING: OPENAI_API_KEY not found in environment!")

# Create transcripts directory if it doesn't exist
TRANSCRIPTS_DIR = Path("transcripts")
TRANSCRIPTS_DIR.mkdir(exist_ok=True)

class Assistant(Agent):
    def __init__(self, research_session: ResearchSession = None, in_research_mode: bool = False) -> None:
        instructions = """You are a research assistant. When the user asks a question, acknowledge briefly that research is being conducted. Do not ask clarifying questions. The research will be executed automatically in the background using Valyu search."""
        super().__init__(instructions=instructions)
        self.research_session = research_session
        self.in_research_mode = in_research_mode

server = AgentServer()

@server.rtc_session()
async def my_agent(ctx: agents.JobContext):
    # Using LiveKit Inference - no OpenAI API key needed!
    # Only requires LiveKit credentials (LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET)
    session = AgentSession(
        stt="assemblyai/universal-streaming:en",  # Speech-to-text
        llm="openai/gpt-4.1-mini",                # Language model
        tts="cartesia/sonic-3",                   # Text-to-speech
    )

    # Initialize research session
    research_session = ResearchSession(session_id=ctx.room.name)

    # Set up transcript logging
    transcript_file = TRANSCRIPTS_DIR / f"transcript_{ctx.room.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    json_file = TRANSCRIPTS_DIR / f"history_{ctx.room.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    conversation_history = []
    research_entries = []
    pending_tasks = []  # Track async tasks to ensure they complete
    research_task = None  # Track background research task

    async def handle_research_flow(user_query: str) -> bool:
        """
        Execute research immediately - speak and research in parallel
        """
        await research_session.initiate_research(user_query)
        
        # Start research task FIRST (don't await)
        nonlocal research_task
        research_task = asyncio.create_task(_execute_research_in_background())
        pending_tasks.append(research_task)
        
        # Then acknowledge - this happens in parallel with research
        await session.say(
            "Researching now.",
            allow_interruptions=True
        )
        
        return True

    async def _execute_research_in_background():
        """Execute research in the background and handle results"""
        nonlocal research_task
        try:
            print(f"DEBUG: Starting background research execution")
            summary = await research_session.execute_research()

            # Save research to markdown
            markdown_path = research_session.save_research_as_markdown()
            if markdown_path:
                print(f"DEBUG: Research saved to {markdown_path}")

            research_entries.append(research_session.get_transcript_entry())

            # Notify that research is complete and available
            completion_message = f"Research complete. {summary} The full results have been saved and are available."
            await session.say(completion_message, allow_interruptions=True)

            research_session.reset()
            research_task = None
        except Exception as e:
            print(f"Research error: {e}")
            import traceback
            traceback.print_exc()
            await session.say("Error during research.", allow_interruptions=True)
            research_session.reset()
            research_task = None

    async def _handle_user_input(event: UserInputTranscribedEvent):
        """Handle user input - execute research immediately"""
        if research_session.state == ResearchState.IDLE:
            print(f"DEBUG: Initiating research for: {event.transcript}")
            await handle_research_flow(event.transcript)

    @session.on("user_input_transcribed")
    def on_user_input_transcribed(event: UserInputTranscribedEvent):
        """Log user transcripts in real-time and handle research flow."""
        # Only log and print final transcripts (when user has stopped talking)
        if not event.is_final:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] USER: {event.transcript} (language: {event.language}, final: {event.is_final})"
        conversation_history.append(entry)

        # Append to file immediately
        with open(transcript_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

        print(f"📝 {entry}")

        # Create task and track it to ensure completion
        task = asyncio.create_task(_handle_user_input(event))
        pending_tasks.append(task)

    @session.on("conversation_item_added")
    def on_conversation_item_added(event: ConversationItemAddedEvent):
        """Log agent responses when added to conversation."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        role = event.item.role.upper()
        text = event.item.text_content or "[audio response]"
        entry = f"[{timestamp}] {role}: {text}"
        conversation_history.append(entry)

        # Append to file immediately
        with open(transcript_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")

        print(f"💬 {entry}")

    async def save_full_history():
        """Save complete conversation history as JSON when session ends."""
        # Wait for any pending research tasks to complete
        if pending_tasks:
            print(f"DEBUG: Waiting for {len(pending_tasks)} pending tasks...")
            await asyncio.gather(*pending_tasks, return_exceptions=True)
            print(f"DEBUG: All pending tasks completed")

        try:
            history_dict = session.history.to_dict()

            # Add research sessions to the history
            if research_entries:
                history_dict["research_sessions"] = research_entries

            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(history_dict, f, indent=2, ensure_ascii=False)

            print(f"\n✅ Full conversation history saved to {json_file}")
        except Exception as e:
            print(f"\n⚠️  Error saving full history: {e}")

    # Save full history when session ends (this will run on Ctrl+C too!)
    ctx.add_shutdown_callback(save_full_history)

    await session.start(
        room=ctx.room,
        agent=Assistant(research_session=research_session),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=lambda params: noise_cancellation.BVCTelephony() if params.participant.kind == rtc.ParticipantKind.PARTICIPANT_KIND_SIP else noise_cancellation.BVC(),
            ),
        ),
    )

    # Don't generate initial greeting - wait for user input to trigger research
    # await session.generate_reply(
    #     instructions="Greet the user and offer your assistance. You should start by speaking in English."
    # )


if __name__ == "__main__":
    agents.cli.run_app(server)
