# LiveKit Voice Research Agent

A voice AI assistant that answers research questions by asking clarifying questions first, then performing deep searches using Valyu's DeepSearch API.

> Based on [LiveKit Agents Voice AI Quickstart](https://docs.livekit.io/agents/start/voice-ai.md)

## Quick Start

### Prerequisites

- Python 3.9+
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)
- Active Valyu API key
- Active OpenAI API key
- LiveKit Cloud account with API keys

### Installation

1. **Install uv** (if not already installed):
   ```bash
   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Windows
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Navigate to the project:**
   ```bash
   cd livekit-voice-agent
   ```

3. **Install dependencies with uv:**
   ```bash
   uv sync
   ```

4. **Download model files:**
   ```bash
   uv run agent.py download-files
   ```

5. **Configure API keys:**

   Edit `.env.local` and ensure you have:
   ```
   LIVEKIT_API_KEY=your-livekit-api-key
   LIVEKIT_API_SECRET=your-livekit-api-secret
   LIVEKIT_URL=your-livekit-url
   OPENAI_API_KEY=sk-your-openai-api-key
   VALYU_API_KEY=your-valyu-api-key
   ```

   Get LiveKit credentials from [LiveKit Cloud](https://cloud.livekit.io/).

### Run the Agent

**Development mode** (with instant reload):
```bash
uv run agent.py dev
```

**Console mode** (test locally in terminal):
```bash
uv run agent.py console
```

**Production mode**:
```bash
uv run agent.py start
```

The agent will connect to LiveKit Cloud and be available in the [Agents Playground](https://docs.livekit.io/agents/start/playground.md).

## How It Works

The agent uses smart detection to determine when research is needed:

1. **User asks a question**
2. **Agent checks**: Does this need research? (smart detection via LLM)
3. **If no research needed**: Agent answers directly from knowledge
4. **If research needed**:
   - Agent says: "Researching..." (minimal status update)
   - Agent asks 3 clarifying questions (short & simple, via voice)
   - User answers each question conversationally
   - Agent says: "Searching..." (minimal status update)
   - Agent performs deep research using Valyu DeepSearch
   - Agent delivers concise summary via voice
   - Full results saved to transcript files

### Example: Research Query

```
User: "What's the latest on quantum computing advances?"

Agent: "Researching..."

Agent: "Theoretical or practical?"

User: "Theoretical"

Agent: "Recent or foundational?"

User: "Recent"

Agent: "Implementation or theory?"

User: "Theory"

Agent: "Searching..."

Agent: "Here's what I found: Recent theoretical advances focus on three key areas:
        quantum error correction improvements, advanced qubit designs, and new algorithm development."

[Full research details saved to transcripts/history_*.json]
```

### Example: Direct Answer Query

```
User: "What's 2+2?"

Agent: "That's 4."

[No research needed - agent answers directly]
```

## Output Files

Transcripts are automatically saved to the `transcripts/` folder:

- **`transcript_*.txt`** - Real-time conversation log
- **`history_*.json`** - Full conversation history with research details

### Sample JSON Structure

```json
{
  "research_sessions": [
    {
      "timestamp": "2025-11-22T10:30:00",
      "original_query": "Tell me about quantum computing",
      "clarifying_questions": [
        "Question 1...",
        "Question 2...",
        "Question 3..."
      ],
      "user_answers": [
        "Answer 1...",
        "Answer 2...",
        "Answer 3..."
      ],
      "research_summary": "Here's what I found: ...",
      "detailed_results": [
        {
          "title": "Paper title",
          "url": "https://arxiv.org/...",
          "source": "valyu/valyu-arxiv",
          "relevance_score": 0.85,
          "authors": ["Author 1", "Author 2"],
          "publication_date": "2025-01-01"
        }
      ]
    }
  ]
}
```

## Configuration

### Environment Variables (.env.local)

```
LIVEKIT_API_KEY=your-livekit-api-key
LIVEKIT_API_SECRET=your-livekit-api-secret
LIVEKIT_URL=wss://your-livekit-url
OPENAI_API_KEY=sk-your-openai-api-key
VALYU_API_KEY=your-valyu-api-key
```

**Do not commit `.env.local` to git** - use `.env.local.example` to document required keys.

## Project Structure

```
livekit-voice-agent/
├── agent.py                 # Main LiveKit voice agent
├── research_handler.py      # Research logic and Valyu integration
├── .env.local              # API keys (not in git)
├── pyproject.toml          # Python dependencies (managed by uv)
├── uv.lock                 # Dependency lockfile (managed by uv)
├── README.md               # This file
├── RESEARCH_SETUP.md       # Detailed setup guide
└── transcripts/            # Generated conversation transcripts
    ├── transcript_*.txt
    └── history_*.json
