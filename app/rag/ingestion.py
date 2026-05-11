from rag.chunking import chunk_text
from rag.embeddings import get_embedding
from rag.vector_store import add_embedding

def ingest_document(text):

    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = get_embedding(chunk)
        add_embedding(embedding, chunk)