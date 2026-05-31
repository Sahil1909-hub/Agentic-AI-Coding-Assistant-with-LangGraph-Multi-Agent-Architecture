from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from utils.logger import logger

class AgentState(TypedDict):

    query: str

    route: str

    final_answer: str
    
    messages: Annotated[list, add_messages]

    plan: str
    research: str
    code: str
    review: str
    tests: str
    documentation: str


logger.info('State created..')