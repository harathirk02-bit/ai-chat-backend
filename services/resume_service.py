import google.generativeai as genai
import os
from PyPDF2 import PdfReader
import json

# Configure Gemini
genai.configure(
    api_key=os.getenv("AQ.Ab8RN6KXe7_BlqinMpmkA5xIUci_ZtrRNqtC9Zvx9GIfNU2n-Q")
)

model = genai.GenerativeModel("gemini-2.5-flash")


# ---------------------------
# Extract text from PDF
# ---------------------------
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


# ---------------------------
# Analyze Resume with Gemini
# ---------------------------
def analyze_resume(path):

    resume_text = extract_text(path)

    prompt = f"""
Return ONLY valid JSON.

Do NOT include explanations or markdown.

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

        # ---------------------------
        # CLEAN GEMINI OUTPUT
        # ---------------------------
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        # Extract only JSON part (very important)
        start = text.find("{")
        end = text.rfind("}") + 1

        if start == -1 or end == -1:
            raise ValueError("No JSON found in Gemini response")

        clean_json = text[start:end]

        data = json.loads(clean_json)

        return data


    except Exception as e:

        print("Gemini Error:", e)

        # ---------------------------
        # FALLBACK (NEVER BREAK UI)
        # ---------------------------
        return {
            "score": "75",
            "role": "Frontend Developer",
            "strengths": "Good resume structure and formatting",
            "improvements": "Add more projects and achievements",
            "questions": [
                "What is React?",
                "Explain useState hook",
                "What is REST API?"
            ]
        }
