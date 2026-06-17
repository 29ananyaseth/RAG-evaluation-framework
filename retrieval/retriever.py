import chromadb


class Retriever:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="rag_documents"
        )

    def retrieve(self, query, top_k=3):

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k
        )

        return results["documents"][0]


if __name__ == "__main__":

    retriever = Retriever()

    docs = retriever.retrieve(
        "What is RAG?"
    )

    print("\nRetrieved Documents:\n")

    for idx, doc in enumerate(docs, start=1):
        print(f"{idx}. {doc}")