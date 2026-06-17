import json
import os
from datetime import datetime


class ExperimentTracker:

    def __init__(self):

        self.results_dir = "experiments"

        os.makedirs(
            self.results_dir,
            exist_ok=True
        )

    def save_run(
        self,
        average_score,
        scores,
        chunk_size,
        embedding_model
    ):

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        result = {
            "timestamp": timestamp,
            "chunk_size": chunk_size,
            "embedding_model": embedding_model,
            "average_score": average_score,
            "scores": scores
        }

        filename = (
            f"{self.results_dir}/"
            f"run_{timestamp}.json"
        )

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                result,
                file,
                indent=4
            )

        print(
            f"\nResults saved to: {filename}"
        )


# ADD THIS PART AT THE VERY END OF THE FILE

if __name__ == "__main__":

    tracker = ExperimentTracker()

    tracker.save_run(
        average_score=0.7789,
        scores=[
            0.8235,
            0.8305,
            0.6608,
            0.8482,
            0.7315
        ],
        chunk_size=500,
        embedding_model="bge-small"
    )