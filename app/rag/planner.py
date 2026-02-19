from enum import Enum


class QueryType(Enum):
    FACTUAL = "factual"
    EXPLANATION = "explanation"
    SUMMARY = "summary"


class Planner:
    def plan(self, query: str):
        query_lower = query.lower()

        if any(word in query_lower for word in ["summarize", "summary", "overview", "brief"]):
            return {"type": QueryType.SUMMARY, "top_k": 5}

        if any(word in query_lower for word in ["explain", "how", "why", "describe"]):
            return {"type": QueryType.EXPLANATION, "top_k": 3}

        return {"type": QueryType.FACTUAL, "top_k": 2}
