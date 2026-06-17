from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class Generator:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        self.model = "llama-3.1-8b-instant"

    def generate(self, query, context):

        prompt = f"""
        Answer the question using ONLY the provided context.

        Context:
        {context}

        Question:
        {query}
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content


if __name__ == "__main__":

    generator = Generator()

    context = """
    Retrieval-Augmented Generation (RAG) combines retrieval systems
    with large language models.
    """

    answer = generator.generate(
        "What is RAG?",
        context
    )

    print(answer)