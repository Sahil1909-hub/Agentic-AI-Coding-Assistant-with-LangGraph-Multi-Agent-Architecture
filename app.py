import streamlit as st
from graph.workflow import graph
from utils.logger import logger
from langchain_core.messages import HumanMessage
import uuid


st.set_page_config(
    page_title="AI Coding Assistant",
    layout="wide"
)

if "thread_id" not in st.session_state:

    st.session_state.thread_id = str(
        uuid.uuid4()
    )


st.title("🤖 Agentic AI Coding Assistant")

logger.info("App creation started..")

query = st.text_area(
    "Describe what you want to build or ask a question"
)

if st.button("Generate"):

    if not query.strip():

        st.warning(
            "Please enter a query."
        )

        st.stop()

    with st.spinner("Agents are working..."):

        result = graph.invoke(
            {
                "query": query,
                "messages": [
                    HumanMessage(
                        content=query
                    )
                ]
            },
            config={
                "configurable": {
                    "thread_id": st.session_state.thread_id
                }
            }
        )

        # -----------------------------
        # CHAT / WEB SEARCH / GITHUB
        # -----------------------------

        if "final_answer" in result:

            st.subheader("💬 Response")

            st.write(
                result["final_answer"]
            )

        # -----------------------------
        # CODING PIPELINE
        # -----------------------------

        else:

            if result.get("plan"):

                st.subheader("📋 Project Plan")

                st.write(
                    result["plan"]
                )

            if result.get("research"):

                st.subheader("🔍 Research")

                st.write(
                    result["research"]
                )

            if result.get("code"):

                st.subheader("💻 Generated Code")

                st.code(
                    result["code"],
                    language="python"
                )

            if result.get("review"):

                st.subheader("📝 Review")

                st.write(
                    result["review"]
                )

            if result.get("tests"):

                st.subheader("🧪 Tests")

                st.code(
                    result["tests"],
                    language="python"
                )

            if result.get("documentation"):

                st.subheader("📚 Documentation")

                st.markdown(
                    result["documentation"]
                )

logger.info("App created..")