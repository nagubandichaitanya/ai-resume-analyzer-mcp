import json
from pathlib import Path
from fastapi import FastAPI, File, HTTPException, UploadFile
from config import APP_NAME, MAX_FILE_SIZE_BYTES
from models import CompareRequest, TextAnalyzeRequest
from services.analyzer import analyze_resume, compare_resume_to_job, generate_report
from services.file_store import save_upload
from services.text_extractor import extract_text

app = FastAPI(title=APP_NAME, version="1.0.0", description="Resume analysis API backed by reusable MCP tools.")

@app.get("/health")
def health():
    return {"status": "ok", "service": APP_NAME}

@app.post("/analyze/text")
def analyze_text(request: TextAnalyzeRequest):
    return analyze_resume(request.resume_text).model_dump()

@app.post("/compare")
def compare(request: CompareRequest):
    return compare_resume_to_job(request.resume_text, request.job_description).model_dump()

@app.post("/analyze/file")
async def analyze_file(resume: UploadFile = File(...)):
    content = await resume.read()
    if len(content) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(413, "Uploaded file is larger than the configured size limit.")
    if not resume.filename:
        raise HTTPException(400, "Filename is required.")
    try:
        path = save_upload(resume.filename, content)
        text = extract_text(path)
        return {"filename": Path(resume.filename).name, "text_preview": text[:500], **analyze_resume(text).model_dump()}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc
    except Exception as exc:
        raise HTTPException(500, f"Unable to process resume: {exc}") from exc

@app.post("/report")
def report(request: CompareRequest):
    return json.loads(generate_report(request.resume_text, request.job_description).model_dump_json())
