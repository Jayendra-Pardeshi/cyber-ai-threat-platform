import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents = []

def add_embedding(embedding, text):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    documents.append(text)

def search(query_embedding, k=5):
    vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(vector, k)

    results = []

    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results