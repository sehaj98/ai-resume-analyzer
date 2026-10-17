from analyzer import extract_skills, analyze_resume


def test_extract_skills():
    text = "I know Python, Flask, SQL and GitHub."
    skills = extract_skills(text)

    assert "Python" in skills
    assert "Flask" in skills
    assert "Sql" in skills
    assert "Github" in skills


def test_analyze_resume():
    resume = "I know Python and Flask."
    job = "Python, Flask and SQL required."

    result = analyze_resume(resume, job)

    assert result["match_percentage"] == 67
    assert "Sql" in result["missing_skills"]


def test_empty_job_description():
    result = analyze_resume("Python developer", "")

    assert result["match_percentage"] == 0
    assert result["missing_skills"] == []