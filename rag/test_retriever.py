from retriever import search_documents

query = "What is inventory management?"

results = search_documents(query)

print("Retrieved Chunks:", len(results))

for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("-" * 40)
    print(doc.page_content[:500])