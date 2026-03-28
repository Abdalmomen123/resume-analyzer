from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(cv_text, job_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([cv_text, job_text])
    similarity = cosine_similarity(vectors)[0][1]
    return round(similarity * 100, 2)