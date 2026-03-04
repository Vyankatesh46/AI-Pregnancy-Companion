from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/profile", tags=["Profile"])

class ProfileInput(BaseModel):
    name: str
    pregnancy_week: int
    diet: str
    condition: str

@router.post("/create")
def create_profile(data: ProfileInput):
    return {
        "message": "Profile created",
        "week": data.pregnancy_week
    }