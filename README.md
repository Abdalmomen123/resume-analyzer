# 📄 AI Resume Analyzer

An AI-powered web application that analyzes resumes against job descriptions and provide a match score, skill comparison, and improvement insights.

---

## 🚀 Features

- **Match Score** – Calculates similarity between resume and job description
- **BERT-based Semantic Matching** – Understands meaning, not just keywords
- **Skill Extraction** – Identifies skills from resume and job description
- **Missing Skills Detection** – Highlights gaps to improve your resume
- **User-Friendly UI** – Built with Streamlit for an interactive experience

---

## 🖥️ Demo

_(Add screenshots here)_

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. User pastes a job description
3. The system:
   - Extracts text from the PDF
   - Identifies relevant skills
   - Converts text into embeddings using BERT
   - Computes similarity using cosine similarity

4. Outputs:
   - Match score (%)
   - Extracted skills
   - Missing skills

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI)
- **spaCy** (NLP)
- **Sentence Transformers (BERT)**
- **scikit-learn** (cosine similarity)
- **pdfplumber** (PDF parsing)

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app.py
├── parser.py
├── skills_extractor.py
├── matcher.py
└── README.md
```

---

## ⚙️ Installation

1. Clone the repository
2. Install dependencies
3. Download spaCy model

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 📈 Example Output

- Match Score: **78.45%**
- Missing Skills: `SQL, NLP`
- Feedback: Moderate match with room for improvement

---

## 💡 Future Improvements

- 🔥 AI-generated resume feedback (LLM integration)
- 📊 Skill importance ranking
- 🌐 Deploy app online (Streamlit Cloud / Hugging Face)
- 📄 Support for multiple resumes
- 🧠 Advanced skill extraction using NLP models

---

## 👤 Author

Abdalmomen Mohammed Awad Mohammed

---

## ⭐ Contribute / Support

If you found this useful:

- Star ⭐ the repo
- Share feedback
- Suggest improvements

---
