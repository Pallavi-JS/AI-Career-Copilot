import streamlit as st

from parser import extract_text
from skills import extract_skills
from jobs import fetch_jobs
from indian_jobs import fetch_indian_jobs
from matcher import match_score
from gap import skill_gap
from interview import generate_questions
from recommendation import recommend_roles
from ats import calculate_ats_score
from learning import create_learning_roadmap


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("🤖 AI Career Copilot")

st.write(
    "Upload your resume and get personalized job matching, "
    "skill gap analysis, ATS scoring, career recommendations, "
    "learning roadmap, and interview questions."
)


# ==========================================
# RESUME UPLOAD
# ==========================================

resume = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"]
)


if resume:

    st.success("✅ Resume Uploaded Successfully!")


    # ==========================================
    # EXTRACT RESUME TEXT
    # ==========================================

    text = extract_text(resume)


    # ==========================================
    # EXTRACT SKILLS
    # ==========================================

    skills = extract_skills(text)


    # ==========================================
    # ATS SCORE
    # ==========================================

    try:

        ats_score = calculate_ats_score(
            text,
            skills
        )

    except:

        ats_score = min(
            len(skills) * 10,
            100
        )


    st.subheader("📊 ATS Resume Score")

    st.metric(
        "ATS Compatibility Score",
        f"{ats_score}/100"
    )


    if ats_score >= 80:

        st.success(
            "🟢 Excellent ATS compatibility"
        )

    elif ats_score >= 60:

        st.warning(
            "🟡 Good ATS compatibility, but there is room for improvement"
        )

    else:

        st.error(
            "🔴 Your resume may need ATS optimization"
        )


    # ==========================================
    # DETECTED SKILLS
    # ==========================================

    st.subheader("📌 Detected Skills")


    if skills:

        for skill in skills:

            st.success(
                f"✅ {skill}"
            )

    else:

        st.warning(
            "⚠️ No skills detected"
        )


    # ==========================================
    # RECOMMENDED CAREER ROLES
    # ==========================================

    st.subheader(
        "🎯 Recommended Career Roles"
    )


    roles = recommend_roles(
        skills
    )


    if roles:

        for role in roles:

            st.info(
                f"💼 {role}"
            )

    else:

        st.warning(
            "No suitable roles found"
        )


    # ==========================================
    # SPECIFIC JOB DESCRIPTION ANALYSIS
    # ==========================================

    st.subheader(
        "🎯 Analyze Resume Against a Specific Job"
    )

    st.write(
        "Paste any job description below to compare it with your resume."
    )


    job_description = st.text_area(

        "📋 Paste Job Description",

        height=250,

        placeholder=(
            "Example: We are looking for a Python Developer "
            "with skills in Python, Django, SQL, AWS, Docker "
            "and REST APIs..."
        )

    )


    if st.button(
        "🔍 Analyze Job Description"
    ):


        if not job_description.strip():

            st.warning(
                "⚠️ Please paste a job description first."
            )


        else:


            with st.spinner(
                "🤖 Analyzing your resume against this job..."
            ):


                # Calculate match score

                specific_match_score = match_score(

                    text,

                    job_description

                )


                # Find missing skills

                missing_skills = skill_gap(

                    skills,

                    job_description

                )


            st.success(
                "✅ Job analysis completed!"
            )


            # ==========================================
            # JOB MATCH SCORE
            # ==========================================

            st.subheader(
                "📊 Job Match Score"
            )


            st.metric(

                "Resume Compatibility",

                f"{round(float(specific_match_score), 2)}%"

            )


            # ==========================================
            # MATCHING SKILLS
            # ==========================================

            st.subheader(
                "✅ Matching Skills"
            )


            matching_skills = []


            job_text_lower = (

                job_description.lower()

            )


            for skill in skills:


                if skill.lower() in job_text_lower:


                    matching_skills.append(

                        skill

                    )


            if matching_skills:


                for skill in matching_skills:


                    st.success(

                        f"✅ {skill}"

                    )


            else:


                st.info(

                    "No direct matching skills detected."

                )


            # ==========================================
            # SKILL GAP ANALYSIS
            # ==========================================

            st.subheader(
                "🎯 Skill Gap Analysis"
            )


            if missing_skills:


                st.error(

                    "❌ Skills you may need to learn:"

                )


                for skill in missing_skills:


                    st.write(

                        f"🔴 {skill}"

                    )


                # ==========================================
                # PERSONALIZED LEARNING ROADMAP
                # ==========================================

                st.subheader(

                    "📚 Personalized Learning Roadmap"

                )


                roadmap = create_learning_roadmap(

                    missing_skills

                )


                for item in roadmap:


                    st.info(

                        f"🎯 {item['skill']}"

                    )


                    st.write(

                        f"📖 Topics: {item['topics']}"

                    )


                    st.write(

                        f"📊 Level: {item['level']}"

                    )


                    st.write(

                        f"⏱️ Estimated Time: {item['time']}"

                    )


                    st.markdown(

                        "---"

                    )


            else:


                st.success(

                    "🎉 Your resume contains all the important detected skills!"

                )


                st.subheader(

                    "📚 Personalized Learning Roadmap"

                )


                st.success(

                    "No major learning gaps found for this job."

                )


    # ==========================================
    # FETCH JOBS
    # ==========================================

    st.subheader(
        "💼 Job Opportunities"
    )


    with st.spinner(

        "🔍 Fetching Indian and remote job opportunities..."

    ):


        try:


            indian_jobs = fetch_indian_jobs()


        except Exception:


            indian_jobs = []


        try:


            remote_jobs = fetch_jobs()


        except Exception:


            remote_jobs = []


    # ==========================================
    # COMBINE JOBS
    # ==========================================

    all_jobs = []


    for job in indian_jobs:


        job["source"] = "India"


        all_jobs.append(

            job

        )


    for job in remote_jobs:


        job["source"] = "Remote / International"


        all_jobs.append(

            job

        )


    # ==========================================
    # CALCULATE MATCH SCORES
    # ==========================================

    results = []


    for job in all_jobs:


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


        results.append(

            {


                "title": job.get(

                    "title",

                    "Unknown Job"

                ),


                "company": job.get(

                    "company_name",

                    "Unknown Company"

                ),


                "location": job.get(

                    "location",

                    "Unknown Location"

                ),


                "score": round(

                    float(score),

                    2

                ),


                "description": description,


                "url": job.get(

                    "url",

                    ""

                ),


                "source": job.get(

                    "source",

                    "Unknown"

                )

            }

        )


    # ==========================================
    # SORT JOBS
    # ==========================================

    results = sorted(

        results,

        key=lambda x: x["score"],

        reverse=True

    )


    # ==========================================
    # INDIAN JOBS
    # ==========================================

    st.subheader(

        "🇮🇳 Indian Job Opportunities"

    )


    indian_results = [

        job

        for job in results

        if job["source"] == "India"

    ]


    if indian_results:


        for job in indian_results[:5]:


            st.markdown(

                f"### 💼 {job['title']}"

            )


            st.write(

                f"🏢 **Company:** {job['company']}"

            )


            st.write(

                f"📍 **Location:** {job['location']}"

            )


            st.write(

                f"📊 **Resume Match Score:** {job['score']}%"

            )


            st.subheader(

                "🎯 Skill Gap Analysis"

            )


            missing = skill_gap(

                skills,

                job["description"]

            )


            if missing:


                st.error(

                    "❌ Skills you may need:"

                )


                for skill in missing:


                    st.write(

                        f"🔴 {skill}"

                    )


                st.subheader(

                    "📚 Recommended Learning"

                )


                roadmap = create_learning_roadmap(

                    missing

                )


                for item in roadmap:


                    st.info(

                        f"🎯 {item['skill']}"

                    )


                    st.write(

                        f"📖 {item['topics']}"

                    )


                    st.write(

                        f"⏱️ {item['time']}"

                    )


            else:


                st.success(

                    "✅ No major skill gaps found"

                )


            if job["url"]:


                st.link_button(

                    "🔗 Apply Now",

                    job["url"]

                )


            st.markdown(

                "---"

            )


    else:


        st.info(

            "No Indian jobs found currently."

        )


    # ==========================================
    # REMOTE JOBS
    # ==========================================

    st.subheader(

        "🌍 Remote / International Job Opportunities"

    )


    remote_results = [

        job

        for job in results

        if job["source"] == "Remote / International"

    ]


    if remote_results:


        for job in remote_results[:5]:


            st.markdown(

                f"### 🌍 {job['title']}"

            )


            st.write(

                f"🏢 **Company:** {job['company']}"

            )


            st.write(

                f"📍 **Location:** {job['location']}"

            )


            st.write(

                f"📊 **Resume Match Score:** {job['score']}%"

            )


            st.subheader(

                "🎯 Skill Gap Analysis"

            )


            missing = skill_gap(

                skills,

                job["description"]

            )


            if missing:


                st.error(

                    "❌ Skills you may need:"

                )


                for skill in missing:


                    st.write(

                        f"🔴 {skill}"

                    )


                st.subheader(

                    "📚 Recommended Learning"

                )


                roadmap = create_learning_roadmap(

                    missing

                )


                for item in roadmap:


                    st.info(

                        f"🎯 {item['skill']}"

                    )


                    st.write(

                        f"📖 {item['topics']}"

                    )


                    st.write(

                        f"⏱️ {item['time']}"

                    )


            else:


                st.success(

                    "✅ No major skill gaps found"

                )


            if job["url"]:


                st.link_button(

                    "🔗 Apply Now",

                    job["url"]

                )


            st.markdown(

                "---"

            )


    else:


        st.info(

            "No remote jobs found currently."

        )


    # ==========================================
    # INTERVIEW QUESTIONS
    # ==========================================

    st.subheader(

        "🎤 Personalized Interview Questions"

    )


    questions = generate_questions(

        skills

    )


    if questions:


        for index, question in enumerate(

            questions,

            start=1

        ):


            st.write(

                f"**Q{index}.** {question}"

            )


    else:


        st.write(

            "No interview questions available."

        )