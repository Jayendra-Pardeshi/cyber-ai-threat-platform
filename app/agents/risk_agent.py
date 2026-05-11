from app.services.llm_service import llm


def risk_analysis(threat_context: str):
    prompt = f"""
    Analyze cybersecurity risk.

    Context:
    {threat_context}

    Return:
    - Severity
    - Attack Type
    - Recommendations
    """

    response = llm.invoke(prompt)

    return response.content