import faiss
import numpy as np
import json

from app.ingest.loader import load_documents
from app.ingest.chunker import chunk_text
from app.ingest.embedder import embed_texts

DOC_PATH = "data/docs"
INDEX_PATH = "data/faiss.index"

def main():
    documents = load_documents(DOC_PATH)
    # chunk all documents
    chunks = []
    for doc in documents:
        chunks.extend(chunk_text(doc))
    # embed all chunks
    embeddings = embed_texts(chunks)
    embeddings = np.array(embeddings).astype("float32")
    
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    # save the index to disk
    faiss.write_index(index, INDEX_PATH)


    # save chunks to a json file for later retrieval
    with open("data/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f)

    print(f"Indexed {len(chunks)} chunks")
    print("FAISS index saved successfully")
    print("Chunks metadata saved")

if __name__ == "__main__":
    main()
