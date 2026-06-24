import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6KXe7_BlqinMpmkA5xIUci_ZtrRNqtC9Zvx9GIfNU2n-Q")

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
