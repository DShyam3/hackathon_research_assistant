# LiveKit Voice Research Agent

A voice AI assistant that performs deep research using Valyu's web search API. Simple, direct, and fast.

> Based on [LiveKit Agents Voice AI Quickstart](https://docs.livekit.io/agents/start/voice-ai.md)

## Quick Start

### Prerequisites

- Python 3.9+
- [uv package manager](https://docs.astral.sh/uv/getting-started/installation/)
- Valyu API key
- OpenAI API key
- LiveKit Cloud account

### Installation

1. **Install uv:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Install dependencies:**
   ```bash
   cd livekit-voice-agent
   uv sync
   ```

3. **Download model files:**
   ```bash
   uv run agent.py download-files
   ```

4. **Configure API keys in `.env.local`:**
   ```
   LIVEKIT_API_KEY=your-livekit-api-key
   LIVEKIT_API_SECRET=your-livekit-api-secret
   LIVEKIT_URL=your-livekit-url
   OPENAI_API_KEY=sk-your-openai-api-key
   VALYU_API_KEY=your-valyu-api-key
   ```

### Run

```bash
# Console mode (test locally)
uv run agent.py console

# Development mode (with reload)
uv run agent.py dev

# Production mode
uv run agent.py start
```

## How It Works

**Simple and direct:**

1. User asks a question
2. Agent says "Researching now"
3. Research executes immediately using Valyu web search
4. Agent delivers detailed summary
5. Full results saved to `research_results/` folder

### Example

```
User: "What are the latest AI developments?"

Agent: "Researching now."

[Research executes in background]

Agent: "Research complete. Recent developments include breakthrough 
       advances in quantum computing error correction by MIT researchers, 
       IBM's 1000-qubit processor announcement, and new frameworks for 
       orchestrating multi-agent systems. The full results have been 
       saved and are available."

[Results saved to research_results/research_20251122_152344_What_are_the_latest.md]
```

## Features

✅ **Direct research** - No clarifying questions, just immediate search  
✅ **Web + proprietary sources** - Comprehensive coverage via Valyu  
✅ **Detailed results** - 15 results with ~100k characters each  
✅ **Smart summaries** - 3-4 sentence summaries from top 5 results  
✅ **Saved research** - Full markdown files in `research_results/`  
✅ **Voice-optimized** - Instant acknowledgment, parallel execution  

## Output Files

### Research Results
Saved to `research_results/`:
- **`research_YYYYMMDD_HHMMSS_[query].md`** - Full research with sources

### Transcripts
Saved to `transcripts/`:
- **`transcript_*.txt`** - Real-time conversation log
- **`history_*.json`** - Full conversation history with research sessions

## Configuration

### Valyu Search Parameters

Current settings in `research_handler.py`:
```python
response = valyu.search(
    query,
    search_type="all",           # Web + proprietary sources
    max_num_results=15,          # 15 results for comprehensive coverage
    response_length="large",     # ~100k chars per result
    max_price=30,                # Max cost per search
    relevance_threshold=0.5,     # Minimum relevance score
    is_tool_call=True            # AI-optimized results
)
```

### Summary Generation

Analyzes top 5 results with 300-character previews for detailed 3-4 sentence summaries.

## Project Structure

```
livekit-voice-agent/
├── agent.py                 # Main voice agent
├── research_handler.py      # Research logic & Valyu integration
├── test_valyu_api.py       # Valyu API tests
├── .env.local              # API keys (not in git)
├── pyproject.toml          # Dependencies
├── research_results/       # Research markdown files
└── transcripts/            # Conversation logs
```

## API Costs

- **OpenAI:** ~$0.001-0.01 per conversation (GPT-4o-mini for summaries)
- **Valyu:** Free tier includes 1000+ queries, then ~$0.003 per search

## Testing

Test Valyu API directly:
```bash
uv run python test_valyu_api.py
```

## Troubleshooting

**"VALYU_API_KEY not found"**
- Add key to `.env.local`
- Get free key at https://platform.valyu.ai/user/account/apikeys

**"OPENAI_API_KEY not found"**
- Add key to `.env.local`
- Get key at https://platform.openai.com/api-keys

**"No results found"**
- Check Valyu API status at https://status.valyu.ai
- Verify API key is valid

## Learn More

- [LiveKit Voice AI Quickstart](https://docs.livekit.io/agents/start/voice-ai.md)
- [Valyu Documentation](https://docs.valyu.ai/)
- [LiveKit Agents Playground](https://docs.livekit.io/agents/start/playground.md)

## Deployment

Deploy to LiveKit Cloud:
```bash
brew install livekit-cli
lk cloud auth
lk agent create
```

See [Deploying to LiveKit Cloud](https://docs.livekit.io/agents/ops/deployment.md) for details.
