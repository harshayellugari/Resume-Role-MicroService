from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_fit_score(skills, req_skills):
    resume_text = " ".join(skills)
    job_description = " ".join(req_skills)
    corpus = [resume_text, job_description]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(corpus)
    score = cosine_similarity(vectors[0], vectors[1])[0][0]
    return round(score, 2)