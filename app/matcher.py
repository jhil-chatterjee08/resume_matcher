from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util

from utils import extract_text_from_pdf, extract_text_from_txt


model = SentenceTransformer('all-MiniLM-L6-v2')

def cosine_similarity_score(resume_text, jd_text):
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume_text, jd_text])
    return cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

def bert_similarity_score(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return float(similarity[0][0])

def calculate_similarity(resume_text, jd_text, method="bert"):
    if method == "cosine":
        return cosine_similarity_score(resume_text, jd_text)
    else:
        return bert_similarity_score(resume_text, jd_text)

if __name__ == "__main__":
    resume_text = extract_text_from_pdf(r"D:\resume_matcher_folder\resumes\resume3.pdf")
    jd_text = extract_text_from_txt(r"D:\resume_matcher_folder\job_descriptions\job3.txt")


    score = calculate_similarity(resume_text, jd_text, method="bert")
    print(f"Match Score using BERT: {score:.2f}")

