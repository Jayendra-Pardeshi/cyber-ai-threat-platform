from app.rag.retriever import retrieve_context

def retrieval_agent(query):

    docs = retrieve_context(query)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    return context