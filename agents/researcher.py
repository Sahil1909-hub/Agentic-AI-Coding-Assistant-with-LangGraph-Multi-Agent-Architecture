from llm.model import llm
from prompts.researcher_prompt import RESEARCHER_PROMPT
from utils.logger import logger
from tools.web_tool import web_search
from tools.github_tool import search_github_repositories

tools = [
    web_search,
    search_github_repositories
]

llm_with_tools = llm.bind_tools(
    tools
)

def researcher_node(state):

    logger.info('Researcher agent started..')

    messages = state['messages']

    response = llm_with_tools.invoke(messages)

    logger.info('Researcher agent completed..')

    return {
    "research": response.content,
    "messages": [response]
}
