skills_db = [
    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "docker",
    "aws",
    "machine learning",
    "data science"
]

def extract_skills(text):

    text = text.lower()

    found = []

    for skill in skills_db:

        if skill in text:
            found.append(skill)

    return found