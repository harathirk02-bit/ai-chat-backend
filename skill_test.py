questions = [
    {
        "question": "What is Python?",
        "options": [
            "Programming Language",
            "Database",
            "Operating System"
        ],
        "answer": "Programming Language"
    },

    {
        "question": "What is React?",
        "options": [
            "Library",
            "Browser",
            "Database"
        ],
        "answer": "Library"
    },

    {
        "question": "What is Machine Learning?",
        "options": [
            "AI Concept",
            "Web Browser",
            "Programming IDE"
        ],
        "answer": "AI Concept"
    }
]

score = 0

for q in questions:

    print("\n", q["question"])

    for i, option in enumerate(q["options"]):
        print(f"{i+1}. {option}")

    user_choice = int(input("Enter option number: "))

    selected_answer = q["options"][user_choice - 1]

    if selected_answer == q["answer"]:
        score += 1

print("\nFinal Score:", score)