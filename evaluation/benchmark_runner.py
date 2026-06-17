from evaluation.benchmark_loader import load_benchmark
from evaluation.similarity_evaluator import SimilarityEvaluator
from evaluation.experiment_tracker import ExperimentTracker
from retrieval.retriever import Retriever
from generation.generator import Generator


def run_benchmark():

    benchmark_data = load_benchmark(
        "data/benchmark_questions.json"
    )

    retriever = Retriever()

    generator = Generator()

    evaluator = SimilarityEvaluator()

    scores = []

    for idx, item in enumerate(benchmark_data, start=1):

        question = item["question"]
        ground_truth = item["ground_truth"]

        retrieved_docs = retriever.retrieve(
            question,
            top_k=3
        )

        context = "\n".join(retrieved_docs)

        generated_answer = generator.generate(
            question,
            context
        )

        score = evaluator.evaluate(
            generated_answer,
            ground_truth
        )

        scores.append(score)

        print(f"\nQuestion {idx}")
        print("-" * 50)
        print("Question:", question)
        print("Generated:", generated_answer[:150])
        print("Ground Truth:", ground_truth)
        print(f"Score: {score:.4f}")

        average_score = sum(scores) / len(scores)

        tracker = ExperimentTracker()

        tracker.save_run(
            average_score=average_score,
            scores=scores,
            chunk_size=500,
            embedding_model="bge-small"
)

        print("\n" + "=" * 50)
        print(f"Average Score: {average_score:.4f}")
        print("=" * 50)
    


if __name__ == "__main__":
    run_benchmark()