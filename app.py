import streamlit as st
from retrieval.retriever import Retriever
from generation.generator import Generator
import json
import os
import pandas as pd

st.set_page_config(
    page_title="RAG Evaluation Framework",
    layout="wide"
)

st.title("📚 RAG Evaluation Framework")
retriever = Retriever()
generator = Generator()
st.write(
    "Evaluate Retrieval-Augmented Generation Systems"
)

tab1, tab2, tab3 = st.tabs(
    [
        "Ask Questions",
        "Benchmark Results",
        "Experiments"
    ]
)

with tab1:

    st.header("Ask Questions")

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Submit"):

        retrieved_docs = retriever.retrieve(
        question,
        top_k=3
    )

        context = "\n".join(retrieved_docs)

        answer = generator.generate(
            question,
            context
    )

        st.subheader("Answer")
        st.write(answer)

        st.subheader("Retrieved Context")

        for idx, doc in enumerate(retrieved_docs, start=1):
            st.write(f"Chunk {idx}")
            st.info(doc)

with tab2:

    st.header("Benchmark Results")

    benchmark_scores = {
        "Question": [
            "Q1",
            "Q2",
            "Q3",
            "Q4",
            "Q5"
        ],
        "Score": [
            0.8235,
            0.8305,
            0.6608,
            0.8482,
            0.7315
        ]
    }

    df = pd.DataFrame(benchmark_scores)

    st.dataframe(
        df,
        use_container_width=True
    )

    avg_score = 0.7789

    st.metric(
        "Average Score",
        f"{avg_score:.4f}"
    )

with tab3:

    st.header("Experiment History")

    experiment_dir = "experiments"

    if os.path.exists(experiment_dir):

        files = sorted(
            os.listdir(experiment_dir),
            reverse=True
        )

        data = []

        for file in files:

            if file.endswith(".json"):

                filepath = os.path.join(
                    experiment_dir,
                    file
                )

                with open(
                    filepath,
                    "r",
                    encoding="utf-8"
                ) as f:

                    result = json.load(f)

                data.append(
                    {
                        "Timestamp":
                        result["timestamp"],

                        "Chunk Size":
                        result["chunk_size"],

                        "Embedding":
                        result["embedding_model"],

                        "Average Score":
                        result["average_score"]
                    }
                )

        if data:

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.info(
                "No experiment files found."
            )

    else:

        st.info(
            "Experiments folder not found."
        )
with st.sidebar:
    st.title("Settings")

    chunk_size = st.selectbox(
        "Chunk Size",
        [200, 500, 800, 1000],
        index=1
    )
st.line_chart(df["Average Score"])