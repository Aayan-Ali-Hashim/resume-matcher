import streamlit as st
from resume_utils import extract_text_from_pdf,preprocess,extract_skills,load_nlp_model
from model_utils import get_similarity_score


nlp = load_nlp_model()

st.title("Resume vs Job Description Matcher")

# File uploader
resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste your job description")

custom_skills_input = st.text_input(
    "Enter skill keywords to match (comma-separated)",
    value="python, sql, machine learning, excel, power bi, deep learning"
)

# Convert to list
custom_skills = [skill.strip().lower() for skill in custom_skills_input.split(",") if skill.strip()]


if resume_file and job_description:
    resume_text = extract_text_from_pdf(resume_file)
    resume_clean = preprocess(resume_text,nlp)
    jd_clean = preprocess(job_description,nlp)

    score = get_similarity_score(resume_clean,jd_clean)
    skills_in_resume = extract_skills(resume_clean, custom_skills)
    skills_in_jd = extract_skills(jd_clean, custom_skills)

    st.subheader("Match Score")
    st.metric(label = "Match %", value=f"{score}%")

    st.subheader("Skills Comparison")
    st.write(f"✅ Matching Skills: {list(set(skills_in_resume) & set(skills_in_jd))}")
    st.write(f"❌ Missing Skills: {list(set(skills_in_jd) - set(skills_in_resume))}")