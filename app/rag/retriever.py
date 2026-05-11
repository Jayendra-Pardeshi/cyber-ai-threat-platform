from rag.embeddings import get_embedding
from rag.vector_store import search

def retrieve_context(query):

    embedding = get_embedding(query)

    return search(embedding)