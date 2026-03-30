from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(cv_text, job_desc):
    cv_embedding = model.encode([cv_text])
    job_desc_embedding = model.encode([job_desc])
    
    similarity = cosine_similarity(cv_embedding, job_desc_embedding)[0][0]
    
    return round(similarity * 100, 2)