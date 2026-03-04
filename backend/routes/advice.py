from fastapi import APIRouter

router = APIRouter(prefix="/advice", tags=["Advice"])

@router.get("/week/{week}")
def get_week_advice(week: int):
    # Later connect LLM service
    return {
        "week": week,
        "advice": "Personalized advice will be generated here."
    }