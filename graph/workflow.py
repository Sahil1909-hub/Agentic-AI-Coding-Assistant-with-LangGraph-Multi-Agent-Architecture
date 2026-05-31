from langgraph.graph import StateGraph,START, END
from graph.state import AgentState
from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.coder import coder_node
from agents.reviewer import reviewer_node
from agents.tester import tester_node
from agents.router import router_node
from agents.web_search_agent import web_search_node
from agents.github_agent import github_node
from agents.chat_agent import chat_node
from agents.documenter import documenter_node
from utils.logger import logger
from tools.web_tool import web_search
from tools.github_tool import search_github_repositories
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


memory = MemorySaver()

tool_node = ToolNode(
    [
        web_search,
        search_github_repositories
    ]
)


logger.info('Graph workflow started..')

graph = StateGraph(AgentState)

# -------------------------
# Router Layer
# -------------------------

graph.add_node("router", router_node)
graph.add_node("chat", chat_node)
graph.add_node("github", github_node)
graph.add_node("web_search", web_search_node)


# -------------------------
# Coding Pipeline
# -------------------------

graph.add_node("planner", planner_node)
graph.add_node("researcher", researcher_node)
graph.add_node("tools", tool_node)
graph.add_node("coder", coder_node)
graph.add_node("reviewer", reviewer_node)
graph.add_node("tester", tester_node)
graph.add_node("documenter", documenter_node)

logger.info("Nodes added successfully")

graph.add_edge(START, "router")

# -------------------------
# Router Decisions
# -------------------------

graph.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "CHAT": "chat",
        "WEB_SEARCH": "web_search",
        "GITHUB": "github",
        "CODING": "planner"
    }
)

# -------------------------
# Direct End Routes
# -------------------------

graph.add_edge("chat",END)
graph.add_edge("web_search",END)
graph.add_edge("github",END)

# -------------------------
# Coding Workflow
# -------------------------
graph.add_edge("planner", "researcher")

graph.add_conditional_edges(
    "researcher",
    tools_condition,
    {
        "tools": "tools",
        "__end__": "coder"
    }
)
graph.add_edge("tools","researcher")
graph.add_edge("coder", "reviewer")
graph.add_edge("reviewer", "tester")
graph.add_edge("tester", "documenter")
graph.add_edge("documenter", END)

logger.info('Edges added..')

graph = graph.compile(
    checkpointer=memory
)

logger.info('Graph created..')






