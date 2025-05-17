import streamlit as st
import os
import sys
import tempfile

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from utils import extract_text_from_pdf
from matcher import calculate_similarity

# App setup
st.set_page_config(page_title="Resume Matcher", layout="centered")
st.title("Resume vs Job Description Matcher")
st.markdown("Upload a resume and paste a job description to see how well they match.")

uploaded_resume = st.file_uploader("Upload Resume (PDF format only)", type=["pdf"])

job_description = st.text_area("Paste Job Description")

method = st.radio("Choose Similarity Method", ["BERT (Semantic)", "Cosine (Keyword-based)"])
selected_method = "bert" if "BERT" in method else "cosine"

if st.button("Match Now"):
    if uploaded_resume is None or not job_description.strip():
        st.warning("Please upload a resume and enter a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_resume.read())
            resume_path = temp_file.name

        resume_text = extract_text_from_pdf(resume_path)

        if not resume_text.strip():
            st.error("Could not extract text from resume. Try another file.")
        else:
            score = calculate_similarity(resume_text, job_description, method=selected_method)
            st.success(f"Match Score using {method}: **{score:.2f}**")

