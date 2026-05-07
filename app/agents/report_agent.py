from app.services.llm_service import llm

def generate_report(data):

    prompt = f'''
    Generate professional incident report.

    Data:
    {data}
    '''

    response = llm.invoke(prompt)

    return response.content