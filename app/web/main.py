from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

import fitz  # PyMuPDF

from app.rag.pipeline import RAGPipeline

app = FastAPI()
templates = Jinja2Templates(directory="app/web/templates")

# Single in-memory pipeline (session scoped)
pipeline = RAGPipeline()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/upload")
async def upload(files: list[UploadFile] = File(...)):
    """
    Upload documents for the current session only (in-memory).
    Supported formats:
      - .txt
      - .pdf (extracted via PyMuPDF/fitz)
    """
    texts: list[str] = []

    for file in files:
        content = await file.read()
        filename = (file.filename or "").lower()

        # TXT files
        if filename.endswith(".txt"):
            text = content.decode("utf-8", errors="ignore").strip()
            if text:
                print("TXT:", file.filename, "chars:", len(text))
                print("TXT preview:\n", text[:800])
                texts.append(text)

        # PDF files (PyMuPDF)
        elif filename.endswith(".pdf"):
            try:
                doc = fitz.open(stream=content, filetype="pdf")
                pdf_text_parts = []
                for page in doc:
                    page_text = page.get_text("text")
                    if page_text:
                        pdf_text_parts.append(page_text)

                joined = "\n".join(pdf_text_parts).strip()

                print("PDF:", file.filename, "chars:", len(joined))
                print("PDF preview:\n", joined[:800])

                if joined:
                    texts.append(joined)

            except Exception as e:
                print(f"PDF extraction failed for {file.filename}: {e}")

        else:
            print("Unsupported file type:", file.filename)

    if not texts:
        return JSONResponse({
            "status": "No supported documents uploaded (only .txt and .pdf allowed)"
        })

    # Ingest documents into memory (session-only)
    pipeline.ingest_documents(texts)

    return JSONResponse({
        "status": f"{len(texts)} document(s) uploaded and indexed for this session"
    })


@app.post("/chat")
def chat(payload: dict):
    query = payload.get("query", "").strip()

    if not query:
        return JSONResponse({"answer": "Please enter a question."})

    try:
        result = pipeline.run(query)
    except RuntimeError as e:
        return JSONResponse({"answer": str(e)})
    except Exception as e:
        # safer: return readable error rather than 500
        return JSONResponse({"answer": f"Server error: {e}"})

    return JSONResponse({
        "query_type": result["query_type"],
        "answer": result["answer"] or "No answer generated.",
        "context": result["context"]
    })
