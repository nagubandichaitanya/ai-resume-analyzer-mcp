from pathlib import Path
import fitz
from docx import Document

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".txt"}

def extract_text_from_pdf(path: Path) -> str:
    parts = []
    with fitz.open(path) as document:
        for page in document:
            parts.append(page.get_text())
    return "\n".join(parts).strip()

def extract_text_from_docx(path: Path) -> str:
    document = Document(path)
    return "\n".join(p.text for p in document.paragraphs if p.text.strip()).strip()

def extract_text_from_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").strip()

def extract_text(path: str | Path) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    extension = file_path.suffix.lower()
    if extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif extension == ".docx":
        text = extract_text_from_docx(file_path)
    elif extension == ".txt":
        text = extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Unsupported file type '{extension}'. Supported: {sorted(SUPPORTED_EXTENSIONS)}")
    if not text:
        raise ValueError("No readable text was found in the document.")
    return text
