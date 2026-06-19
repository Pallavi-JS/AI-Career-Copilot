skills_db = [
    "python",
    "java",
    "sql",
    "react",
    "docker",
    "aws",
    "machine learning",
    "data science",
    "javascript"
]

def skill_gap(user_skills, job_text):

    missing = []

    job_text = job_text.lower()

    for skill in skills_db:

        if skill in job_text and skill not in user_skills:

            missing.append(skill)

    return missing