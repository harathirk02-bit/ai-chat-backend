from sklearn.feature_extraction.text import CountVectorizer
from PyPDF2 import PdfReader


# Skills Database
skills_database = [
    "python",
    "react",
    "machine learning",
    "fastapi",
    "sql",
    "html",
    "css",
    "javascript",
    "tensorflow",
    "mongodb"
]


# Read Resume Text File
def read_resume_text(file_path):

    with open(file_path, "r", encoding="utf-8") as file:

        text = file.read()

    return text.lower()


# Read PDF Resume
def read_resume_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text.lower()


# Extract Skills
def extract_skills(resume_text):

    vectorizer = CountVectorizer(
        vocabulary=skills_database
    )

    X = vectorizer.fit_transform([resume_text])

    found_skills = vectorizer.get_feature_names_out()

    resume_vector = X.toarray()[0]

    detected_skills = []

    for skill, value in zip(found_skills, resume_vector):

        if value > 0:

            detected_skills.append(skill)

    return detected_skills


# Generate Resume Score
def generate_resume_score(skills):

    total_skills = len(skills_database)

    found_skills = len(skills)

    score = int((found_skills / total_skills) * 100)

    return score


# Strengths and Weaknesses
def analyze_strengths_weaknesses(skills):

    strengths = []

    weaknesses = []

    if "python" in skills:
        strengths.append("Good Python Knowledge")

    if "machine learning" in skills:
        strengths.append("AI/ML Skills")

    if "react" not in skills:
        weaknesses.append("Frontend Skills Missing")

    if "mongodb" not in skills:
        weaknesses.append("Database Skills Need Improvement")

    return strengths, weaknesses


# Main Program
if __name__ == "__main__":

    resume_text = read_resume_text("sample_resume.txt")

    skills = extract_skills(resume_text)

    score = generate_resume_score(skills)

    strengths, weaknesses = analyze_strengths_weaknesses(skills)

    print("\nDetected Skills:")
    print(skills)

    print("\nResume Score:")
    print(score)

    print("\nStrengths:")
    print(strengths)

    print("\nWeaknesses:")
    print(weaknesses)