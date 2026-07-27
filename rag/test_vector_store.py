from document_loader import load_documents
from text_splitter import split_documents
from vector_store import create_vector_store

documents = load_documents()

chunks = split_documents(documents)

db = create_vector_store(chunks)

print("Vector Database Created Successfully!")

print("Total Chunks:", len(chunks))