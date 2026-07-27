import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from agents.planner_agent import PlannerAgent
from agents.retrieval_agent import RetrievalAgent
from agents.inventory_expert_agent import InventoryExpertAgent
from agents.reflection_agent import ReflectionAgent



# State definition
class AgentState(TypedDict):

    query: str
    plan: dict
    retrieved: dict
    answer: dict
    final_answer: str



# Initialize agents

planner = PlannerAgent()
retrieval = RetrievalAgent()
expert = InventoryExpertAgent()
reflection = ReflectionAgent()



# Node 1 - Planner

def planner_node(state: AgentState):

    plan = planner.plan(state["query"])

    return {
        "plan": plan
    }



# Node 2 - Retrieval

def retrieval_node(state: AgentState):

    retrieved = retrieval.retrieve(
        state["plan"]["query"]
    )

    return {
        "retrieved": retrieved
    }



# Node 3 - Expert

def expert_node(state: AgentState):

    answer = expert.generate_answer(
        state["retrieved"]["query"],
        state["retrieved"]["context"]
    )

    return {
        "answer": answer
    }



# Node 4 - Reflection

def reflection_node(state: AgentState):

    final = reflection.review(
        state["answer"]["answer"]
    )

    return {
        "final_answer": final
    }



# Build LangGraph

workflow = StateGraph(AgentState)


workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "retrieval",
    retrieval_node
)

workflow.add_node(
    "expert",
    expert_node
)

workflow.add_node(
    "reflection",
    reflection_node
)



# Connections

workflow.add_edge(
    START,
    "planner"
)

workflow.add_edge(
    "planner",
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "expert"
)

workflow.add_edge(
    "expert",
    "reflection"
)

workflow.add_edge(
    "reflection",
    END
)



# Compile

app = workflow.compile()



if __name__ == "__main__":

    query = input("Ask a question: ")

    result = app.invoke(
        {
            "query": query
        }
    )

    print("\n========== LANGGRAPH FINAL ANSWER ==========\n")

    print(result["final_answer"])