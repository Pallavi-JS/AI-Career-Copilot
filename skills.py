import re


SKILLS_DB = [

    "python",
    "java",
    "c",
    "c++",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "html",
    "css",
    "javascript",
    "typescript",

    "react",
    "next.js",
    "node.js",
    "express",

    "docker",
    "kubernetes",

    "aws",
    "azure",
    "gcp",

    "git",
    "github",

    "machine learning",
    "deep learning",
    "data science",

    "pandas",
    "numpy",
    "scikit-learn",

    "tensorflow",
    "pytorch",

    "rest api",
    "fastapi",
    "flask",
    "django",

    "data structures",
    "algorithms",

    "microservices",
    "terraform",
    "system design"

]


def extract_skills(text):

    text = text.lower()

    found_skills = []


    for skill in SKILLS_DB:

        if skill == "c":

            pattern = r"(?<![a-zA-Z])c(?![a-zA-Z])"

            if re.search(pattern, text):

                found_skills.append(skill)


        elif skill == "c++":

            if "c++" in text:

                found_skills.append(skill)


        else:

            pattern = (

                r"(?<![a-zA-Z0-9])"

                + re.escape(skill)

                + r"(?![a-zA-Z0-9])"

            )

            if re.search(pattern, text):

                found_skills.append(skill)


    return found_skills