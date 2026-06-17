from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed_documents(self, chunks):
        return self.model.encode(
            chunks,
            convert_to_numpy=True
        )

    def embed_query(self, query):
        return self.model.encode(
            query,
            convert_to_numpy=True
        )


if __name__ == "__main__":

    chunks = [
        "RAG combines retrieval and generation.",
        "Vector databases store embeddings.",
        "Large language models generate answers."
    ]

    embedder = EmbeddingModel()

    embeddings = embedder.embed_documents(chunks)

    print("Embedding Shape:")
    print(embeddings.shape)