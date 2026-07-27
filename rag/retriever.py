from langchain_chroma import Chroma
from embeddings import get_embedding_model


def load_vector_store():

    embedding_model = get_embedding_model()

    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )

    return db


def search_documents(query, k=3):

    db = load_vector_store()

    results = db.similarity_search(query, k=k)

    return results