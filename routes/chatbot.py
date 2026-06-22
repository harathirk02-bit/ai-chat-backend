from fastapi import APIRouter, Depends
from pydantic import BaseModel

from utils.jwt_handler import security
from services.chatbot_service import chatbot_reply

router = APIRouter()

# Request body
class ChatRequest(BaseModel):
    question: str

# Chatbot API
@router.post("/chatbot")
def chatbot(
    data: ChatRequest,
    credentials=Depends(security)
):

    reply = chatbot_reply(data.question)

    return {
        "question": data.question,
        "reply": reply
    }