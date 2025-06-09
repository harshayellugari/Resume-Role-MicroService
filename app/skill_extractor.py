import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("app/skills.json", "r") as f:
    skills_data = json.load(f)

alias_map = {}
for skill, aliases in skills_data.items():
    for alias in aliases:
        alias_map[alias.lower()] = skill

def extract_skills(text):
    text = text.lower()
    skills_found = set()
    doc = nlp(text)

    for token in doc:
        if token.text in alias_map:
            skills_found.add(alias_map[token.text])

    for phrase in alias_map:
        if f" {phrase} " in f" {text} ": 
            skills_found.add(alias_map[phrase])

    return skills_found
