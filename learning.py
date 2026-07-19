def create_learning_roadmap(missing_skills):

    roadmap = []

    learning_data = {

        "python": {
            "topics": "Python fundamentals, functions, OOP and libraries",
            "level": "Beginner to Intermediate",
            "time": "2 weeks"
        },

        "java": {
            "topics": "Java fundamentals, OOP, collections and Spring Boot",
            "level": "Beginner to Intermediate",
            "time": "3 weeks"
        },

        "sql": {
            "topics": "SQL queries, joins, subqueries and database design",
            "level": "Beginner",
            "time": "1 week"
        },

        "docker": {
            "topics": "Containers, images, Dockerfiles and Docker Compose",
            "level": "Beginner",
            "time": "1 week"
        },

        "aws": {
            "topics": "EC2, S3, IAM and basic cloud deployment",
            "level": "Beginner",
            "time": "2 weeks"
        },

        "kubernetes": {
            "topics": "Pods, deployments, services and cluster basics",
            "level": "Intermediate",
            "time": "2 weeks"
        },

        "react": {
            "topics": "Components, props, state, hooks and API integration",
            "level": "Beginner to Intermediate",
            "time": "2 weeks"
        },

        "javascript": {
            "topics": "ES6, DOM, asynchronous programming and APIs",
            "level": "Beginner",
            "time": "2 weeks"
        },

        "machine learning": {
            "topics": "Supervised learning, unsupervised learning and model evaluation",
            "level": "Intermediate",
            "time": "3 weeks"
        },

        "data science": {
            "topics": "Python, Pandas, NumPy, visualization and statistics",
            "level": "Beginner to Intermediate",
            "time": "3 weeks"
        }

    }


    for skill in missing_skills:

        skill_lower = skill.lower()


        if skill_lower in learning_data:

            roadmap.append({

                "skill": skill,

                "topics": learning_data[skill_lower]["topics"],

                "level": learning_data[skill_lower]["level"],

                "time": learning_data[skill_lower]["time"]

            })


        else:

            roadmap.append({

                "skill": skill,

                "topics": f"Learn the fundamentals and practical applications of {skill}",

                "level": "Beginner",

                "time": "1-2 weeks"

            })


    return roadmap