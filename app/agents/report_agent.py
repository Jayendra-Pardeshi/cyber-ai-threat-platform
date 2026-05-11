from app.services.llm_service import llm


def generate_report(analysis: str):
    prompt = f"""
    Generate professional cybersecurity incident report.

    Analysis:
    {analysis}
    """

    response = llm.invoke(prompt)

    return response.content