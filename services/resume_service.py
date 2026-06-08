import google.generativeai as genai

import os

from PyPDF2 import PdfReader


# GEMINI SETUP

genai.configure(

    api_key=os.getenv(

        "GEMINI_API_KEY"

    )

)

model = genai.GenerativeModel(

    "gemini-2.0-flash"

)


# EXTRACT PDF TEXT

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

        text = ""

    return text


# ANALYZE RESUME

def analyze_resume(path):

    resume_text = extract_text(

        path

    )

    prompt = f"""

Analyze this resume.

Give:

1 Resume Score

2 Recommended Role

3 Strengths

4 Improvements

5 Three Interview Questions

Resume:

{resume_text}

Return concise answers.

"""

    try:

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

    except Exception as e:

        print(

            "Gemini Error:",

            e

        )

        return {

            "score":

            "N/A",

            "role":

            "Unable to Generate",

            "strengths":

            "Gemini quota exceeded",

            "improvement":

            "Try again later",

            "questions":

            [

                "AI analysis unavailable currently"

            ]

        }