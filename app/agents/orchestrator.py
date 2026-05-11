from agents.planner_agent import planner_agent
from rag.retriever import retrieve_context
from services.llm_service import generate_response

def run_orchestrator(query):

    plan = planner_agent(query)

    context = retrieve_context(query)

    final_prompt = f"""
    Security Plan:
    {plan}

    Retrieved Context:
    {context}

    Generate final cybersecurity intelligence report.
    """

    return generate_response(final_prompt)