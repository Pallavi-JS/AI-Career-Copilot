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


def skill_gap(user_skills, job_text):

    missing = []


    # Convert resume skills to lowercase

    user_skills = [

        skill.lower().strip()

        for skill in user_skills

    ]


    job_text = job_text.lower()


    for skill in SKILLS_DB:


        # Check whether the job requires the skill

        if skill == "c":

            pattern = r"(?<![a-zA-Z])c(?![a-zA-Z])"

            required = re.search(

                pattern,

                job_text

            )


        elif skill == "c++":

            required = "c++" in job_text


        else:

            pattern = (

                r"(?<![a-zA-Z0-9])"

                + re.escape(skill)

                + r"(?![a-zA-Z0-9])"

            )

            required = re.search(

                pattern,

                job_text

            )


        # If job requires skill but resume does not have it

        if required and skill not in user_skills:

            missing.append(skill)


    return missing