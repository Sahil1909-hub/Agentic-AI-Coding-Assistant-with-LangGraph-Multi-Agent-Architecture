from llm.model import llm
from tools.github_tool import (
    search_github_repositories
)
from utils.logger import logger


def github_node(state):

    query = state["query"]

    logger.info(
        f"Original Query: {query}"
    )

    # Extract GitHub search keywords
    keyword_response = llm.invoke(
        f"""
        Extract only the most relevant GitHub repository search keywords.

        Rules:
        - Return only keywords.
        - No explanations.
        - No extra text.
        - Maximum 3-5 words.

        Examples:

        Find LangGraph repositories
        -> langgraph

        Best FastAPI projects on GitHub
        -> fastapi

        Show React dashboard repositories
        -> react dashboard

        User Query:
        {query}
        """
    )

    search_query = (
        keyword_response.content.strip()
    )

    logger.info(
        f"Search Query: {search_query}"
    )

    repos = search_github_repositories.invoke(
        {
            "query": search_query
        }
    )

    logger.info(
        f"Repositories Found: {len(repos)}"
    )

    if not repos:

        return {
            "final_answer":
            f"No repositories found for '{search_query}'."
        }

    formatted = []

    for repo in repos:

        formatted.append(
            f"""
        Repository: {repo['name']}
        Stars: {repo['stars']}
        Description: {repo['description']}
        URL: {repo['url']}
        """
        )

    return {
        "final_answer":
        "\n".join(formatted)
    }