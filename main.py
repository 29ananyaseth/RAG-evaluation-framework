from ingestion.loader import load_pdf
from chunking.chunker import chunk_text

import chromadb

from retrieval.retriever import Retriever
from generation.generator import Generator


PDF_PATH = "data/docs/sample.pdf"


def build_vector_store(chunks):

    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="rag_documents"
    )

    try:
        collection.delete(
            ids=[
                f"chunk_{i}"
                for i in range(len(chunks))
            ]
        )
    except:
        pass

    collection.add(
        documents=chunks,
        ids=[
            f"chunk_{i}"
            for i in range(len(chunks))
        ]
    )

    return collection


def main():

    print("Loading PDF...")

    text = load_pdf(PDF_PATH)

    print("Chunking document...")

    chunks = chunk_text(text)

    print(f"Total Chunks: {len(chunks)}")

    print("Building Vector Store...")

    build_vector_store(chunks)

    retriever = Retriever()

    generator = Generator()

    query = input("\nAsk a question: ")

    retrieved_docs = retriever.retrieve(
        query=query,
        top_k=3
    )

    context = "\n".join(retrieved_docs)

    answer = generator.generate(
        query=query,
        context=context
    )

    print("\nRetrieved Context:\n")
    print(context[:1000])

    print("\nAnswer:\n")
    print(answer)


if __name__ == "__main__":
    main()