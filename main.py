from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
import os
from langchain_tavily import TavilySearch
from tavily import TavilyClient

load_dotenv()

"""
Custom Function and Tool for AI Agent
"""
# tavily = TavilyClient()
# @tool
# def search(query: str) -> str:
#     """
#     Tool that searches over internet
#     Args:
#         query: The query to search for
#     Returns:
#         The search result
#     """
#     print(f"Searching for {query}")
#     return tavily.search(query=query)


llm = ChatOllama(temperature=0, model="llama3.1:8b")

# tools = [search] ; calling search function in a tools variable.
tools = [TavilySearch()] #calling Tavily Search of Langchain
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-based-search-agent!")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo?")})
    print(result)


if __name__ == "__main__":
    main()
