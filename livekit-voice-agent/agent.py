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

load_dotenv(".env.local")

# Create transcripts directory if it doesn't exist
TRANSCRIPTS_DIR = Path("transcripts")
TRANSCRIPTS_DIR.mkdir(exist_ok=True)

class Assistant(Agent):
    def __init__(self, research_session: ResearchSession = None) -> None:
        instructions = """You are a research-focused voice AI assistant.

When users ask questions:
1. Answer simple questions directly from your knowledge
2. For questions needing current data or research, the agent will trigger research mode
3. During research, you'll ask clarifying questions to understand better
4. Provide concise, conversational responses suitable for voice

Be helpful, clear, and brief in your spoken responses."""
        super().__init__(instructions=instructions)
        self.research_session = research_session

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

    async def handle_research_flow(user_query: str) -> bool:
        """
        Manage the full research conversation flow with voice.
        Returns True if research was triggered, False if it should use normal LLM.

        CONVERSATION FLOW:
        1. User: "What's the latest on quantum computing?"
        2. Agent checks: Does this need research? (Yes)
        3. Agent says: "Researching..."
        4. Agent asks: "Question 1 of 3: Theoretical or practical?"
        5. User: "Theoretical"
        6. Agent asks: "Question 2 of 3: Recent or foundational?"
        7. User: "Recent"
        8. Agent asks: "Question 3 of 3: Your background level?"
        9. User: "Intermediate"
        10. Agent says: "Searching..."
        11. Agent: "Here's what I found: [summary]"
        12. System: Saves full results to transcript
        """
        # Check if research is needed
        needs_research = await research_session.should_research(user_query)
        if not needs_research:
            return False

        # Say we're researching
        await session.say("Researching...", allow_interruptions=True)

        # Start research and get first question
        first_question = await research_session.initiate_research(user_query)
        await session.say(first_question, allow_interruptions=True)

        return True

    async def _handle_user_input(event: UserInputTranscribedEvent):
        """Async handler for user input - handles research flow."""
        # Handle research flow based on current state
        if research_session.state == ResearchState.IDLE:
            # New query - check if research is needed
            await handle_research_flow(event.transcript)

        elif research_session.state in [
            ResearchState.ASKING_QUESTION_1,
            ResearchState.ASKING_QUESTION_2,
            ResearchState.ASKING_QUESTION_3
        ]:
            # Record answer and get next question or trigger search
            next_prompt = research_session.record_answer(event.transcript)

            if next_prompt:
                # Ask next question
                await session.say(next_prompt, allow_interruptions=True)
            else:
                # All questions answered - start research
                await session.say("Searching...", allow_interruptions=True)

                try:
                    summary = await research_session.execute_research()

                    # Save research to transcript
                    research_entries.append(research_session.get_transcript_entry())

                    # Speak summary
                    await session.say(summary, allow_interruptions=True)

                    # Reset for next query
                    research_session.reset()
                except Exception as e:
                    error_msg = f"Sorry, I had trouble researching that. {str(e)}"
                    await session.say(error_msg, allow_interruptions=True)
                    research_session.reset()

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

        # Use asyncio.create_task to run async research flow in background
        asyncio.create_task(_handle_user_input(event))

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

    await session.generate_reply(
        instructions="Greet the user and offer your assistance. You should start by speaking in English."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)
