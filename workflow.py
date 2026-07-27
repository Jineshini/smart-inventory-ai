from agents.planner_agent import PlannerAgent
from agents.retrieval_agent import RetrievalAgent
from agents.inventory_expert_agent import InventoryExpertAgent
from agents.reflection_agent import ReflectionAgent


def run_workflow(user_query):

    planner = PlannerAgent()
    retrieval = RetrievalAgent()
    expert = InventoryExpertAgent()
    reflection = ReflectionAgent()

    # Planner Agent
    plan = planner.plan(user_query)

    print("\n--- Planner Output ---")
    print(plan)

    # Retrieval Agent
    retrieved = retrieval.retrieve(plan["query"])

    print("\n--- Retrieved Context ---")
    print(retrieved)

    # Inventory Expert Agent
    answer = expert.generate_answer(
        retrieved["query"],
        retrieved["context"]
    )

    print("\n--- Expert Answer ---")
    print(answer)

    # Reflection Agent
    final_answer = reflection.review(answer["answer"])

    return final_answer


if __name__ == "__main__":

    query = input("Ask a question: ")

    result = run_workflow(query)

    print("\n========== FINAL ANSWER ==========\n")

    print(result)