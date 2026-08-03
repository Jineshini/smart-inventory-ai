import streamlit as st
from graph.workflow_graph import run_langgraph

st.set_page_config(
    page_title="Smart Inventory AI Assistant",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Smart Inventory AI Assistant")

st.markdown("""
Welcome to Smart Inventory AI Assistant.

This system uses Agentic AI, RAG, LangGraph and Groq LLM to answer inventory-related questions.
""")

question = st.text_input("Enter your inventory question:")

if st.button("Ask Assistant"):

    if question:

        with st.spinner("Generating answer..."):

            answer = run_langgraph(question)

        st.success("Answer")

        st.write(answer)

    else:

        st.warning("Please enter a question.")