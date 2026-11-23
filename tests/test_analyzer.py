from services.analyzer import analyze_resume, compare_resume_to_job, extract_skills
RESUME = """BTech Computer Science graduate. Python, FastAPI, PostgreSQL, SQL, Git and REST API development. Built an AI document assistant using RAG and LLM technologies."""
JOB = """Looking for a Python developer with FastAPI, PostgreSQL, SQL, Docker, AWS and REST API experience."""

def test_extract_skills():
    result = extract_skills(RESUME)
    assert "python" in result and "fastapi" in result and "postgresql" in result and "rag" in result

def test_analyze_resume():
    assert analyze_resume(RESUME).skill_count >= 4

def test_compare_resume_to_job():
    result = compare_resume_to_job(RESUME, JOB)
    assert 0 <= result.match_score <= 100
    assert "python" in result.matched_skills
    assert "docker" in result.missing_skills and "aws" in result.missing_skills
