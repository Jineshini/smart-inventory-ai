import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
print(os.getenv("GROQ_API_KEY"))


class InventoryExpertAgent:

    def __init__(self):

        self.llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0.2,
            api_key=os.getenv("GROQ_API_KEY")
        )

    def generate_answer(self, query, context):

        prompt = f"""
You are an Inventory Management Expert.

Answer the user's question using ONLY the information provided in the context.

Context:
{context}

Question:
{query}

Provide a clear, accurate and well-structured answer.
"""

        response = self.llm.invoke(prompt)

        return {
            "query": query,
            "answer": response.content,
            "next_agent": "reflection_agent"
        }


if __name__ == "__main__":

    sample_context = """
Inventory management is a specialized branch of business management.
It helps organizations maintain optimum stock levels.
"""

    agent = InventoryExpertAgent()

    result = agent.generate_answer(
        "What is inventory management?",
        sample_context
    )

    print(result["answer"])