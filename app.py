import streamlit as st
from parser import extract_text_from_pdf
from skills_extractor import extract_skills
from matcher import calculate_similarity

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.markdown("Match your resume with job descriptions using AI")
st.divider()

st.header("📥 Input")

col1, col2 = st.columns(2)
with col1:
    cv_file = st.file_uploader("Upload your CV (PDF)")
with col2:
    job_desc = st.text_area("Paste Job Description")
analyze_button = st.button("🚀 Analyze Resume")

if analyze_button:
    if not cv_file or not job_desc:
        st.warning("⚠️ Please upload a CV and paste a job description.")
    else:
        with st.spinner("Analyzing your resume... 🤖"):
            cv_text = extract_text_from_pdf(cv_file)
            
            cv_skills = extract_skills(cv_text)
            job_skills = extract_skills(job_desc)
            
            match_score = calculate_similarity(cv_text, job_desc)
            
            missing_skills = list(set(job_skills) - set(cv_skills))

        st.divider()
        st.header("📊 Results")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Your Skills")
            st.write(", ".join(cv_skills) if cv_skills else "No skills detected")

        with col2:
            st.subheader("❌ Missing Skills")
            st.write(", ".join(missing_skills) if missing_skills else "None 🎉")
        
        st.divider()
            
        score = max(0, min(100, match_score))

        st.subheader("📊 Match Score")
        st.progress(int(score))
        st.write(f"### {score:.2f}% match")

        # Feedback
        if score >= 75:
            st.success("🔥 Strong match! You're a great fit.")
        elif score > 50:
            st.warning("⚠️ You can improve your resume.")
        else:
            st.error("❌ Low match. Consider improving your resume.")