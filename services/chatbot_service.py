import google.generativeai as genai
import os

# Gemini API Setup
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash")


def chatbot_reply(question: str):

    try:

        response = model.generate_content(question)

        # SAFE CHECK
        if not response or not response.text:
            return {
                "reply": "Sorry, I couldn't generate a response."
            }

        return {
            "reply": response.text
        }

    except Exception as e:

        return {
            "reply": f"Error: {str(e)}"
        }