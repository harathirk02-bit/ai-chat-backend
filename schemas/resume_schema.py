from pydantic import BaseModel


class ResumeResponse(BaseModel):
    message: str
    filename: str