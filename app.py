import streamlit as st

st.set_page_config(
    page_title="Smart Inventory AI Assistant",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Smart Inventory AI Assistant")

st.markdown(
    """
    Welcome to Smart Inventory AI Assistant.
    
    This system helps users find inventory-related information using Agentic AI and RAG.
    """
)

question = st.text_input(
    "Enter your inventory question:"
)

if st.button("Ask Assistant"):

    if question:
        st.info("Processing your question...")
        
        st.success(
            f"Your question: {question}"
        )

    else:
        st.warning(
            "Please enter a question."
        )