import os
from utils import extract_text_from_pdf, extract_text_from_txt
from matcher import calculate_similarity

RESUME_FOLDER = r"D:\resume_matcher_folder\resumes"
JOB_DESCRIPTION_PATH = r"D:\resume_matcher_folder\job_descriptions\job1.txt"

def main():
    jd_text = extract_text_from_txt(JOB_DESCRIPTION_PATH)
    results = []

    for file in os.listdir(RESUME_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(RESUME_FOLDER, file)
            resume_text = extract_text_from_pdf(path)

            if resume_text.strip():
                score = calculate_similarity(resume_text, jd_text, method="bert")
                results.append((file, score))

    ranked = sorted(results, key=lambda x: x[1], reverse=True)

    print("\n Ranked Resumes:")
    for i, (filename, score) in enumerate(ranked, 1):
        print(f"{i}. {filename} — Match Score: {score:.2f}")

if __name__ == "__main__":
    main()
