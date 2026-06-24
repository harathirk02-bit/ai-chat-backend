import google.generativeai as genai
import os

# Gemini API Setup
genai.configure(
    api_key=os.getenv("AQ.Ab8RN6KXe7_BlqinMpmkA5xIUci_ZtrRNqtC9Zvx9GIfNU2n-Q")
)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


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
