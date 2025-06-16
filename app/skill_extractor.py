import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("app/skills.json", "r") as f:
    data = json.load(f)

alias_map = {}
for skill, aliases in data.items():
    for alias in aliases:
        alias_map[alias.lower()] = skill

def extract_skills(text):
    text = text.lower()
    s_f = set()
    doc = nlp(text)

    for token in doc:
        if token.text in alias_map:
            s_f.add(alias_map[token.text])

    for phrase in alias_map:
        if f" {phrase} " in f" {text} ": 
            s_f.add(alias_map[phrase])

    return s_f
