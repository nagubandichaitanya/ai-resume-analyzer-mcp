from pydantic import BaseModel, Field

class TextAnalyzeRequest(BaseModel):
    resume_text: str = Field(min_length=20)

class CompareRequest(BaseModel):
    resume_text: str = Field(min_length=20)
    job_description: str = Field(min_length=20)

class SkillAnalysis(BaseModel):
    skills: list[str]
    skill_count: int

class ComparisonResult(BaseModel):
    match_score: float
    matched_skills: list[str]
    missing_skills: list[str]
    resume_skills: list[str]
    job_skills: list[str]
    text_similarity: float
    recommendations: list[str]

class ResumeReport(ComparisonResult):
    resume_word_count: int
    job_word_count: int
