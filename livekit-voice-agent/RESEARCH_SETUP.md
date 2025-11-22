# Voice Research Agent Setup Guide

## Overview

This guide walks you through setting up the voice research agent with Valyu DeepSearch integration and OpenAI clarifying questions.

## Architecture

The system works in the following way:

```
User Query (Voice)
    ↓
Agent detects new query
    ↓
Generates 3 clarifying questions using OpenAI
    ↓
User answers each question sequentially (Voice)
    ↓
Executes Valyu DeepSearch with enhanced query
    ↓
Agent provides concise summary (Voice)
    ↓
Full results saved to transcript JSON
```

## Setup Steps

### 1. Update Environment Variables

Edit `.env.local` and add your OpenAI API key:

```bash
OPENAI_API_KEY="sk-your-actual-key-here"
```

The `VALYU_API_KEY` should already be in your `.env.local` file.

**Note:** Never commit `.env.local` to git with real API keys.

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
# or
poetry install
```

The new dependencies added are:
- `openai>=1.0.0` - For generating clarifying questions
- `valyu` - For deep search (already configured via langchain-valyu)

### 3. Verify API Keys

Ensure your `.env.local` has:
- `LIVEKIT_API_KEY` ✓ (already set)
- `LIVEKIT_API_SECRET` ✓ (already set)
- `LIVEKIT_URL` ✓ (already set)
- `VALYU_API_KEY` ✓ (needs your actual Valyu API key)
- `OPENAI_API_KEY` ✓ (add your OpenAI API key)

## Running the Agent

```bash
python agent.py
```

The agent will:
1. Start listening for voice input
2. Greet the user
3. When user says something, automatically trigger research mode
4. Ask clarifying questions sequentially
5. Perform deep search with Valyu
6. Deliver results via voice
7. Save full transcript with research details to `transcripts/` folder

## File Structure

### New Files Created

**`research_handler.py`** - Core research functionality
- `ResearchSession` class - Manages individual research sessions
- `ResearchState` enum - Tracks conversation state (IDLE, ASKING_QUESTION_1, etc.)
- Methods:
  - `initiate_research()` - Start research and ask first question
  - `record_answer()` - Record user answers and move to next state
  - `execute_research()` - Run Valyu search with enhanced query
  - `get_transcript_entry()` - Format research session for JSON transcript

### Modified Files

**`agent.py`**
- Updated imports to include `ResearchSession` and `ResearchState`
- Modified `Assistant` class to include research session reference
- Enhanced transcript logging to include research entries
- Updated shutdown callback to save research data with conversation history

**`.env.local`**
- Added placeholder for `OPENAI_API_KEY`

**`pyproject.toml`**
- Replaced `langchain-anthropic` with `openai>=1.0.0`

## How It Works

### Conversation Flow

1. **User speaks:** "Tell me about quantum computing"
2. **Agent responds:** "I'll research that for you. Let me ask a few clarifying questions. Question 1 of 3: Are you interested in the theoretical foundations or practical applications?"
3. **User responds:** "Theoretical foundations"
4. **Agent asks:** "Question 2 of 3: Are you looking for recent developments or foundational concepts?"
5. **User responds:** "Recent developments"
6. **Agent asks:** "Question 3 of 3: What is your technical background level - beginner, intermediate, or advanced?"
7. **User responds:** "Intermediate"
8. **Agent researches** with query: "Tell me about quantum computing theoretical foundations recent developments intermediate level"
9. **Agent summarizes:** "Here's what I found: Recent theoretical advances in quantum computing focus on three key areas: quantum error correction improvements, new qubit designs, and novel algorithm development. The full research details have been saved to your transcript file."

### State Management

The `ResearchSession` tracks the conversation state:

```
IDLE → GENERATING_QUESTIONS → ASKING_QUESTION_1
    → ASKING_QUESTION_2 → ASKING_QUESTION_3
    → RESEARCHING → DELIVERING_RESULTS → IDLE
