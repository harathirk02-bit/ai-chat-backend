import google.generativeai as genai

import os

from PyPDF2 import PdfReader


genai.configure(

    api_key=os.getenv(

        "GEMINI_API_KEY"

    )

)

model = genai.GenerativeModel(

    "gemini-1.5-flash"

)


def extract_text(path):

    text = ""

    try:

        reader = PdfReader(path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text

    except:

        text = ""

    return text


def analyze_resume(path):

    resume_text = extract_text(
        path
    )

    prompt = f"""

Analyze this resume.

Give:

Resume Score

Recommended Role

Strengths

Improvements

3 Interview Questions

Resume:

{resume_text}

Return concise answers.

"""

    response = model.generate_content(
        prompt
    )

    return {

        "score":

        "Generated",

        "role":

        "AI Suggested",

        "strengths":

        "Based on Resume",

        "improvement":

        "Based on Resume",

        "questions":

        [

            response.text

        ]

    }