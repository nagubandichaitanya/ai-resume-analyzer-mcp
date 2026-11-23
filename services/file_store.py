from pathlib import Path
import uuid
from config import UPLOAD_DIR, RESULT_DIR
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}

def save_upload(filename: str, content: bytes) -> Path:
    extension = Path(filename).suffix.lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type. Allowed: {sorted(ALLOWED_EXTENSIONS)}")
    destination = UPLOAD_DIR / f"{uuid.uuid4().hex}{extension}"
    destination.write_bytes(content)
    return destination

def save_json(filename: str, content: str) -> Path:
    destination = RESULT_DIR / filename
    destination.write_text(content, encoding="utf-8")
    return destination
