import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

def generate_roadmap(skill):

    prompt = f"""
    Create a roadmap for becoming a {skill} developer.
    
    Include:
    - Daily targets
    - Weekly targets
    - Monthly targets
    """

    response = model.generate_content(prompt)

    return response.text


roadmap = generate_roadmap("Python")

print(roadmap)