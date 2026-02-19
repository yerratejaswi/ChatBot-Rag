from app.rag.pipeline import RAGPipeline

def main():
    pipeline = RAGPipeline()

    query = "Explain tejaswi work experience in detail."
    response = pipeline.run(query)

    print(f"\nQuery type: {response['query_type']}\n")
    print("ANSWER:\n")
    print(response["answer"])
    print("\n===============================\n")

if __name__ == "__main__":
    main()
