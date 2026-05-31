from llm.model import llm
from prompts.planner_prompt import PLANNER_PROMPT
from utils.logger import logger


def planner_node(state):

    logger.info('Planner agent started..')

    query = state['query']

    prompt = PLANNER_PROMPT.format(
        query = query
    )

    response = llm.invoke(prompt)
    
    logger.info('Planner agent completed')


    return {
        "plan": response.content
    }