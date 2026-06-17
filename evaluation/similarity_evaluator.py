from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class SimilarityEvaluator:

    def __init__(self):

        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def evaluate(self,
                 generated_answer,
                 ground_truth):

        embeddings = self.model.encode(
            [generated_answer, ground_truth]
        )

        similarity = cosine_similarity(
            [embeddings[0]],
            [embeddings[1]]
        )[0][0]

        return float(similarity)


if __name__ == "__main__":

    evaluator = SimilarityEvaluator()

    generated = (
        "RAG combines retrieval systems "
        "with language models."
    )

    ground_truth = (
        "Retrieval-Augmented Generation "
        "combines retrieval systems "
        "with language models."
    )

    score = evaluator.evaluate(
        generated,
        ground_truth
    )

    print(
        f"Similarity Score: {score:.4f}"
    )