import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "machine learning", "deep learning",
    "tensorflow", "pytorch", "sql", "data analysis",
    "nlp", "pandas", "numpy"
]

def extract_skills(text):
    text = text.lower()
    found_skills = [skill for skill in SKILLS_DB if skill in text]
    return list(set(found_skills))