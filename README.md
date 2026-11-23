# AI Resume Analyzer using MCP

Complete portfolio project combining Model Context Protocol, resume parsing, NLP skill extraction, TF-IDF matching, FastAPI and automated tests.

## Features
- PDF/DOCX/TXT resume parsing
- Technical skill extraction
- Job-description skill extraction
- Skill coverage calculation
- TF-IDF cosine similarity
- Combined match score
- Missing skills and recommendations
- FastAPI REST API and Swagger UI
- MCP tools, resource and prompt
- Automated tests

## Architecture
```text
User/LLM -> MCP Server -> Analyzer -> Parser/NLP -> Structured report
                         \-> FastAPI -> JSON API
```

## Setup
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

## Test
```powershell
pytest -q
```

## FastAPI
```powershell
uvicorn api:app --reload
```
Open `http://127.0.0.1:8000/docs`.

## MCP Inspector
```powershell
mcp dev mcp_server.py
```
If needed:
```powershell
python -m mcp dev mcp_server.py
```

## MCP tools
- `extract_resume_text(file_path)`
- `extract_skills(resume_text)`
- `compare_resume_to_job(resume_text, job_description)`
- `generate_resume_report(resume_text, job_description)`

Resource: `resume://supported-formats`

Prompt: `resume_analysis_prompt(job_title)`

## Example API request
```json
{
  "resume_text": "Python developer with FastAPI, PostgreSQL, SQL and Git.",
  "job_description": "Python developer with FastAPI, PostgreSQL, SQL, Docker and AWS."
}
```

## Security
This is a local portfolio project. In production, restrict arbitrary file paths, validate uploads, add authentication/authorization, scan files, enforce size limits, audit tool calls, and avoid sending resume PII to external LLMs without appropriate consent.

## Resume entry
**AI Resume Analyzer using MCP** — `Python | MCP | FastAPI | NLP | TF-IDF | Scikit-learn | PyMuPDF | python-docx`
- Developed an MCP-based AI resume analyzer exposing resume parsing, skill extraction, job-description matching and report generation as structured AI tools.
- Implemented PDF/DOCX text extraction and normalized resume content for NLP processing.
- Built technical-skill matching using a curated taxonomy and TF-IDF cosine similarity.
- Developed FastAPI endpoints for file uploads, resume analysis, job matching and structured JSON reports.
- Added automated tests covering analysis logic, API endpoints and document extraction.
