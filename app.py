import streamlit as st
from parser import extract_text_from_pdf
from skills_extractor import extract_skills
from matcher import calculate_similarity

st.title("AI Resume Analyzer")

cv_file = st.file_uploader("Upload your CV (PDF)")
job_desc = st.text_area("Paste Job Description")

if cv_file and job_desc:
    cv_text = extract_text_from_pdf(cv_file)
    
    cv_skills = extract_skills(cv_text)
    job_skills = extract_skills(job_desc)
    
    match_score = calculate_similarity(cv_text, job_desc)
    
    missing_skills = list(set(job_skills) - set(cv_skills))
    
    st.subheader("Match Score")
    st.write(f"{match_score}%")
    
    st.subheader("Your Skills")
    st.write(cv_skills)
    
    st.subheader("Missing Skills")
    st.write(missing_skills)