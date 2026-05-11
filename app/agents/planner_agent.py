from services.llm_service import generate_response

def planner_agent(query):

    prompt = f"""
    You are a cybersecurity planner agent.

    User Query:
    {query}

    Create step-by-step security analysis plan.
    """

    return generate_response(prompt)