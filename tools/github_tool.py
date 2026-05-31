import requests
from utils.logger import logger
from langchain.tools import tool


@tool
def search_github_repositories(query, limit=5):
    """Search Github Repositories"""

    logger.info('Github tool inialized..')

    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": limit
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    repositories = []

    for repo in data["items"]:

        repositories.append(
            {
                "name": repo["full_name"],
                "url": repo["html_url"],
                "stars": repo["stargazers_count"],
                "description": repo["description"]
            }
        )

    return repositories