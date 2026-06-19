def recommend_roles(skills):

    roles = []

    if "java" in skills:
        roles.append("Java Developer")

    if "python" in skills:
        roles.append("Python Developer")

    if "sql" in skills:
        roles.append("Data Analyst")

    if "machine learning" in skills:
        roles.append("ML Engineer")

    return roles