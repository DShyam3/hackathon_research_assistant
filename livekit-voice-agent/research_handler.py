import os
import json
import re
from typing import Optional
from datetime import datetime
from enum import Enum
from openai import OpenAI
from valyu import Valyu


class ResearchState(Enum):
    """Enum for research conversation states"""
    IDLE = "idle"
    GENERATING_QUESTIONS = "generating_questions"
    ASKING_QUESTION_1 = "asking_question_1"
    ASKING_QUESTION_2 = "asking_question_2"
    ASKING_QUESTION_3 = "asking_question_3"
    RESEARCHING = "researching"
    DELIVERING_RESULTS = "delivering_results"


class ResearchSession:
    """Manages a research session including clarifying questions and Valyu search"""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.state = ResearchState.IDLE
        self.original_query = ""
        self.clarifying_questions = []
        self.user_answers = []
        self.research_results = None
        self.research_summary = ""

        # Initialize API clients
        self.openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.valyu_client = Valyu(api_key=os.getenv("VALYU_API_KEY"))

    async def should_research(self, query: str) -> bool:
        """Use LLM to determine if query needs research or can be answered directly"""
        prompt = f"""Does this question require current information, recent data, or research?
Answer with only 'yes' or 'no'.

Question: {query}"""

        try:
            response = self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=10,
                temperature=0.3  # Lower temperature for consistent yes/no
            )

            answer = response.choices[0].message.content.strip().lower()
            return answer.startswith('yes')
        except Exception as e:
            print(f"Error in should_research: {e}")
            return False

    def get_voice_status_updates(self) -> dict:
        """Return minimal status messages for each research state"""
        return {
            ResearchState.IDLE: None,
            ResearchState.GENERATING_QUESTIONS: "Researching...",
            ResearchState.ASKING_QUESTION_1: None,  # Question itself is the update
            ResearchState.ASKING_QUESTION_2: None,
            ResearchState.ASKING_QUESTION_3: None,
            ResearchState.RESEARCHING: "Searching...",
            ResearchState.DELIVERING_RESULTS: None   # Summary is the update
        }

    async def initiate_research(self, query: str) -> str:
        """Start research process and generate first clarifying question"""
        self.original_query = query
        self.state = ResearchState.GENERATING_QUESTIONS

        # Generate 3 clarifying questions
        self.clarifying_questions = await self._generate_questions(query)

        # Move to asking first question
        self.state = ResearchState.ASKING_QUESTION_1
        self.user_answers = [None, None, None]

        return f"I'll research that for you. Let me ask a few clarifying questions to give you the best results. Question 1 of 3: {self.clarifying_questions[0]}"

    async def _generate_questions(self, query: str) -> list[str]:
        """Generate 3 short clarifying questions using OpenAI - max 10 words each for voice"""
        prompt = f"""Generate exactly 3 SHORT clarifying questions (max 10 words each) for voice conversation.
Make them simple, conversational, and easy to understand when spoken.
Return ONLY the questions, one per line, without numbering.

Topic: {query}"""

        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )

        # Parse the response to extract questions
        text = response.choices[0].message.content
        questions = [q.strip() for q in text.split('\n') if q.strip()]
        return questions[:3]  # Ensure we have exactly 3

    def record_answer(self, answer: str) -> Optional[str]:
        """Record user's answer to current question and move to next or research"""
        current_question_index = {
            ResearchState.ASKING_QUESTION_1: 0,
            ResearchState.ASKING_QUESTION_2: 1,
            ResearchState.ASKING_QUESTION_3: 2,
        }.get(self.state)

        if current_question_index is not None:
            self.user_answers[current_question_index] = answer

            if current_question_index == 0:
                self.state = ResearchState.ASKING_QUESTION_2
                return f"Question 2 of 3: {self.clarifying_questions[1]}"
            elif current_question_index == 1:
                self.state = ResearchState.ASKING_QUESTION_3
                return f"Question 3 of 3: {self.clarifying_questions[2]}"
            elif current_question_index == 2:
                # All questions answered, move to research
                self.state = ResearchState.RESEARCHING
                return None  # Signal to start research

        return None

    async def execute_research(self) -> str:
        """Execute Valyu search with enhanced query from clarifying questions"""
        self.state = ResearchState.RESEARCHING

        # Build enhanced search query from answers
        enhanced_query = self._build_enhanced_query()

        try:
            # Execute Valyu search
            response = self.valyu_client.search(
                enhanced_query,
                search_type="proprietary",
                max_num_results=10,
                max_price=30,
                relevance_threshold=0.5,
                included_sources=["valyu/valyu-arxiv", "valyu/valyu-pubmed"],
                is_tool_call=True
            )

            self.research_results = response

            # Generate summary for voice delivery
            self.research_summary = await self._generate_summary()

            self.state = ResearchState.DELIVERING_RESULTS
            return self.research_summary

        except Exception as e:
            return f"I encountered an error while researching: {str(e)}"

    def _build_enhanced_query(self) -> str:
        """Build enhanced search query combining original question with answers"""
        query_parts = [self.original_query]

        if self.user_answers[0]:
            query_parts.append(self.user_answers[0])
        if self.user_answers[1]:
            query_parts.append(self.user_answers[1])
        if self.user_answers[2]:
            query_parts.append(self.user_answers[2])

        return " ".join(query_parts)

    async def _generate_summary(self) -> str:
        """Generate concise summary of research results for voice delivery"""
        if not self.research_results or not self.research_results.get("results"):
            return "I wasn't able to find specific results for that query."

        # Extract top 3 results
        top_results = self.research_results["results"][:3]
        results_text = "\n".join([
            f"- {r.get('title', 'Unknown')}: {r.get('content', '')[:150]}..."
            for r in top_results
        ])

        prompt = f"""Create a brief, conversational 2-3 point summary (suitable for voice delivery)
from these research results. Focus on the most important insights. Do NOT mention sources or URLs.

Results:
{results_text}"""

        response = self.openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )

        summary = response.choices[0].message.content
        return f"Here's what I found: {summary}"

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
        if not self.research_results or not self.research_results.get("results"):
            return []

        formatted = []
        for result in self.research_results["results"]:
            formatted.append({
                "title": result.get("title"),
                "url": result.get("url"),
                "source": result.get("source"),
                "content_preview": result.get("content", "")[:300],
                "relevance_score": result.get("relevance_score"),
                "authors": result.get("authors"),
                "publication_date": result.get("publication_date"),
                "doi": result.get("doi"),
                "citation_count": result.get("citation_count")
            })

        return formatted

    def reset(self):
        """Reset session for new research query"""
        self.state = ResearchState.IDLE
        self.original_query = ""
        self.clarifying_questions = []
        self.user_answers = []
        self.research_results = None
        self.research_summary = ""
