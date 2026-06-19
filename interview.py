def generate_questions(skills):

    questions = []

    if "python" in skills:

        questions.extend([
            "What is List Comprehension?",
            "Difference between List and Tuple?"
        ])

    if "java" in skills:

        questions.extend([
            "What is JVM?",
            "What is Multithreading?"
        ])

    if "sql" in skills:

        questions.extend([
            "Difference between WHERE and HAVING?",
            "Explain JOIN Types."
        ])

    return questions