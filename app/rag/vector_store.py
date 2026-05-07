from langchain_community.vectorstores import Chroma
from app.rag.embeddings import embeddings

vector_db = Chroma(
    collection_name="cyber-threats",
    embedding_function=embeddings,
    persist_directory="vector_store"
)