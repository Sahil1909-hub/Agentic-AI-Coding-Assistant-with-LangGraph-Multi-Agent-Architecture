from llm.model import llm
from prompts.coder_prompt import CODER_PROMPT
from utils.logger import logger


def coder_node(state):

    logger.info('Coder agent started..')

    plan = state['plan']

    research = state['research']

    prompt = CODER_PROMPT.format(
        plan = plan,
        research = research
    )

    response = llm.invoke(prompt)

    logger.info('Coder agent completed..')

    return {
        "code": response.content
    }
    
