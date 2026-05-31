from tools.web_tool import web_search
from llm.model import llm
from utils.logger import logger


def web_search_node(state):

    logger.info(
        "Web Search Agent Started..."
    )

    query = state["query"]

    results = web_search.invoke(
        {"query": query}
    )

    if not results:

        return {
            "final_answer":
            "No search results found."
        }

    summary = llm.invoke(
        f"""
        User Query:
        {query}

        Search Results:
        {results}

        Based on the search results,
        answer the user's question clearly.
        """
    )

    logger.info(
        "Web Search Agent Completed..."
    )

    return {
        "final_answer":
        summary.content
    }