import json


def load_benchmark(path):

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


if __name__ == "__main__":

    benchmarks = load_benchmark(
        "data/benchmark_questions.json"
    )

    print(f"Total Questions: {len(benchmarks)}")

    print("\nFirst Question:\n")

    print(benchmarks[0])