class InventoryExpertAgent:

    def generate_answer(self, query, context):

        answer = f"""
Question:
{query}

Answer:

Based on the retrieved inventory documents,

{context[:1000]}

This answer is generated using the inventory knowledge base.
"""

        return {
            "query": query,
            "answer": answer,
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