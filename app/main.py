from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

from app.skill_extractor import extract_skills
from app.fit_score_engine import compute_fit_score
from app.learning_path_generator import get_learning_path

with open("app/config.json", "r") as f:
    CONFIG = json.load(f)

app = FastAPI()

class FitRequest(BaseModel):
    resume_text: str
    job_description: str

class LearningStep(BaseModel):
    skill: str
    steps: List[str]

class FitResponse(BaseModel):
    fit_score: float
    verdict: str
    matched_skills: List[str]
    missing_skills: List[str]
    recommended_learning_track: List[LearningStep]
    status: str

@app.post("/evaluate-fit", response_model=FitResponse)
def evaluate_fit(data: FitRequest):
    resume_skills = extract_skills(data.resume_text)
    jd_skills = extract_skills(data.job_description)

    matched = list(resume_skills & jd_skills)
    missing = list(jd_skills - resume_skills)
    score = compute_fit_score(data.resume_text, data.job_description)

    cutoffs = CONFIG["fit_score_cutoffs"]
    if score >= cutoffs["strong_fit"]:
        verdict = "strong_fit"
    elif score >= cutoffs["moderate_fit"]:
        verdict = "moderate_fit"
    else:
        verdict = "weak_fit"

    track = get_learning_path(missing, CONFIG["max_learning_steps_per_skill"])

    return {
        "fit_score": score,
        "verdict": verdict,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommended_learning_track": track,
        "status": "success"
    }

@app.get("/health")
def health():
    return {"status": "ok"}