import spacy
import re
from utils import extract_text_from_pdf

nlp = spacy.load("en_core_web_sm")

def extract_details(text):
    doc = nlp(text)

    name = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), "N/A")

    email = re.search(r'\S+@\S+', text)
    email = email.group() if email else "N/A"

    skills_list = ['python', 'java', 'sql', 'excel', 'machine learning', 'power bi', 'data analysis']
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]

    education_keywords = ['b.tech', 'bachelor', 'm.tech', 'master', 'degree', 'graduation']
    education = [line for line in text.split('\n') if any(kw in line.lower() for kw in education_keywords)]

    experience_keywords = ['experience', 'worked', 'intern', 'years']
    experience = [line for line in text.split('\n') if any(kw in line.lower() for kw in experience_keywords)]

    return {
        "name": name,
        "email": email,
        "skills": found_skills,
        "education": education[:2],
        "experience": experience[:3]
    }


if __name__ == "__main__":
    print("[DEBUG] Running parser.py as main")

    
    resume_path = "D:\\resume_matcher_folder\\resumes\\resume3.pdf"

    resume_text = extract_text_from_pdf(resume_path)
    if resume_text.strip():
        details = extract_details(resume_text)
        print("\n--- Extracted Resume Details ---")
        for key, value in details.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("[ERROR] No text extracted from resume")

