import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models import ComparisonResult, ResumeReport, SkillAnalysis
from skill_taxonomy import SKILL_ALIASES

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()

def contains_skill(text: str, phrase: str) -> bool:
    normalized, phrase = normalize_text(text), normalize_text(phrase)
    if len(phrase) <= 2:
        return bool(re.search(rf"(?<![a-z0-9+#]){re.escape(phrase)}(?![a-z0-9+#])", normalized))
    return phrase in normalized

def extract_skills(text: str) -> list[str]:
    return sorted(skill for skill, aliases in SKILL_ALIASES.items() if any(contains_skill(text, alias) for alias in aliases))

def calculate_text_similarity(resume_text: str, job_description: str) -> float:
    matrix = TfidfVectorizer(stop_words="english", ngram_range=(1, 2)).fit_transform([normalize_text(resume_text), normalize_text(job_description)])
    return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]), 4)

def build_recommendations(resume_skills, job_skills, similarity):
    missing = sorted(set(job_skills) - set(resume_skills))
    recommendations = []
    if missing:
        recommendations.append("Consider adding evidence for these job skills if you genuinely have experience: " + ", ".join(missing[:10]) + ".")
    if similarity < 0.25:
        recommendations.append("The resume and job description have low textual similarity. Review terminology and make relevant experience more explicit.")
    elif similarity < 0.50:
        recommendations.append("The resume has moderate textual overlap. Add measurable project details and role-specific terminology where truthful.")
    else:
        recommendations.append("The resume has relatively strong textual overlap with the job description.")
    if not resume_skills:
        recommendations.append("No skills were detected. Add a clearly labeled technical skills section.")
    return recommendations

def compare_resume_to_job(resume_text: str, job_description: str) -> ComparisonResult:
    resume_skills, job_skills = extract_skills(resume_text), extract_skills(job_description)
    matched = sorted(set(resume_skills) & set(job_skills))
    missing = sorted(set(job_skills) - set(resume_skills))
    skill_score = len(matched) / len(job_skills) if job_skills else 0.0
    similarity = calculate_text_similarity(resume_text, job_description)
    score = round(min((skill_score * 70) + (similarity * 30), 100.0), 2)
    return ComparisonResult(match_score=score, matched_skills=matched, missing_skills=missing,
        resume_skills=resume_skills, job_skills=job_skills, text_similarity=similarity,
        recommendations=build_recommendations(resume_skills, job_skills, similarity))

def analyze_resume(resume_text: str) -> SkillAnalysis:
    skills = extract_skills(resume_text)
    return SkillAnalysis(skills=skills, skill_count=len(skills))

def generate_report(resume_text: str, job_description: str) -> ResumeReport:
    comparison = compare_resume_to_job(resume_text, job_description)
    return ResumeReport(**comparison.model_dump(), resume_word_count=len(resume_text.split()), job_word_count=len(job_description.split()))
