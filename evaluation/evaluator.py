def context_precision(retrieved_docs, keyword):

    relevant = 0

    for doc in retrieved_docs:
        if keyword.lower() in doc.lower():
            relevant += 1

    return relevant / len(retrieved_docs)


if __name__ == "__main__":

    docs = [
        "RAG combines retrieval and generation.",
        "Cats are cute animals.",
        "RAG improves answer quality."
    ]

    score = context_precision(
        docs,
        "RAG"
    )

    print(score)