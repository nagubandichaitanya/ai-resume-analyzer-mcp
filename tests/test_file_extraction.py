from pathlib import Path
from services.text_extractor import extract_text

def test_txt_extraction(tmp_path: Path):
    path = tmp_path / "resume.txt"
    path.write_text("Python developer with FastAPI and PostgreSQL.", encoding="utf-8")
    text = extract_text(path)
    assert "Python developer" in text and "FastAPI" in text
