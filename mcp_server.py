import json
from mcp.server import MCPServer
from services.analyzer import analyze_resume, compare_resume_to_job as compare_service, generate_report
from services.text_extractor import extract_text

mcp = MCPServer("AI Resume Analyzer", instructions="Analyze resumes against job descriptions using structured resume-analysis tools.")

@mcp.tool()
def extract_resume_text(file_path: str) -> str:
    """Extract readable text from a PDF, DOCX, or TXT resume."""
    return extract_text(file_path)

@mcp.tool()
def extract_skills(resume_text: str) -> dict:
    """Extract normalized technical skills from resume text."""
    return analyze_resume(resume_text).model_dump()

@mcp.tool()
def compare_resume_to_job(resume_text: str, job_description: str) -> dict:
    """Compare a resume with a job description using skill coverage and TF-IDF similarity."""
    return compare_service(resume_text, job_description).model_dump()

@mcp.tool()
def generate_resume_report(resume_text: str, job_description: str) -> str:
    """Generate a complete JSON resume-analysis report."""
    return json.dumps(generate_report(resume_text, job_description).model_dump(), indent=2)

@mcp.resource("resume://supported-formats")
def supported_formats() -> str:
    """List supported resume formats and analyzer capabilities."""
    return "Supported formats: PDF, DOCX, TXT. Capabilities: text extraction, skill extraction, TF-IDF similarity, skill matching, missing-skill detection, and recommendations."

@mcp.prompt()
def resume_analysis_prompt(job_title: str) -> str:
    """Create a reusable analysis prompt for a job title."""
    return f"Analyze the candidate resume for the {job_title} role. Identify relevant skills, missing requirements, textual overlap, and concrete improvements. Do not invent experience."

if __name__ == "__main__":
    mcp.run()
