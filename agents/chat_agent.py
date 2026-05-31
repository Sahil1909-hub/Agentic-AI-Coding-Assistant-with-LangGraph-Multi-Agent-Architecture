from llm.model import llm


def chat_node(state):

    query = state["query"]

    response = llm.invoke(query)

    return {
        "final_answer": response.content
    }