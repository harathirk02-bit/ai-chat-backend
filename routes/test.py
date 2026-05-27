from fastapi import APIRouter, Depends
from utils.jwt_handler import security

router = APIRouter()


# Start Skill Test API
@router.get("/start-test")
def start_test(
    credentials = Depends(security)
):

    questions = [

        {
            "question": "What is Python?",
            "options": [
                "Programming Language",
                "Database",
                "Browser",
                "Operating System"
            ]
        },

        {
            "question": "What is FastAPI?",
            "options": [
                "Python Framework",
                "Game Engine",
                "IDE",
                "Compiler"
            ]
        },

        {
            "question": "Machine Learning is used for?",
            "options": [
                "Learning from data",
                "Cooking",
                "Networking",
                "Typing"
            ]
        }
    ]

    return {
        "message": "Skill Test Started",
        "questions": questions
    }


# Test Result API
@router.get("/test-result")
def test_result(
    credentials = Depends(security)
):

    return {

        "score": 85,

        "status": "Good",

        "strengths": [
            "Python",
            "Problem Solving"
        ],

        "improvement_areas": [
            "Deep Learning",
            "Cloud Computing"
        ]
    }