from langchain_community.embeddings import OllamaEmbeddings

emb = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector = emb.embed_query(
    "customer support agent"
)

print(f"Embedding dimensions: {len(vector)}")
print(vector[:10])