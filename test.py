from tools.github_tool import (
    search_github_repositories
)

result = search_github_repositories.invoke(
    {
        "query": "langgraph"
    }
)

print(result)