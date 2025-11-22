import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_valyu import ValyuSearchTool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env.local in the same directory
env_path = os.path.join(os.path.dirname(__file__), '.env.local')
load_dotenv(dotenv_path=env_path)

def get_clarifying_questions(query: str, llm: ChatAnthropic) -> list[str]:
    """
    Ask the LLM to generate clarifying questions for a given query.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful research assistant. Your goal is to understand the user's request fully before performing a search. "
                   "Given the user's query, generate 3 clarifying questions that would help you provide a better answer. "
                   "Return ONLY the questions, one per line."),
        ("user", "{query}")
    ])
    chain = prompt | llm
    response = chain.invoke({"query": query})
    questions = [q.strip() for q in response.content.split('\n') if q.strip()]
    return questions

def main():
    # Check for API keys
    if not os.getenv("VALYU_API_KEY"):
        print("Error: VALYU_API_KEY not found in environment variables.")
        print(f"Please add it to {env_path}")
        return
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Error: ANTHROPIC_API_KEY not found in environment variables.")
        print(f"Please add it to {env_path}")
        return

    # Initialize LLM
    llm = ChatAnthropic(model="claude-3-5-sonnet-20240620", temperature=0)

    # Initialize Valyu Tool
    valyu_tool = ValyuSearchTool()
    tools = [valyu_tool]

    # Create the agent
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful research assistant. You have access to a search tool called Valyu. "
                   "Use it to find information and answer the user's questions. "
                   "Always cite your sources if provided by the tool."),
        ("user", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])

    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Interactive loop
    print("Valyu Research Agent Initialized.")
    while True:
        user_query = input("\nEnter your research topic (or 'quit' to exit): ")
        if user_query.lower() in ['quit', 'exit']:
            break

        print("\nAnalyzing query...")
        
        # Step 1: Clarifying Questions
        questions = get_clarifying_questions(user_query, llm)
        print("\nTo better understand your request, I have a few clarifying questions:")
        
        answers = []
        for i, q in enumerate(questions, 1):
            answer = input(f"{i}. {q}\nAnswer: ")
            answers.append(f"Q: {q}\nA: {answer}")
        
        # Step 2: Deep Research
        refined_query = f"Original Query: {user_query}\n\nContext from Clarifying Questions:\n" + "\n".join(answers)
        print("\nPerforming deep research with Valyu...")
        
        result = agent_executor.invoke({"input": refined_query})
        
        print("\n=== Research Results ===")
        print(result["output"])
        print("========================")

if __name__ == "__main__":
    main()
