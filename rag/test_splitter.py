from document_loader import load_documents
from text_splitter import split_documents

documents = load_documents()

chunks = split_documents(documents)

print("Documents:", len(documents))
print("Chunks:", len(chunks))

if chunks:
    print("\nFirst Chunk:\n")
    print(chunks[0]["content"])