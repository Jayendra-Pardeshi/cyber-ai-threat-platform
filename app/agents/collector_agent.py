from app.services.llm_service import llm


def collect_threats(log_data: str):
    prompt = f"""
    Analyze the following security logs.
    Detect suspicious activities.

    Logs:
    {log_data}
    """

    response = llm.invoke(prompt)

    return response.content