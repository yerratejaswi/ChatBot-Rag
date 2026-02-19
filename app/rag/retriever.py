import faiss
import numpy as np
from app.ingest.embedder import embed_texts


class Retriever:
    def __init__(self):
        self.index = None
        self.chunks: list[str] = []

    def ingest(self, chunks: list[str], embeddings):
        """
        Build in-memory FAISS index using cosine similarity
        """
        embeddings = np.array(embeddings).astype("float32")

        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)

        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatIP(dim)  # Inner product index
        self.index.add(embeddings)

        self.chunks = chunks

    def retrieve(self, query: str, top_k: int):
        if self.index is None or not self.chunks:
            return []

        query_embedding = embed_texts([query])
        query_embedding = np.array(query_embedding).astype("float32")

        # Normalize query
        faiss.normalize_L2(query_embedding)

        scores, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx, score in zip(indices[0], scores[0]):
            if idx == -1:
                continue

            results.append({
                "text": self.chunks[idx],
                "score": float(score)
            })

        return results
