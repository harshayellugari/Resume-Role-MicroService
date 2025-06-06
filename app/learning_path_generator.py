import json

# Load learning paths once
with open("app/learning_paths.json", "r") as f:
    LEARNING_PATHS = json.load(f)

def get_learning_path(missing_skills: list, max_steps: int = 4) -> list:
    result = []
    for skill in missing_skills:
        steps = LEARNING_PATHS.get(skill, {}).get("steps", [])[:max_steps]
        if steps:
            result.append({
                "skill": skill,
                "steps": steps
            })
    return result
