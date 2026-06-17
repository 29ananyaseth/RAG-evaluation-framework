from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(text)

    return chunks


if __name__ == "__main__":
    sample_text = """
    Retrieval-Augmented Generation (RAG) combines retrieval systems
    with large language models to improve answer quality.
    """ * 100

    chunks = chunk_text(sample_text)

    print(f"Total Chunks: {len(chunks)}")
    print("\nFirst Chunk:\n")
    print(chunks[0])