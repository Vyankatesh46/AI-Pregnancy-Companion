from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/mood", tags=["Mood"])

class MoodInput(BaseModel):
    answers: list[int]
    sleep_hours: float

@router.post("/score")
def score_mood(data: MoodInput):
    # Later this will call ML model
    return {
        "risk_level": "Low",
        "score": sum(data.answers)
    }