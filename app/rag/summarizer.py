class Summarizer:
    def __init__(self, max_chars: int = 800):
        self.max_chars = max_chars

    def summarize(self, retrieved_chunks: list[dict]) -> str:
        seen = set()
        context_parts = []
        current_length = 0

        for chunk in retrieved_chunks:
            text = chunk["text"].strip()

            if text in seen:
                continue

            if current_length + len(text) > self.max_chars:
                break

            seen.add(text)
            context_parts.append(text)
            current_length += len(text)

        return "\n\n".join(context_parts)
