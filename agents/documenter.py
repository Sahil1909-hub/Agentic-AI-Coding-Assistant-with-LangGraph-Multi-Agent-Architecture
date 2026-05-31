from llm.model import llm
from prompts.documenter_prompt import DOCUMENTER_PROMPT
from utils.logger import logger
from tools.file_tool import save_file


def documenter_node(state):
    logger.info('Documenter agent started')

    code = state['code']

    prompt = DOCUMENTER_PROMPT.format(
        code = code
    )

    response = llm.invoke(prompt)

    documentation = response.content

    save_file(
        "generated_projects/README.md",
        documentation
    )

    logger.info('Documenter agent completed..')

    return {
        "documentation": documentation
    }
