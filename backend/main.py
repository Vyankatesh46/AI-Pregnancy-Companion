from fastapi import FastAPI
from backend.routes import mood, kicks, profile, advice

app = FastAPI()

app.include_router(mood.router)
app.include_router(kicks.router)
app.include_router(profile.router)
app.include_router(advice.router)

@app.get("/")
def root():
    return {"message": "AI Pregnancy Companion Backend Running"}
