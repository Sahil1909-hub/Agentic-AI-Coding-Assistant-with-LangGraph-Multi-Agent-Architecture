from ddgs import DDGS
from utils.logger import logger
from langchain.tools import tool


@tool
def web_search(query, max_results=5):
    """Search users query from web"""

    logger.info('Web search tool started..')

    results = []

    with DDGS() as ddgs:

        search_results = ddgs.text(
            query,
            max_results=max_results
        )

        for result in search_results:

            results.append(
                {
                    "title": result["title"],
                    "link": result["href"],
                    "snippet": result["body"]
                }
            )

    return results