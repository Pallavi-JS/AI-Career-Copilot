import re


def calculate_ats_score(text, skills):

    score = 0

    text_lower = text.lower()


    # ---------------------------------------
    # 1. CONTACT INFORMATION - 10 POINTS
    # ---------------------------------------

    contact_score = 0


    # Email

    if re.search(

        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",

        text

    ):

        contact_score += 5


    # Phone number

    if re.search(

        r"\+?\d[\d\s-]{8,}",

        text

    ):

        contact_score += 5


    score += contact_score


    # ---------------------------------------
    # 2. STANDARD RESUME SECTIONS - 20 POINTS
    # ---------------------------------------

    sections = {

        "education": 5,

        "skills": 5,

        "projects": 5,

        "certifications": 5

    }


    for section, points in sections.items():

        if section in text_lower:

            score += points


    # ---------------------------------------
    # 3. TECHNICAL SKILLS - 20 POINTS
    # ---------------------------------------

    skill_count = len(skills)


    if skill_count >= 10:

        score += 20

    elif skill_count >= 7:

        score += 15

    elif skill_count >= 4:

        score += 10

    elif skill_count >= 1:

        score += 5


    # ---------------------------------------
    # 4. EDUCATION DETAILS - 10 POINTS
    # ---------------------------------------

    if any(

        word in text_lower

        for word in [

            "bachelor",

            "engineering",

            "university",

            "college",

            "degree",

            "cgpa",

            "gpa"

        ]

    ):

        score += 10


    # ---------------------------------------
    # 5. PROJECTS / EXPERIENCE - 15 POINTS
    # ---------------------------------------

    project_words = [

        "built",

        "developed",

        "implemented",

        "designed",

        "created",

        "developed",

        "project"

    ]


    project_count = sum(

        1

        for word in project_words

        if word in text_lower

    )


    if project_count >= 4:

        score += 15

    elif project_count >= 2:

        score += 10

    elif project_count >= 1:

        score += 5


    # ---------------------------------------
    # 6. QUANTIFIABLE ACHIEVEMENTS - 10 POINTS
    # ---------------------------------------

    numbers = re.findall(

        r"\b\d+%|\b\d+\+|\b\d+\b",

        text

    )


    if len(numbers) >= 5:

        score += 10

    elif len(numbers) >= 2:

        score += 5


    # ---------------------------------------
    # 7. ACTION VERBS - 5 POINTS
    # ---------------------------------------

    action_verbs = [

        "built",

        "developed",

        "implemented",

        "designed",

        "created",

        "optimized",

        "analyzed",

        "improved"

    ]


    action_count = sum(

        1

        for verb in action_verbs

        if verb in text_lower

    )


    if action_count >= 4:

        score += 5

    elif action_count >= 2:

        score += 3


    # ---------------------------------------
    # FINAL SCORE
    # ---------------------------------------

    return min(score, 100)