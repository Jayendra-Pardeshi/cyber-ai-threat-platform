from app.services.llm_service import llm

def risk_analysis(context):

    prompt = f'''
    Analyze cybersecurity severity.

    Context:
    {context}

    Return:
    - severity
    - risk level
    - remediation
    '''

    response = llm.invoke(prompt)

    return response.content