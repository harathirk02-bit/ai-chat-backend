import google.generativeai as genai
import os
from PyPDF2 import PdfReader
import json

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


# Extract text from PDF
def extract_text(path):

    text = ""

    try:
        reader = PdfReader(path)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    except Exception as e:
        print("PDF Error:", e)

    return text


# Main function
def analyze_resume(path):

    resume_text = extract_text(path)

    prompt = f"""
Return ONLY valid JSON. Do NOT add explanation or markdown.

Format:
{{
  "score": "",
  "role": "",
  "strengths": "",
  "improvements": "",
  "questions": ["", "", ""]
}}

Resume:
{resume_text}
"""

    try:

        response = model.generate_content(prompt)

        text = response.text

        # Clean Gemini response (important)
        text = text.replace("```json", "").replace("```", "").strip()

        # Convert to Python dict
        data = json.loads(text)

        return data

    except Exception as e:

        print("Gemini Error:", e)

        return {
            "score": "N/A",
            "role": "Unable to Generate",
            "strengths": "Gemini failed",
            "improvements": "Try again later",
            "questions": [
                "AI analysis unavailable"
            ]
        }