import google.generativeai as genai
import os
from PyPDF2 import PdfReader

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)


def extract_text(path):

    text = ""

    try:

        reader = PdfReader(path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    except Exception as e:

        print(e)

    return text


def analyze_resume(path):

    resume_text = extract_text(path)

    prompt = f"""

Analyze this resume and return ONLY in this format:

Score: <score>

Role: <recommended role>

Strengths: <strengths>

Improvements: <improvements>

Questions:

1. question

2. question

3. question

Resume:

{resume_text}

"""

    try:

        response = model.generate_content(
            prompt
        )

        text = response.text

        score = "Not Available"
        role = "Not Available"
        strengths = "Not Available"
        improvement = "Not Available"

        questions = []

        lines = text.split("\n")

        for line in lines:

            if line.startswith("Score:"):
                score = line.replace(
                    "Score:",
                    ""
                ).strip()

            elif line.startswith("Role:"):
                role = line.replace(
                    "Role:",
                    ""
                ).strip()

            elif line.startswith("Strengths:"):
                strengths = line.replace(
                    "Strengths:",
                    ""
                ).strip()

            elif line.startswith("Improvements:"):
                improvement = line.replace(
                    "Improvements:",
                    ""
                ).strip()

            elif (
                line.strip().startswith("1.")
                or
                line.strip().startswith("2.")
                or
                line.strip().startswith("3.")
            ):

                questions.append(
                    line.strip()
                )

        return {

            "score": score,

            "role": role,

            "strengths": strengths,

            "improvement": improvement,

            "questions": questions

        }

    except Exception as e:

        print("Gemini Error:", e)

        return {

            "score": "N/A",

            "role": "Unable to Generate",

            "strengths": "Gemini failed",

            "improvement": "Try again later",

            "questions": [

                "AI analysis unavailable"

            ]

        }