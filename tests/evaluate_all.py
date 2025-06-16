import os
import json
from app.skill_extractor import extract_skills
from app.fit_score_engine import compute_fit_score
from app.learning_path_generator import get_learning_path

with open("app/config.json", "r") as f:
    config = json.load(f)

results = []

for i in range(1, 51):
    with open(f"app/sample_data/sample_resumes/resume_{i}.txt") as r:
        resume_text = r.read()

    with open(f"app/sample_data/sample_jobs/job_description_{i}.txt") as j:
        jd_text = j.read()

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched = list(resume_skills & jd_skills)
    missing = list(jd_skills - resume_skills)
    score = compute_fit_score(resume_text, jd_text)

    cutoffs = config["fit_score_cutoffs"]
    if score >= cutoffs["strong_fit"]:
        verdict = "strong_fit"
    elif score >= cutoffs["moderate_fit"]:
        verdict = "moderate_fit"
    else:
        verdict = "weak_fit"

    learning_track = get_learning_path(missing, config["max_learning_steps_per_skill"])

    results.append({
        "resume": f"resume_{i:02}.txt",
        "job": f"job_{i:02}.txt",
        "fit_score": score,
        "verdict": verdict,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommended_learning_track": learning_track
    })

with open("evaluation_results.json", "w") as out:
    json.dump(results, out, indent=4)

print("Evaluation complete. Results saved to evaluation_results.json.")
