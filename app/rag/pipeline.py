from app.rag.planner import Planner
from app.rag.retriever import Retriever
from app.rag.summarizer import Summarizer
from app.rag.validator import Validator
from app.rag.generator import Generator

from app.ingest.chunker import chunk_text
from app.ingest.embedder import embed_texts


class RAGPipeline:
    def __init__(self):
        self.planner = Planner()
        self.retriever = Retriever()
        self.summarizer = Summarizer()
        self.validator = Validator()
        self.generator = Generator()

    def ingest_documents(self, texts: list[str]):
        chunks = []
        for text in texts:
            chunks.extend(chunk_text(text))

        if not chunks:
            raise RuntimeError("No valid text chunks found.")

        embeddings = embed_texts(chunks)
        self.retriever.ingest(chunks, embeddings)

    def run(self, query: str):
        plan = self.planner.plan(query)

        retrieved_chunks = self.retriever.retrieve(
            query=query,
            top_k=plan["top_k"]
        ) or []

        context = self.summarizer.summarize(retrieved_chunks)

        is_valid = self.validator.validate(retrieved_chunks, context)

        if not is_valid:
            return {
                "query_type": plan["type"].value,
                "answer": "I don’t have enough reliable information to answer that.",
                "context": ""
            }

        answer = self.generator.generate(query, context)

        return {
            "query_type": plan["type"].value,
            "answer": answer,
            "context": context
        }
