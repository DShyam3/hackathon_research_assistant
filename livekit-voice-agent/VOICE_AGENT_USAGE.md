# Voice-Enabled Research Agent - Usage Guide

## Quick Start

### 1. Install & Setup
```bash
uv sync
uv run agent.py download-files
# Add your API keys to .env.local
```

### 2. Run the Agent
```bash
uv run agent.py dev
```

### 3. Test in Playground
Go to [Agents Playground](https://playground.livekit.io/) and select your agent.

## How to Interact

### Simple Question (No Research)
```
You: "What's 2 plus 2?"
Agent: "That's 4."
```
- Agent detects this doesn't need research
- Answers directly from knowledge
- Conversation continues normally

### Research Question (With Voice)
```
You: "What's the latest on quantum computing?"

Agent: "Researching..."
[Minimal status while preparing questions]

Agent: "Theoretical or practical?"
You: "Theoretical"

Agent: "Recent or foundational?"
You: "Recent"

Agent: "Implementation or theory?"
You: "Theory"

Agent: "Searching..."
[Minimal status while researching]

Agent: "Here's what I found: Recent theoretical advances focus on three key areas:
        quantum error correction improvements, advanced qubit designs, and new algorithm development."

[Full research details saved to transcripts/history_*.json]
```

## Voice Features

### ✅ Spoken Questions
Clarifying questions are spoken aloud by the agent using Cartesia TTS.
- Max 10 words per question for clarity
- Simple, conversational language
- One question at a time (easy to follow)

### ✅ Status Updates
Brief, non-intrusive updates while the agent works:
- "Researching..." - Preparing clarifying questions
- "Searching..." - Executing Valyu search

### ✅ Spoken Results
Research summaries delivered as 2-3 bullet points, suitable for voice:
- Key findings only (no sources or URLs)
- Conversational tone
- About 30-60 seconds total

### ✅ Interruptions
You can interrupt at any time:
- Break in while agent is speaking
- Clarify your question
- Ask for more details

## Smart Detection Logic

The agent uses OpenAI to decide if research is needed:

**Triggers Research:**
- "What are recent developments in AI?"
- "How do neural networks work?"
- "Tell me about quantum computing"
- "Latest stock prices for Apple"
- "What happened in tech news this week?"

**Answers Directly (No Research):**
- "What's 2+2?" → "4"
- "Who is the president of France?" → "Emmanuel Macron"
- "What is photosynthesis?" → [Direct explanation]
- "How do you cook pasta?" → [Direct recipe]

## Question Examples

### Short & Simple (What You'll Hear)

❌ "Could you please elaborate on whether you're interested in the theoretical underpinnings or practical applications of this technology?"

✅ "Theoretical or practical?"

❌ "Are you seeking recent developments, or would you prefer foundational information?"

✅ "Recent or foundational?"

❌ "What would you describe as your level of technical expertise - beginner, intermediate, or advanced?"

✅ "Implementation or theory?"

## Answering Questions

Just speak naturally - the agent understands conversational answers:

```
Agent: "Theoretical or practical?"
You: "Theoretical"        ✅ Works
You: "Theoretical focus"  ✅ Works
You: "Theroetical please" ✅ Works (handles typos)
You: "I'm interested in the theoretical side" ✅ Works
```

## After Research

Once research is complete:

1. **Listen to Summary** - Agent speaks 2-3 key findings
2. **Files Saved** - Full results automatically saved to:
   - `transcripts/transcript_*.txt` - Conversation log
   - `transcripts/history_*.json` - Full research details with metadata

3. **Ask Follow-ups** - You can then ask:
   - "Tell me more about that"
   - "Any other details?"
   - "Who are the authors?"
   - Start new research with a different topic

## Transcript Files

### Text Transcript (transcript_*.txt)
```
[2025-11-22 10:30:00] USER: What's the latest on quantum computing advances?
[2025-11-22 10:30:02] ASSISTANT: Researching...
[2025-11-22 10:30:03] ASSISTANT: Theoretical or practical?
[2025-11-22 10:30:05] USER: Theoretical
[2025-11-22 10:30:07] ASSISTANT: Recent or foundational?
...
```

### JSON Transcript (history_*.json)
```json
{
  "research_sessions": [
    {
      "timestamp": "2025-11-22T10:30:00",
      "original_query": "What's the latest on quantum computing advances?",
      "clarifying_questions": [
        "Theoretical or practical?",
        "Recent or foundational?",
        "Implementation or theory?"
      ],
      "user_answers": [
        "Theoretical",
        "Recent",
        "Theory"
      ],
      "research_summary": "Here's what I found: ...",
      "detailed_results": [
        {
          "title": "Paper title",
          "url": "https://arxiv.org/...",
          "source": "valyu/valyu-arxiv",
          "relevance_score": 0.85,
          "authors": ["Author 1", "Author 2"],
          "publication_date": "2025-01-01",
          "doi": "https://doi.org/...",
          "citation_count": 42
        }
      ]
    }
  ],
  "history": [...]
}
```

## Troubleshooting

### "Agent doesn't speak the question"
- Check internet connection
- Verify OpenAI API key is valid
- Check Cartesia TTS is working (system audio)

### "Questions are unclear or too long"
- Questions should be max 10 words
- If not, check OpenAI API response

### "No research results"
- Try simplifying your question
- Check Valyu API key is valid
- Verify internet connection

### "Agent answers everything directly"
- Agent is using smart detection
- Not all questions need research
- Only complex/recent queries trigger research

## Advanced Usage

### Setting Question Topics

By asking in a certain way, you influence the types of questions:

```
"Tell me about neural networks"
→ Questions about theory, applications, complexity level

"How to implement machine learning"
→ Questions about language, framework, skill level

"Recent breakthroughs in AI"
→ Questions about domain, depth, current state
```

### Following Up

After research completes, you can ask:

```
You: "Tell me more about quantum error correction"
Agent: [Triggers new research on that subtopic]

You: "Who wrote this paper?"
Agent: [Searches transcript for author info]

You: "Can you find implementations?"
Agent: [New research for implementation examples]
```

## Tips for Best Results

### ✅ Do This:
- Ask clear, specific questions
- Answer questions directly (one or two words often works)
- Let the agent finish speaking before responding
- Ask follow-up questions after research

### ❌ Don't:
- Interrupt too early (agent needs context)
- Ask extremely vague questions ("Tell me everything about AI")
- Try to converse like it's a chat app
- Expect real-time data (research takes 5-10 seconds)

## Performance Expectations

- **Smart detection check**: ~500ms
- **Question generation**: ~1-2 seconds
- **Waiting for your answers**: Real-time
- **Valyu research**: ~3-5 seconds
- **Summary generation**: ~1-2 seconds
- **Total research flow**: ~7-10 seconds

## Architecture

```
You (Voice Input)
    ↓
STT: AssemblyAI (Speech-to-Text)
    ↓
Agent decides: Research needed?
    ↓ (if yes)
Generate 3 clarifying questions (OpenAI)
    ↓
Speak questions (Cartesia TTS)
    ↓
Wait for answers (Voice Input)
    ↓ (all 3 answered)
Valyu DeepSearch (Research API)
    ↓
Generate summary (OpenAI)
    ↓
Speak summary (Cartesia TTS)
    ↓
You (Voice Output)
    ↓
Save to transcripts (JSON + Text)
```

## Getting Help

- **Setup issues**: See README.md
- **Advanced customization**: See RESEARCH_SETUP.md
- **Implementation details**: See IMPLEMENTATION_SUMMARY.md
- **LiveKit docs**: https://docs.livekit.io/agents/
- **Valyu docs**: https://docs.valyu.ai/

---

**Ready to use?** Run `uv run agent.py dev` and start asking questions!
