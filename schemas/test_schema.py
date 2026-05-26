from pydantic import BaseModel
from typing import List


class TestQuestion(BaseModel):
    questions: List[str]


class TestResult(BaseModel):
    score: int
    status: str