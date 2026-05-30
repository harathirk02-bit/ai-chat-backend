import google.generativeai as genai

# Add Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Load Gemini Model
model = genai.GenerativeModel("gemini-pro")

def ask_chatbot(user_question):

    response = model.generate_content(user_question)

    return response.text


# Example
question = "Suggest roadmap for becoming ML Engineer"

reply = ask_chatbot(question)

print(reply)