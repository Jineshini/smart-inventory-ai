class PlannerAgent:

    def plan(self, user_query):

        return {
            "task": "inventory_question_answering",
            "query": user_query,
            "next_agent": "retrieval_agent"
        }


if __name__ == "__main__":

    planner = PlannerAgent()

    result = planner.plan("What is inventory management?")

    print(result)