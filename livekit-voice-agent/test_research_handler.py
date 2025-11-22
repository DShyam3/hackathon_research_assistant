"""
Test script to verify the ResearchSession class works correctly with Valyu API.
This tests the research handler in isolation before running the full voice agent.
"""

import asyncio
import os
from dotenv import load_dotenv
from research_handler import ResearchSession

# Load environment variables
load_dotenv('.env.local')


async def test_research_flow():
    """Test the complete research flow"""
    print("=" * 80)
    print("  Testing ResearchSession with Valyu API")
    print("=" * 80)
    
    # Check API keys
    if not os.getenv("VALYU_API_KEY"):
        print("❌ Error: VALYU_API_KEY not found")
        return
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found")
        return
    
    print("\n✅ API keys found\n")
    
    # Initialize research session
    session = ResearchSession(session_id="test_session")
    
    # Test query
    query = "What are the latest developments in quantum computing?"
    print(f"Query: {query}\n")
    
    # Step 1: Check if research is needed
    print("Step 1: Checking if research is needed...")
    needs_research = await session.should_research(query)
    print(f"Needs research: {needs_research}\n")
    
    if not needs_research:
        print("Query doesn't need research. Exiting.")
        return
    
    # Step 2: Initiate research and get first question
    print("Step 2: Initiating research...")
    first_question = await session.initiate_research(query)
    print(f"First question: {first_question}\n")
    
    # Simulate user answers
    mock_answers = [
        "Recent developments",
        "Practical applications",
        "Intermediate level"
    ]
    
    # Step 3: Answer clarifying questions
    for i, answer in enumerate(mock_answers, 1):
        print(f"Step {i + 2}: Answering question {i}...")
        print(f"Answer: {answer}")
        next_prompt = session.record_answer(answer)
        if next_prompt:
            print(f"Next prompt: {next_prompt}\n")
        else:
            print("All questions answered. Ready to search.\n")
    
    # Step 4: Execute research
    print("Step 5: Executing Valyu search...")
    try:
        summary = await session.execute_research()
        print("\n" + "=" * 80)
        print("  RESEARCH SUMMARY")
        print("=" * 80)
        print(summary)
        print("\n" + "=" * 80)
        
        # Step 5: Check transcript entry
        print("\nStep 6: Generating transcript entry...")
        transcript = session.get_transcript_entry()
        print(f"\n✅ Transcript generated with {len(transcript.get('detailed_results', []))} results")
        
        # Show sample result
        if transcript.get('detailed_results'):
            print("\nSample result:")
            result = transcript['detailed_results'][0]
            print(f"  Title: {result['title']}")
            print(f"  URL: {result['url']}")
            print(f"  Source: {result['source']}")
            print(f"  Relevance: {result['relevance_score']}")
            if result.get('authors'):
                print(f"  Authors: {result['authors']}")
        
        print("\n" + "=" * 80)
        print("  ✅ ALL TESTS PASSED!")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Error during research: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_research_flow())
