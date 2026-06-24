import google.generativeai as genai
import os


# Configure Gemini API Key

genai.configure(
    api_key=os.getenv("AQ.Ab8RN6KXe7_BlqinMpmkA5xIUci_ZtrRNqtC9Zvx9GIfNU2n-Q")
)


# Load Gemini Model

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


# Chatbot Function

def ask_chatbot(user_question):

    try:

        response = model.generate_content(
            user_question
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"



# Example Test

if __name__ == "__main__":

    question = input(
        "Ask Question: "
    )

    reply = ask_chatbot(
        question
    )

    print(
        "\nAI Reply:",
        reply
    )
