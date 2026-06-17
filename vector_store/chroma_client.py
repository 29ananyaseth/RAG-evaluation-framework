import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="rag_documents"
)

documents = [
    "RAG combines retrieval and generation.",
    "Vector databases store embeddings.",
    "Large language models generate answers."
]

ids = ["doc1", "doc2", "doc3"]

collection.add(
    documents=documents,
    ids=ids
)

results = collection.query(
    query_texts=["What is RAG?"],
    n_results=2
)


print(results["documents"])