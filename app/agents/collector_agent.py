from app.services.llm_service import llm

def collect_threats(logs):

    prompt = f'''
    Analyze cybersecurity logs.

    Detect:
    - suspicious activity
    - attack type
    - malicious indicators

    Logs:
    {logs}
    '''

    response = llm.invoke(prompt)

    return response.content