# Quick Setup (2 minutes)

## 1. Install uv (if needed)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 2. Install dependencies

```bash
uv sync
uv run agent.py download-files
```

## 3. Configure `.env.local`

Copy from `.env.local.example` and add your API keys:
```bash
cp .env.local.example .env.local
# Edit .env.local and add:
# - OPENAI_API_KEY=sk-...
# - VALYU_API_KEY=...
```

Already configured:
- ✅ LIVEKIT_API_KEY
- ✅ LIVEKIT_API_SECRET
- ✅ LIVEKIT_URL

## 4. Run the agent

```bash
# Development mode (with hot reload)
uv run agent.py dev

# Or test locally in terminal
uv run agent.py console
```

## 5. Test it

1. Go to [Agents Playground](https://playground.livekit.io/)
2. Select your agent from the dropdown
3. Click "Join" and start talking
4. Results saved to `transcripts/` folder

## Key Commands

```bash
uv sync                          # Install/update dependencies
uv run agent.py download-files   # Download model files
uv run agent.py dev              # Run in development
uv run agent.py console          # Run locally in terminal
uv run agent.py start            # Production mode
```

## Need Help?

- **README.md** - Full setup and features
- **RESEARCH_SETUP.md** - Advanced customization
- **docs.livekit.io** - Official LiveKit docs

## What It Does

User: "Tell me about quantum computing"
↓
Agent: "I'll help. Question 1: Theoretical or practical?"
User: "Theoretical"
↓
Agent: "Question 2: Recent or foundational?"
User: "Recent"
↓
Agent: "Question 3: Beginner, intermediate, or advanced?"
User: "Intermediate"
↓
Agent: Researches + delivers summary + saves full results
