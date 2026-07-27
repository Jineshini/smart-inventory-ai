from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for doc in documents:

        split_text = splitter.split_text(doc["content"])

        for text in split_text:
            chunks.append({
                "filename": doc["filename"],
                "content": text
            })

    return chunks