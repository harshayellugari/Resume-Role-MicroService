from app.skill_extractor import extract_skills

def test_basic_skills():
    text = "I have worked on Python, Django, and REST API development."
    expected = {"python", "django", "rest api"}
    result = extract_skills(text)
    assert expected.issubset(result)

def test_multi_word_skills():
    text = "Experienced with Amazon Web Services and system design patterns."
    expected = {"aws", "system design"}
    result = extract_skills(text)
    assert expected.issubset(result)

def test_no_skills():
    text = "I enjoy cooking and playing football."
    result = extract_skills(text)
    assert len(result) == 0
