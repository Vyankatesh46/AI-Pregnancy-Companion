"""
Main FastAPI Application
Person 2: Backend API Developer
Person 5: Environment validation integration
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from integrations import validate_environment
from backend.routes.voice import router as voice_router

# Initialize FastAPI
app = FastAPI(
    title="AI Pregnancy Companion",
    description="Voice-enabled pregnancy support assistant",
    version="1.0.0"
)

# CORS configuration (allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(voice_router, prefix="/api")


@app.on_event("startup")
async def startup_event():
    """
    Validate environment variables on startup
    """
    try:
        validate_environment()
        print("✅ Environment validation passed")
    except Exception as e:
        print(f"❌ Environment validation failed: {e}")
        raise


@app.get("/health")
async def health_check():
    """
    Basic health check endpoint
    """
    return {
        "status": "healthy",
        "service": "AI Pregnancy Companion API"
    }


@app.get("/api/status")
async def status():
    """
    Check API and integrations status
    """
    try:
        validate_environment()
        return {
            "api": "running",
            "voice_integration": "ready",
            "environment": "configured"
        }
    except Exception as e:
        return {
            "api": "running",
            "voice_integration": "error",
            "error": str(e)
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)