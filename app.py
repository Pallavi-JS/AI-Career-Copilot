import streamlit as st

from parser import extract_text
from skills import extract_skills
from jobs import fetch_jobs
from matcher import match_score
from gap import skill_gap
from interview import generate_questions
from recommendation import recommend_roles

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Career Copilot")

st.write(
    "Upload your resume and get job matches, skill gap analysis, recommended roles, and interview questions."
)

resume = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if resume:

    st.success("✅ Resume Uploaded Successfully!")

    # Extract resume text
    text = extract_text(resume)

    # Extract skills
    skills = extract_skills(text)

    # ATS Score
    ats_score = min(len(skills) * 10, 100)

    st.subheader("📊 ATS Score")

    st.metric(
        "Score",
        f"{ats_score}/100"
    )

    # Skills
    st.subheader("📌 Detected Skills")

    if skills:

        for skill in skills:
            st.success(skill)

    else:
        st.warning("No skills detected")

    # Recommended Roles
    st.subheader("🎯 Recommended Roles")

    roles = recommend_roles(skills)

    if roles:

        for role in roles:
            st.success(role)

    else:
        st.warning("No suitable roles found")

    # Fetch Jobs
    with st.spinner("Fetching Jobs..."):

        jobs = fetch_jobs()

    results = []

    for job in jobs:

        description = job.get(
            "description",
            ""
        )

        try:

            score = match_score(
                text,
                description
            )

        except:

            score = 0

        results.append({

            "title": job.get(
                "title",
                "Unknown Job"
            ),

            "company": job.get(
                "company_name",
                "Unknown Company"
            ),

            "score": round(
                float(score),
                2
            ),

            "description": description,

            "url": job.get(
                "url",
                ""
            )
        })

    # Sort by score
    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    # Top Jobs
    st.subheader("💼 Top Matching Jobs")

    for job in results[:5]:

        st.markdown(
            f"### {job['title']}"
        )

        st.write(
            f"**Company:** {job['company']}"
        )

        st.write(
            f"**Match Score:** {job['score']}%"
        )

        missing = skill_gap(
            skills,
            job["description"]
        )

        if missing:

            st.write(
                "❌ Missing Skills:"
            )

            for skill in missing:

                st.write(
                    f"• {skill}"
                )

        else:

            st.write(
                "✅ No major skill gaps found"
            )

        if job["url"]:

            st.link_button(
                "Apply Now",
                job["url"]
            )

        st.markdown("---")

    # Interview Questions
    st.subheader("🎤 Interview Questions")

    questions = generate_questions(
        skills
    )

    if questions:

        for q in questions:

            st.write(
                f"• {q}"
            )

    else:

        st.write(
            "No interview questions available."
        )