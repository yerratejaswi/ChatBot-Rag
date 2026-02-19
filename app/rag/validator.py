class Validator:
    def __init__(
        self,
        min_score: float = 0.25,  # cosine similarity threshold
        min_context_chars: int = 100
    ):
        self.min_score = min_score
        self.min_context_chars = min_context_chars

    def validate(self, retrieved_chunks: list[dict], context: str) -> bool:
        if not retrieved_chunks:
            return False

        best_score = retrieved_chunks[0]["score"]

        # Require minimum similarity
        if best_score < self.min_score:
            return False

        if len(context.strip()) < self.min_context_chars:
            return False

        return True
