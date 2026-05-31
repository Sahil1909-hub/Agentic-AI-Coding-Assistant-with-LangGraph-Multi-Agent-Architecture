from llm.model import llm
from utils.logger import logger


def router_node(state):

    query = state["query"]

    prompt = f"""
    Classify the user query.

    Return ONLY one of:

    CHAT
    WEB_SEARCH
    GITHUB
    CODING

    Examples:

    What is Python?
    -> CHAT

    Weather in Mumbai
    -> WEB_SEARCH

    Latest AI news
    -> WEB_SEARCH

    Search FastAPI repositories
    -> GITHUB

    Build a weather app
    -> CODING

    Query:
    {query}
    """

    response = llm.invoke(prompt)

    return {
        "route": response.content.strip().upper()
    }

