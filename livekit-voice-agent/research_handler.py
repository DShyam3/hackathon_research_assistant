import os
import json
from typing import Optional
from datetime import datetime
from enum import Enum
from pathlib import Path
from openai import OpenAI
from valyu import Valyu


class ResearchState(Enum):
    """Enum for research conversation states"""
    IDLE = "idle"
    ASKING_QUESTIONS = "asking_questions"
    COLLECTING_ANSWERS = "collecting_answers"
    RESEARCHING = "researching"
    DELIVERING_RESULTS = "delivering_results"


class ResearchSession:
    """Manages a research session with Valyu search"""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.state = ResearchState.IDLE
        self.original_query = ""
        self.clarifying_questions = []
        self.user_answers = []
        self.research_results = None
        self.research_summary = ""
        self.answer_count = 0

        # Create research output directory
        self.research_dir = Path("research_results")
        self.research_dir.mkdir(exist_ok=True)

        # Initialize API clients
        print(f"DEBUG: Initializing ResearchSession with id: {session_id}")
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.valyu_client = Valyu(api_key=os.getenv("VALYU_API_KEY"))
        print(f"DEBUG: API clients initialized")

    async def should_research(self, query: str) -> bool:
        """Always force research for all queries - no LLM fallback"""
        return True

    async def initiate_research(self, query: str) -> None:
        """Start research immediately - no clarifying questions"""
        self.original_query = query
        self.state = ResearchState.RESEARCHING
        self.clarifying_questions = []
        self.user_answers = []
        self.answer_count = 0

    def record_answer(self, answer: str) -> bool:
        """Not used in simplified flow"""
        return False

    async def execute_research(self) -> str:
        """Execute Valyu search with robust error handling"""
        self.state = ResearchState.RESEARCHING

        # Build enhanced search query from answers
        enhanced_query = self._build_enhanced_query()
        print(f"DEBUG: Enhanced query for Valyu: {enhanced_query}")

        try:
            # Execute Valyu search with retries
            print(f"DEBUG: Calling Valyu search...")
            response = await self._search_with_retry(enhanced_query)

            if not response or not hasattr(response, 'results') or not response.results:
                return "I couldn't find results for that query. Try asking again differently."

            self.research_results = response

            # Generate summary for voice delivery
            self.research_summary = await self._generate_summary()
            self.state = ResearchState.DELIVERING_RESULTS
            return self.research_summary

        except Exception as e:
            error_msg = str(e)
            print(f"Error in execute_research: {error_msg}")
            return f"I encountered an error. {error_msg[:50]}"

    async def _search_with_retry(self, query: str, retries: int = 2):
        """Execute Valyu search with retry logic"""
        for attempt in range(retries):
            try:
                print(f"DEBUG: Valyu search attempt {attempt + 1} for query: {query}")
                response = self.valyu_client.search(
                    query,
                    search_type="all",  # Search both web and proprietary sources
                    max_num_results=15,  # Increased for more comprehensive results
                    response_length="large",  # ~100k characters per result for detail
                    max_price=30,
                    relevance_threshold=0.5,
                    is_tool_call=True  # Optimized for AI processing
                )
                print(f"DEBUG: Valyu search successful, got response")
                return response
            except Exception as e:
                print(f"Valyu search attempt {attempt + 1} failed: {e}")
                if attempt < retries - 1:
                    import asyncio
                    await asyncio.sleep(1)
                else:
                    raise

    def _build_enhanced_query(self) -> str:
        """Build search query from original question and answer"""
        parts = [self.original_query]
        if self.user_answers and self.user_answers[0]:
            parts.append(self.user_answers[0])
        return " ".join(parts)

    async def _generate_summary(self) -> str:
        """Generate detailed summary of research results"""
        if not self.research_results or not hasattr(self.research_results, 'results') or not self.research_results.results:
            return "No results found for that query."

        try:
            # Extract top 5 results for more comprehensive summary
            top_results = self.research_results.results[:5]
            results_text = "\n".join([
                f"- {getattr(r, 'title', 'N/A')}: {r.content[:300] if hasattr(r, 'content') and r.content else 'N/A'}"
                for r in top_results
            ])

            prompt = f"""Provide a detailed summary in 3-4 sentences covering the key findings from these research results:

{results_text}"""

            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,  # Increased for more detailed summary
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating summary: {e}")
            return "I found results but couldn't summarize them."

    def get_transcript_entry(self) -> dict:
        """Generate transcript entry with full research details"""
        return {
            "timestamp": datetime.now().isoformat(),
            "type": "research_session",
            "session_id": self.session_id,
            "original_query": self.original_query,
            "clarifying_questions": self.clarifying_questions,
            "user_answers": self.user_answers,
            "research_summary": self.research_summary,
            "detailed_results": self._format_detailed_results() if self.research_results else None
        }

    def _format_detailed_results(self) -> list[dict]:
        """Format detailed research results for transcript"""
        if not self.research_results or not hasattr(self.research_results, 'results') or not self.research_results.results:
            return []

        formatted = []
        for result in self.research_results.results:
            formatted.append({
                "title": getattr(result, 'title', 'N/A'),
                "url": getattr(result, 'url', 'N/A'),
                "source": getattr(result, 'source', 'N/A'),
                "content_preview": result.content[:300] if hasattr(result, 'content') and result.content else "",
                "relevance_score": getattr(result, 'relevance_score', None),
                "authors": getattr(result, 'authors', None),
                "publication_date": getattr(result, 'publication_date', None),
                "doi": getattr(result, 'doi', None),
                "citation_count": getattr(result, 'citation_count', None)
            })

        return formatted

    def save_research_as_markdown(self) -> Optional[str]:
        """Save research results to a markdown file and return the file path"""
        if not self.research_results or not hasattr(self.research_results, 'results'):
            print("No research results to save")
            return None

        try:
            # Create filename based on timestamp and query
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            query_slug = self.original_query[:30].replace(" ", "_")
            filename = f"research_{timestamp}_{query_slug}.md"
            filepath = self.research_dir / filename

            # Build markdown content
            markdown_content = self._generate_markdown_content()

            # Write to file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)

            print(f"✅ Research saved to {filepath}")
            return str(filepath)

        except Exception as e:
            print(f"Error saving research to markdown: {e}")
            return None

    def _generate_markdown_content(self) -> str:
        """Generate markdown formatted research content"""
        lines = []

        # Header
        lines.append("# Research Results\n")
        lines.append(f"**Query:** {self.original_query}\n")

        if self.user_answers and self.user_answers[0]:
            lines.append(f"**Clarification:** {self.user_answers[0]}\n")

        lines.append(f"**Timestamp:** {datetime.now().isoformat()}\n")
        lines.append(f"**Summary:** {self.research_summary}\n")

        # Detailed Results
        lines.append("\n## Detailed Results\n")

        if self.research_results and hasattr(self.research_results, 'results') and self.research_results.results:
            for i, result in enumerate(self.research_results.results, 1):
                lines.append(f"\n### Result {i}\n")
                lines.append(f"**Title:** {getattr(result, 'title', 'N/A')}\n")

                if hasattr(result, 'url') and result.url:
                    lines.append(f"**URL:** {result.url}\n")

                lines.append(f"**Source:** {getattr(result, 'source', 'N/A')}\n")

                if hasattr(result, 'content') and result.content:
                    lines.append(f"\n**Content:**\n{result.content}\n")

                if hasattr(result, 'authors') and result.authors:
                    lines.append(f"**Authors:** {result.authors}\n")

                if hasattr(result, 'publication_date') and result.publication_date:
                    lines.append(f"**Published:** {result.publication_date}\n")

                if hasattr(result, 'citation_count') and result.citation_count:
                    lines.append(f"**Citations:** {result.citation_count}\n")
        else:
            lines.append("\nNo results found.\n")

        return "".join(lines)

    def reset(self):
        """Reset session for new research query"""
        self.state = ResearchState.IDLE
        self.original_query = ""
        self.clarifying_questions = []
        self.user_answers = []
        self.research_results = None
        self.research_summary = ""
        self.answer_count = 0