```

## Key Files

- **`agent.py`** - LiveKit voice agent that manages conversations
- **`research_handler.py`** - Research orchestration, question generation, and Valyu integration
- **`RESEARCH_SETUP.md`** - Comprehensive documentation with customization options

## Features

✅ **Voice-First Design** - All interaction via speech
✅ **Smart Detection** - Agent decides when research is actually needed (not every question)
✅ **Short & Simple Questions** - Max 10 words per clarifying question for voice clarity
✅ **Minimal Status Updates** - Brief updates ("Researching...", "Searching...") not verbose
✅ **Deep Research** - Access to 1000+ academic papers and web content via Valyu
✅ **Structured Results** - Results saved in JSON with full metadata
✅ **No Blocking** - Async operations for responsive voice UX
✅ **Conversation Awareness** - Agent speaks clarifying questions and status directly to user

## Troubleshooting

**"OPENAI_API_KEY not found"**
- Ensure `.env.local` has your OpenAI API key
- Verify the file is in the project root directory
- Check that `load_dotenv(".env.local")` runs before API calls

**"VALYU_API_KEY not found"**
- Confirm your Valyu API key is in `.env.local`
- Get a free key at https://platform.valyu.ai/user/account/apikeys

**"Model download failed"**
- Run `uv run agent.py download-files` to download model files
- Ensure you have sufficient disk space (~500MB)

**"No results found"**
- Try simplifying your query
- Check Valyu API status at https://status.valyu.ai

**"Connection refused" when running agent**
- Verify LiveKit credentials in `.env.local`
- Ensure you have a valid LiveKit Cloud account
- Check your internet connection

**Transcript files not appearing**
- The `transcripts/` directory is created automatically
- Check file permissions if manually created

## API Costs

- **OpenAI:** ~$0.001-0.01 per conversation (GPT-4o-mini)
- **Valyu:** Free tier includes 1000+ queries, then $0.0005-0.003 per search

## Learn More

- **Detailed Setup Guide:** See `RESEARCH_SETUP.md` for customization options
- **LiveKit Voice AI Quickstart:** https://docs.livekit.io/agents/start/voice-ai.md
- **LiveKit Agents Documentation:** https://docs.livekit.io/agents/
- **LiveKit Agents Playground:** https://docs.livekit.io/agents/start/playground.md
- **Valyu Documentation:** https://docs.valyu.ai/
- **OpenAI API Documentation:** https://platform.openai.com/docs/

## Next Steps

1. Install uv and dependencies: `uv sync`
2. Download model files: `uv run agent.py download-files`
3. Add your OpenAI and Valyu API keys to `.env.local`
4. Start in dev mode: `uv run agent.py dev`
5. Connect via [Agents Playground](https://docs.livekit.io/agents/start/playground.md)
6. Test with a voice query and check `transcripts/` folder for results
7. See `RESEARCH_SETUP.md` for advanced customization

## Deployment

To deploy this agent to LiveKit Cloud:

```bash
# Ensure you have the LiveKit CLI installed
brew install livekit-cli

# Link your LiveKit Cloud project
lk cloud auth

# Create and deploy the agent
lk agent create
```

See [Deploying to LiveKit Cloud](https://docs.livekit.io/agents/ops/deployment.md) for more details.
