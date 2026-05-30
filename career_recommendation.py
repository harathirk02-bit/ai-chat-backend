def recommend_career(skills):

    if "Machine Learning" in skills:
        return "ML Engineer"

    elif "React" in skills:
        return "Frontend Developer"

    elif "FastAPI" in skills:
        return "Backend Developer"

    else:
        return "Software Developer"


user_skills = [
    "Python",
    "React",
    "Machine Learning"
]

career = recommend_career(user_skills)

print("Recommended Career:", career)