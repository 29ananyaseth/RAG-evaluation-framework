from embeddings.embedder import EmbeddingModel
from vector_store.vector_store import VectorStore


chunks = [
    "RAG combines retrieval and generation.",
    "Vector databases store embeddings.",
    "Large language models generate answers."
]

embedder = EmbeddingModel()

embeddings = embedder.embed_documents(chunks)

vector_store = VectorStore()

vector_store.reset_collection()
vector_store.add_documents(
    chunks,
    embeddings
)

query = "What is RAG?"

query_embedding = embedder.embed_query(query)

results = vector_store.search(
    query_embedding,
    top_k=2
)

print("\nRetrieved Documents:\n")

for doc in results:
    print(doc)