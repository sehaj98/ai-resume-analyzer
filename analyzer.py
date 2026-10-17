import re
from pypdf import PdfReader


SKILLS_LIST = [
    "python",
    "java",
    "c++",
    "sql",
    "flask",
    "django",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "github",
    "machine learning",
    "data analysis",
    "excel",
    "power bi",
    "aws",
    "docker",
    "communication",
    "teamwork",
]


def extract_text_from_pdf(file_path):
    """Extract text from an uploaded PDF resume."""
    reader = PdfReader(file_path)

    pages_text = []

    for page in reader.pages:
        pages_text.append(page.extract_text() or "")

    return "\n".join(pages_text).strip()


def extract_skills(text):
    """Find known skills in resume text or a job description."""
    text = text.lower()
    found_skills = []

    for skill in SKILLS_LIST:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            if skill == "c++":
                display_skill = "C++"
            else:
                display_skill = skill.title()

            found_skills.append(display_skill)

    return sorted(set(found_skills))


def analyze_resume(resume_text, job_description):
    """Compare resume skills with the job requirements."""
    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    resume_skill_set = {skill.lower() for skill in resume_skills}

    matched_skills = [
        skill for skill in required_skills
        if skill.lower() in resume_skill_set
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill.lower() not in resume_skill_set
    ]

    if required_skills:
        match_percentage = round(
            len(matched_skills) / len(required_skills) * 100
        )
    else:
        match_percentage = 0

    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": match_percentage,
    }