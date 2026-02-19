from openai import OpenAI

class Generator:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = OpenAI()
        self.model = model

    def generate(self, query: str, context: str) -> str:
        prompt = f"""
You are a helpful assistant.
Answer the question ONLY using the provided context.
If the context does not contain the answer, say you do not know.

Context:
{context}

Question:
{query}

Answer:
""".strip()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )

        return response.choices[0].message.content.strip()
