from langchain_chroma import Chroma

from embeddings import get_embedding_model


def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    texts = [chunk["content"] for chunk in chunks]

    vector_db = Chroma.from_texts(
        texts=texts,
        embedding=embedding_model,
        persist_directory="chroma_db"
    )

    return vector_db