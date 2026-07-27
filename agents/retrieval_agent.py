import os
import sys

# rag folder path add pannudhu
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "rag"))

from retriever import search_documents


class RetrievalAgent:

    def retrieve(self, query):

        results = search_documents(query)

        context = ""

        for doc in results:
            context += doc.page_content + "\n\n"

        return {
            "query": query,
            "context": context,
            "next_agent": "inventory_expert_agent"
        }


if __name__ == "__main__":

    agent = RetrievalAgent()

    result = agent.retrieve("What is inventory management?")

    print(result["context"][:800])