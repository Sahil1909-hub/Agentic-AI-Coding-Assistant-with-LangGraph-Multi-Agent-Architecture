from llm.model import llm
from prompts.tester_prompt import TESTER_PROMPT
from utils.logger import logger


def tester_node(state):

    logger.info('Tester agent started..')

    code = state['code']

    prompt = TESTER_PROMPT.format(
        code = code
    )

    response = llm.invoke(prompt)

    logger.info('Tester agent completed..')

    return {
        "tests": response.content
    }

