import json


with open("app/learning_paths.json", "r") as f:
    LP = json.load(f)

def get_learning_path(missing_skills: list, max_steps: int = 4):
    result = []
    for skill in missing_skills:
        steps = LP.get(skill, {}).get("steps", [])[:max_steps]
        if steps:
            result.append({
                "skill": skill,
                "steps": steps
            })
    return result
