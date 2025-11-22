from dotenv import load_dotenv
import json
from datetime import datetime
from pathlib import Path

from livekit import agents, rtc
from livekit.agents import AgentServer, AgentSession, Agent, room_io, UserInputTranscribedEvent, ConversationItemAddedEvent

from livekit.plugins import (
    noise_cancellation,
)

load_dotenv(".env.local")

# Create transcripts directory if it doesn't exist
TRANSCRIPTS_DIR = Path("transcripts")
TRANSCRIPTS_DIR.mkdir(exist_ok=True)

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")

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

    # Set up transcript logging
    transcript_file = TRANSCRIPTS_DIR / f"transcript_{ctx.room.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    conversation_history = []

    @session.on("user_input_transcribed")
    def on_user_input_transcribed(event: UserInputTranscribedEvent):
        """Log user transcripts in real-time."""
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

    @session.on("conversation_item_added")
    def on_conversation_item_added(event: ConversationItemAddedEvent):
        """Log agent responses when added to conversation."""
        # Skip user messages - they're already logged in on_user_input_transcribed
        if event.item.role.lower() == "user":
            return
        
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
            json_file = TRANSCRIPTS_DIR / f"history_{ctx.room.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            history_dict = session.history.to_dict()
            
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(history_dict, f, indent=2, ensure_ascii=False)
            
            print(f"\n✅ Full conversation history saved to {json_file}")
        except Exception as e:
            print(f"\n⚠️  Error saving full history: {e}")

    # Save full history when session ends (this will run on Ctrl+C too!)
    ctx.add_shutdown_callback(save_full_history)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
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
