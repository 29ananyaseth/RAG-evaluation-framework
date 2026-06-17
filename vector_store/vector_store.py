import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="rag_documents"
        )
    def add_documents(self, chunks, embeddings):
        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        self.collection.add(
            documents=chunks,
            embeddings=embeddings.tolist(),
            ids=ids

        )
            
    def search(self, query_embedding, top_k=3):

        results = self.collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=top_k
        )

        return results["documents"][0]
    
    def reset_collection(self):
        self.client.delete_collection(
        name="rag_documents"
        )

        self.collection = self.client.get_or_create_collection(
        name="rag_documents"
       )