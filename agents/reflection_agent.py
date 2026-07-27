class ReflectionAgent:

    def review(self, answer):

        improved_answer = answer.strip()

        improved_answer += "\n\n[Reviewed by Reflection Agent]"

        return improved_answer


if __name__ == "__main__":

    sample_answer = """
Inventory management helps maintain optimal stock levels.
"""

    agent = ReflectionAgent()

    final_answer = agent.review(sample_answer)

    print(final_answer)