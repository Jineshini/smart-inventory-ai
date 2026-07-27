from embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query("What is inventory management?")

print("Embedding Length:", len(vector))
print("First 10 Values:")
print(vector[:10])