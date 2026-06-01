import google.generativeai as genai
import os

# Gemini API Setup

genai.configure(

    api_key=os.getenv(
        "GEMINI_API_KEY"
    )

)

# Load Gemini Model

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)


def chatbot_reply(question: str):

    try:

        response = model.generate_content(
            question
        )

        return {

            "reply":
            response.text

        }

    except Exception as e:

        return {

            "reply":
            str(e)

        }