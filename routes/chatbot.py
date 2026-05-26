from fastapi import APIRouter, Depends
from utils.jwt_handler import security
from services.chatbot_service import chatbot_reply

router = APIRouter()


# AI Chatbot API
@router.get("/chatbot")
def chatbot(
    question: str,
    credentials = Depends(security)
):

    response = chatbot_reply(question)

    return {
        "question": question,
        "response": response
    }