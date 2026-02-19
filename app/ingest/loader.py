from pathlib import Path
import fitz  # PyMuPDF


def load_documents(doc_dir: str) -> list[str]:
    """
    Load .txt and .pdf documents from a directory.
    Used for offline ingestion (CLI use).
    """
    texts: list[str] = []

    doc_path = Path(doc_dir)

    if not doc_path.exists():
        raise ValueError(f"Directory does not exist: {doc_dir}")

    for file in doc_path.iterdir():

        # -----------------
        # TXT Files
        # -----------------
        if file.suffix.lower() == ".txt":
            try:
                with open(file, "r", encoding="utf-8") as f:
                    text = f.read().strip()
                    if text:
                        texts.append(text)
            except Exception as e:
                print(f"Failed to read TXT file {file.name}: {e}")

        # -----------------
        # PDF Files
        # -----------------
        elif file.suffix.lower() == ".pdf":
            try:
                with fitz.open(file) as doc:
                    pdf_text_parts = []
                    for page in doc:
                        page_text = page.get_text("text")
                        if page_text:
                            pdf_text_parts.append(page_text)

                joined = "\n".join(pdf_text_parts).strip()
                if joined:
                    texts.append(joined)

            except Exception as e:
                print(f"Failed to extract PDF {file.name}: {e}")

    return texts
