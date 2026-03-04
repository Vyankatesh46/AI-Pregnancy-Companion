from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/kicks", tags=["Kicks"])

class KickInput(BaseModel):
    daily_count: int

@router.post("/log")
def log_kick(data: KickInput):
    # Later connect ML anomaly detection
    return {
        "message": "Kick logged",
        "count": data.daily_count
    }