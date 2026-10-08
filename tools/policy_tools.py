from crewai.tools import tool

from rag.policy_rag import search_policy


@tool("Search E-commerce Policies")
def search_ecommerce_policy(question: str) -> str:
    """Search the e-commerce policy knowledge base using RAG."""

    return search_policy(question)