```

### Transcript Format

Transcripts are saved in two formats:

**Text file** (`transcript_*.txt`):
```
[2025-11-22 10:30:00] USER: Tell me about quantum computing (language: en, final: True)
[2025-11-22 10:30:05] ASSISTANT: I'll research that for you...
[2025-11-22 10:30:10] USER: Theoretical foundations (language: en, final: True)
...
```

**JSON file** (`history_*.json`):
```json
{
  "research_sessions": [
    {
      "timestamp": "2025-11-22T10:30:00",
      "type": "research_session",
      "session_id": "room-name",
      "original_query": "Tell me about quantum computing",
      "clarifying_questions": [
        "Are you interested in theoretical foundations or practical applications?",
        "Are you looking for recent developments or foundational concepts?",
        "What is your technical background level?"
      ],
      "user_answers": [
        "Theoretical foundations",
        "Recent developments",
        "Intermediate"
      ],
      "research_summary": "Here's what I found: ...",
      "detailed_results": [
        {
          "title": "...",
          "url": "...",
          "source": "valyu/valyu-arxiv",
          "content_preview": "...",
          "relevance_score": 0.85,
          "authors": [...],
          "publication_date": "2025-01-01",
          "doi": "...",
          "citation_count": 42
        },
        ...
      ]
    }
  ],
  "history": [...]
}
```

## API Keys

### OpenAI API Key
Get your key from: https://platform.openai.com/api-keys
- Used for generating clarifying questions using GPT-4o-mini
- Approximately 10-50 tokens per question generation

### Valyu API Key
Get your key from: https://platform.valyu.ai/user/account/apikeys
- Used for deep search across academic papers, web content, and structured data
- Free tier includes 1000+ query retrievals

## Customization

### Adjust Search Sources

In `research_handler.py`, modify the `execute_research()` method's `included_sources`:

```python
included_sources=["valyu/valyu-arxiv", "valyu/valyu-pubmed"],  # Current: Academic focus
```

Other available sources:
- `valyu/valyu-arxiv` - arXiv papers
- `valyu/valyu-pubmed` - PubMed medical literature
- `valyu/valyu-stocks-US` - Financial data
- `valyu/valyu-web` - General web search

### Adjust Question Generation

Modify the prompt in `_generate_questions()` to change how questions are generated:

```python
prompt = f"""Generate exactly 3 concise clarifying questions for the following research topic.
Make each question brief and conversational (suitable for voice conversation), not academic.
Return ONLY the questions, one per line, without numbering or extra text.

Topic: {query}"""
```

### Adjust Summary Generation

Modify the prompt in `_generate_summary()` to change how results are summarized:

```python
prompt = f"""Create a brief, conversational 2-3 point summary (suitable for voice delivery)
from these research results. Focus on the most important insights. Do NOT mention sources or URLs.

Results:
{results_text}"""
```

## Troubleshooting

### "OPENAI_API_KEY not found"
Make sure you've added your OpenAI API key to `.env.local` and it's loaded correctly.

### "VALYU_API_KEY not found"
Ensure your Valyu API key is in `.env.local`.

### Questions aren't being generated
Check that OpenAI API key has sufficient credits and is valid.

### Search results are empty
Try simplifying the query or adjusting the `max_price` parameter in `execute_research()`.

### Transcript files not being created
Ensure the `transcripts/` directory exists (it's created automatically if missing).

## Advanced Usage

### Manual Research Testing

You can test the research handler directly:

```python
import asyncio
from research_handler import ResearchSession

async def test():
    session = ResearchSession("test-session")

    # Start research
    q1_prompt = await session.initiate_research("What is quantum computing?")
    print(q1_prompt)

    # Answer question 1
    q2_prompt = session.record_answer("Theoretical foundations")
    print(q2_prompt)

    # Answer question 2
    q3_prompt = session.record_answer("Recent developments")
    print(q3_prompt)

    # Answer question 3
    session.record_answer("Intermediate")

    # Execute research
    summary = await session.execute_research()
    print(summary)

    # Get full transcript entry
    transcript = session.get_transcript_entry()
    print(json.dumps(transcript, indent=2))

asyncio.run(test())
```

### Async Considerations

Both `initiate_research()` and `execute_research()` are async functions. They must be awaited in the LiveKit agent context.

## Performance Notes

- **Question Generation:** ~1-2 seconds (GPT-4o-mini is fast)
- **Valyu Search:** ~3-5 seconds (depends on query complexity and sources)
- **Summary Generation:** ~1-2 seconds
- **Total Research Time:** ~5-10 seconds

The agent will indicate it's researching, so the user experience won't feel blocked.

## Next Steps

1. Add your OPENAI_API_KEY to `.env.local`
2. Run `python agent.py` to start the agent
3. Test the flow with a simple query
4. Check the `transcripts/` folder for generated files
5. Customize prompts as needed for your use case

## Support

For issues with:
- **LiveKit Agent:** Check https://docs.livekit.io/agents/
- **Valyu API:** Check https://docs.valyu.ai/
- **OpenAI API:** Check https://platform.openai.com/docs/

## Architecture Diagram

```
┌─────────────────────────────────────────────────┐
│         LiveKit Voice Agent (agent.py)          │
└────────────────┬────────────────────────────────┘
                 │
                 ├─→ STT: AssemblyAI Universal Streaming
                 ├─→ LLM: OpenAI GPT-4.1-mini
                 └─→ TTS: Cartesia Sonic-3
                 │
    ┌────────────┴───────────────┐
    │                            │
    ▼                            ▼
┌─────────────────────┐  ┌──────────────────────┐
│  Research Handler   │  │ Transcript Logging   │
│ (research_handler.  │  │ • Text files         │
│      py)            │  │ • JSON history       │
│                     │  │ • Research sessions  │
│ • Question Gen      │  └──────────────────────┘
│   (OpenAI)          │
│                     │
│ • Search Exec       │
│   (Valyu)           │
│                     │
│ • Summary Gen       │
│   (OpenAI)          │
│                     │
│ • State Mgmt        │
└─────────────────────┘
        │
        ├─→ OpenAI API (GPT-4o-mini)
        └─→ Valyu DeepSearch API
```
