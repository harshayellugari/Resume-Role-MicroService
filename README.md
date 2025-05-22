# 🧠 Resume–Role Fit Evaluator (Score & Track Generator)

This microservice checks how well a resume matches a job description. It gives a score, shows which skills are matched or missing, and recommends what to learn step-by-step to fill the gaps. Built fully offline. No copying, no external APIs. Just clean Python and FastAPI.

---

## ⚙️ What It Does

- Checks resume and JD compatibility
- Extracts and maps skills using your own `skills.json`
- Calculates fit score using TF-IDF + Cosine Similarity
- Gives learning steps for each missing skill from `learning_paths.json`
- Built using FastAPI + Pydantic + Scikit-learn
- Offline and customizable through config files

---

## 🧱 Folder Structure

```

Resume-Role-MicroService/
├── app/
│   ├── main.py
│   ├── skill\_extractor.py
│   ├── fit\_score\_engine.py
│   ├── learning\_path\_generator.py
│   ├── config.json
│   ├── skills.json
│   ├── learning\_paths.json
│   └── sample\_data/
│       ├── sample\_resumes/
│       └── sample\_jobs/
├── tests/
├── requirements.txt
├── Dockerfile
└── README.md

````

---

## API Usage

### POST `/evaluate-fit`

**Input JSON:**
```json
{
  "resume_text": "I’ve worked on Flask, Docker, and cloud basics.",
  "job_description": "Looking for a backend dev with AWS, Docker, and system design."
}
````

**Output JSON:**

```json
{
  "fit_score": 0.52,
  "verdict": "moderate_fit",
  "matched_skills": ["docker"],
  "missing_skills": ["aws", "system design"],
  "recommended_learning_track": [
    {
      "skill": "aws",
      "steps": [
        "Understand basic AWS services",
        "Create an AWS free tier account",
        "Deploy a simple app to EC2",
        "Learn IAM and permissions"
      ]
    }
  ],
  "status": "success"
}
```

---

## 🧪 How to Run Locally

```bash
cd Resume-Role-MicroService
python3 -m venv fapivenv
source fapivenv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

You can test everything directly from Swagger UI.

---

## 🧠 Testing Strategy

* `tests/` folder contains logic tests (manual or automated with pytest)
* Tested for strong\_fit (>0.9), moderate\_fit (\~0.5), and weak\_fit (<0.4)
* Skill normalization tested using alias words from `skills.json`
* Sample resumes and JDs are stored in `app/sample_data/`

---

## 🧰 Configurable Files

You can tweak how the system behaves without changing code:

* `skills.json`: maps skill synonyms to a base skill
* `learning_paths.json`: holds predefined learning steps
* `config.json`: change fit score cutoffs and alias mappings

---

## 🧑‍🤝‍🧑 Team Collaboration

This project is being built by **Harsha Yellugari**, with early help from **Naveen Josh**, my teammate on data selection and initial planning.
Code written completely from scratch, fully offline, and verified step-by-step.

---

## 📦 Docker (Optional for Deployment)

```bash
docker build -t resume-fit-evaluator .
docker run -p 8000:8000 resume-fit-evaluator
```

---

## 📝 Goals

This wasn’t just a microservice. The goal was to:

* Learn and implement real-world backend structure
* Use FastAPI professionally
* Handle text similarity + logic with explainability
* Build clean code without copying anything
* Deliver something beyond what was asked (optional UI planned later)

---

## ✊ Ownership Note

This project is built for Turtil internship, but everything — from structure to logic to configuration — is handwritten, debugged, and documented by me, with full understanding.

---

## ✍️ Author

**Harsha Yellugari**
B.Tech – GPREC
Intern @ Turtil

## 🔗 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/yellugari-harsha-vardhan-reddy-9673322ab/)


> “No shortcuts. No AI-written backend. Just me, VS Code, and learning one bug at a time.”

```

---

```
