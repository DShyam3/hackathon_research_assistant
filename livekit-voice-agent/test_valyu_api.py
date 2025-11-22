"""
Valyu API Test Script
This script tests various Valyu API features including:
- Basic Search
- Advanced Search (Academic Research)
- Financial Data Search
- Content Extraction
- Answer API

Based on the Valyu quickstart guide and referencing existing agent code.
"""

import os
from dotenv import load_dotenv
from valyu import Valyu

# Load environment variables from .env.local in the same directory
env_path = os.path.join(os.path.dirname(__file__), '.env.local')
load_dotenv(dotenv_path=env_path)


def print_section(title: str):
    """Print a formatted section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def test_basic_search(valyu: Valyu):
    """Test basic Valyu search functionality"""
    print_section("TEST 1: Basic Search")
    
    query = "What is quantum computing?"
    print(f"Query: {query}\n")
    
    response = valyu.search(query)
    
    print(f"Success: {response.success}")
    print(f"Transaction ID: {response.tx_id}")
    print(f"Total Results: {len(response.results)}\n")
    
    for i, result in enumerate(response.results[:3], 1):  # Show first 3 results
        print(f"--- Result {i} ---")
        print(f"Title: {result.title}")
        print(f"Source: {result.source}")
        print(f"URL: {result.url}")
        print(f"Content Preview: {result.content[:200]}...")
        print(f"Relevance Score: {result.relevance_score}")
        print()


def test_academic_search(valyu: Valyu):
    """Test academic research search with proprietary sources"""
    print_section("TEST 2: Academic Research Search")
    
    query = "Extending context window of large language models via positional interpolation"
    print(f"Query: {query}\n")
    
    response = valyu.search(
        query,
        search_type="proprietary",
        max_num_results=5,
        max_price=30,
        included_sources=["valyu/valyu-arxiv"]
    )
    
    print(f"Success: {response.success}")
    print(f"Total Results: {len(response.results)}\n")
    
    for i, result in enumerate(response.results, 1):
        print(f"--- Academic Paper {i} ---")
        print(f"Title: {result.title}")
        print(f"Authors: {', '.join(result.authors) if hasattr(result, 'authors') and result.authors else 'N/A'}")
        print(f"Publication Date: {getattr(result, 'publication_date', 'N/A')}")
        print(f"DOI: {getattr(result, 'doi', 'N/A')}")
        print(f"Citation Count: {getattr(result, 'citation_count', 'N/A')}")
        print(f"URL: {result.url}")
        print(f"Content Preview: {result.content[:300]}...")
        print(f"Relevance Score: {result.relevance_score}")
        print()


def test_financial_data(valyu: Valyu):
    """Test financial market data search"""
    print_section("TEST 3: Financial Market Data Search")
    
    query = "Tesla stock price today"
    print(f"Query: {query}\n")
    
    response = valyu.search(
        query,
        search_type="proprietary",
        max_num_results=1,
        max_price=30
    )
    
    print(f"Success: {response.success}")
    print(f"Total Results: {len(response.results)}\n")
    
    for result in response.results:
        print(f"Title: {result.title}")
        print(f"Source: {result.source}")
        print(f"URL: {result.url}")
        print(f"Data Type: {result.data_type}")
        print(f"Source Type: {result.source_type}")
        
        # For structured financial data, show sample data points
        if result.data_type == "structured" and isinstance(result.content, list):
            print(f"Sample Data Points: {len(result.content)} entries")
            for item in result.content[:3]:
                print(f"  {item}")
        else:
            print(f"Content Preview: {str(result.content)[:300]}...")
        print()


def test_content_extraction(valyu: Valyu):
    """Test content extraction API"""
    print_section("TEST 4: Content Extraction")
    
    url = "https://techcrunch.com/category/artificial-intelligence/"
    print(f"URL: {url}\n")
    
    data = valyu.contents(
        urls=[url],
        response_length="medium",
        extract_effort="auto",
    )
    
    if hasattr(data, 'results') and data.results:
        result = data.results[0]
        print(f"Title: {getattr(result, 'title', 'N/A')}")
        print(f"URL: {getattr(result, 'url', 'N/A')}")
        print(f"Content Preview (first 500 chars):")
        print(result.content[:500])
        print("...")
    else:
        print("No results returned")
        print(f"Response: {data}")


def test_answer_api(valyu: Valyu):
    """Test Answer API for AI-powered responses"""
    print_section("TEST 5: AI-Powered Answer API")
    
    query = "latest developments in quantum computing"
    print(f"Query: {query}\n")
    
    data = valyu.answer(
        query=query,
    )
    
    if hasattr(data, 'contents'):
        print("AI-Generated Response:")
        print(data.contents)
    elif hasattr(data, 'answer'):
        print("AI-Generated Response:")
        print(data.answer)
    else:
        print("Response:")
        print(data)


def test_realtime_web_search(valyu: Valyu):
    """Test real-time web search with current date to verify up-to-date information"""
    print_section("TEST 6: Real-Time Web Search (Current Information)")
    
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    query = f"latest AI developments and news as of {current_date}"
    print(f"Query: {query}")
    print(f"Current Date: {current_date}\n")
    
    response = valyu.search(
        query,
        search_type="web",  # Web search for current information
        max_num_results=5,
        max_price=30,
        is_tool_call=True
    )
    
    print(f"Success: {response.success}")
    print(f"Total Results: {len(response.results)}\n")
    
    for i, result in enumerate(response.results, 1):
        print(f"--- Result {i} ---")
        print(f"Title: {result.title}")
        print(f"URL: {result.url}")
        print(f"Source: {result.source}")
        print(f"Relevance Score: {result.relevance_score}")
        print(f"Content Preview: {result.content[:200]}...")
        print()


def test_advanced_search(valyu: Valyu):
    """Test advanced search with multiple parameters"""
    print_section("TEST 7: Advanced Search with Parameters")
    
    query = "Implementation details of agentic search-enhanced large reasoning models"
    print(f"Query: {query}\n")
    
    response = valyu.search(
        query,
        search_type="proprietary",
        max_num_results=5,
        max_price=30,
        relevance_threshold=0.5,
        category="agentic retrieval-augmented generation",
        included_sources=["valyu/valyu-arxiv"],
        is_tool_call=True
    )
    
    print(f"Success: {response.success}")
    print(f"Total Results: {len(response.results)}")
    print(f"Results by Source: {response.results_by_source}\n")
    
    for i, result in enumerate(response.results, 1):
        print(f"--- Result {i} ---")
        print(f"Title: {result.title}")
        print(f"URL: {result.url}")
        print(f"Source: {result.source}")
        print(f"Relevance Score: {result.relevance_score}")
        print(f"Content Preview: {result.content[:200]}...")
        print()


def main():
    """Main test runner"""
    # Check for API key
    api_key = os.getenv("VALYU_API_KEY")
    if not api_key:
        print("❌ Error: VALYU_API_KEY not found in environment variables.")
        print(f"Please add it to: {env_path}")
        return
    
    print("=" * 80)
    print("  Valyu API Test Suite")
    print("=" * 80)
    print(f"\nEnvironment: {env_path}")
    print(f"API Key: {api_key[:10]}...{api_key[-4:]}")
    
    # Initialize Valyu client
    valyu = Valyu(api_key)
    
    # Run all tests
    try:
        test_basic_search(valyu)
        test_academic_search(valyu)
        test_financial_data(valyu)
        test_content_extraction(valyu)
        test_answer_api(valyu)
        test_realtime_web_search(valyu)  # New test for real-time web search
        test_advanced_search(valyu)
        
        print_section("All Tests Completed Successfully! ✅")
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
