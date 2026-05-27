def chatbot_reply(question: str):

    responses = {
        "python": "Python is a powerful programming language used in AI and web development.",

        "fastapi": "FastAPI is a modern Python framework used for building APIs.",

        "ml": "Machine Learning helps systems learn from data."
    }

    question = question.lower()

    for key in responses:

        if key in question:
            return {
                "reply": responses[key]
            }

    return {
        "reply": "I am your AI Career Assistant."
    }