from langchain_groq import ChatGroq
from config.settings import settings

llm = ChatGroq(
    groq_api_key=settings.GROQ_API_KEY,
    model_name="llama3-70b-8192"
)

def generate_response(prompt: str):
    response = llm.invoke(prompt)
    return response.content