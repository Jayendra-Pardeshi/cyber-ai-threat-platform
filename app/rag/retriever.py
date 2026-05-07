from app.rag.vector_store import vector_db

def retrieve_context(query):

    docs = vector_db.similarity_search(query, k=5)

    return docs