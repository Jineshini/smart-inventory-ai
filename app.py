import streamlit as st

st.set_page_config(
    page_title="Smart Inventory AI Assistant",
    page_icon="📦"
)

st.title("📦 Smart Inventory AI Assistant")

st.write("Agentic AI Inventory Assistant is running!")

question = st.text_input("Ask your inventory question:")

if st.button("Submit"):
    if question:
        st.success(f"Your question: {question}")
    else:
        st.warning("Please enter a question.")