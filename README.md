# ChatBot-Rag
Perfect Teja 😎
Here’s a **clean, professional, resume-grade README.md** for your RAG project.

You can copy-paste this directly into a file named:

```bash
README.md
```

---

# 📄 `README.md`

```markdown
# ChatBot-RAG 🚀

A modular Retrieval-Augmented Generation (RAG) chatbot built using:

- FastAPI
- FAISS (vector search)
- SentenceTransformers (MiniLM embeddings)
- OpenAI (LLM generation)
- Modular pipeline architecture

This project demonstrates a production-style RAG system with clean separation of responsibilities across ingestion, retrieval, validation, summarization, and generation stages.

---

## 🧠 Architecture Overview

The pipeline follows this flow:

Planner  
→ Retriever (FAISS cosine similarity search)  
→ Summarizer (context compression)  
→ Validator (confidence filtering)  
→ Generator (LLM answer synthesis)

```

User Query
↓
Planner (detect type + top_k)
↓
Retriever (vector search)
↓
Summarizer (build context)
↓
Validator (confidence + threshold check)
↓
OpenAI Generator
↓
Final Answer

```

---

## 📂 Project Structure

```

app/
│
├── ingest/
│   ├── chunker.py
│   ├── embedder.py
│   └── loader.py
│
├── rag/
│   ├── planner.py
│   ├── retriever.py
│   ├── summarizer.py
│   ├── validator.py
│   ├── generator.py
│   └── pipeline.py
│
└── web/
└── main.py

````

---

## 🔥 Features

- Sentence-based chunking
- MiniLM embeddings
- FAISS cosine similarity vector search
- Confidence-based validation layer
- Context size control
- Modular RAG pipeline
- PDF + TXT ingestion
- Session-scoped in-memory indexing

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yerratejaswi/ChatBot-Rag.git
cd ChatBot-Rag
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file exists yet:

```bash
pip install fastapi uvicorn sentence-transformers faiss-cpu openai pymupdf numpy
```

---

## 🔑 Set OpenAI API Key

Windows (PowerShell):

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Mac/Linux:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Restart terminal after setting.

---

## 🚀 Run Application

```bash
uvicorn app.web.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000
```

---

## 📄 Upload Documents

Supported formats:

* `.txt`
* `.pdf`

Documents are indexed in-memory for the current session.

---

## 🧪 Example Query

```
Explain the main idea discussed in the document.
```

---

## 🏗 Technical Design Decisions

### Why Cosine Similarity?

MiniLM embeddings perform best using normalized vectors and cosine similarity.
FAISS `IndexFlatIP` with L2 normalization is used for optimal semantic retrieval.

### Why Validator Layer?

Prevents hallucinations by:

* Enforcing minimum similarity threshold
* Requiring sufficient context length

### Why Modular Architecture?

Improves:

* Testability
* Maintainability
* Extensibility (e.g., adding rerankers or hybrid search)

---

## 📈 Future Improvements

* Persistent FAISS index
* Hybrid BM25 + vector search
* Streaming LLM responses
* Multi-user session isolation
* Docker containerization
* Deployment to AWS / Azure

---

## 👨‍💻 Author

Tejaswi Yerra
Software Engineer | AI Systems | Cloud & Distributed Architectures

---

## ⭐ If You Like This Project

Give it a star and feel free to fork!



