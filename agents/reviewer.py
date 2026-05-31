from prompts.reviewer_prompt import REVIEWER_PROMPT
from llm.model import llm
from utils.logger import logger


def reviewer_node(state):

    logger.info('Reviewer agent started..')

    code = state['code']

    prompt = REVIEWER_PROMPT.format(
        code = code
    )

    response = llm.invoke(prompt)

    logger.info('Reviewer agent completed..')

    return {
        "review": response.content
    }


    
