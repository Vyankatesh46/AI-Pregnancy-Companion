"""
Main FastAPI Application
Person 5: Voice + Integrations + DevOps
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from integrations import validate_environment, process_voice_input
from backend.routes.voice import router as voice_router

# Initialize FastAPI
app = FastAPI(
    title="AI Pregnancy Companion",
    description="Voice-enabled pregnancy support assistant",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voice_router, prefix="/api")
@app.on_event("startup")
async def startup_event():
    """Validate environment on startup"""
    try:
        validate_environment()
        print("✅ Environment validation passed")
    except EnvironmentError as e:
        print(f"❌ Environment validation failed: {e}")
        raise


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "AI Pregnancy Companion API"
    }


@app.post("/api/voice/transcribe")
async def transcribe_voice(audio_file: UploadFile = File(...)):
    """
    Transcribe audio file using Whisper
    
    Args:
        audio_file: Audio file (mp3, wav, m4a, etc.)
    
    Returns:
        Transcribed text
    """
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            content = await audio_file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # Import here to avoid circular imports
        from integrations import transcribe_audio
        
        # Transcribe
        transcribed_text = transcribe_audio(tmp_path)
        
        # Cleanup
        os.unlink(tmp_path)
        
        return {
            "status": "success",
            "transcription": transcribed_text
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/voice/process")
async def process_voice(audio_file: UploadFile = File(...)):
    """
    Full pipeline: Audio → Transcription → ML Processing
    
    Args:
        audio_file: Audio file for processing
    
    Returns:
        ML engine response
    """
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            content = await audio_file.read()
            tmp.write(content)
            tmp_path = tmp.name
        
        # Import ML module (to be implemented by ML person)
        try:
            from ml_engine import ml_model
        except ImportError:
            raise ImportError("ML engine not configured. Contact ML person.")
        
        # Process voice input
        result = process_voice_input(tmp_path, ml_model)
        
        # Cleanup
        os.unlink(tmp_path)
        
        return {
            "status": "success",
            "result": result
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/status")
async def status():
    """Check API and integrations status"""
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
    uvicorn.run(app, host="0.0.0.0", port=8000)
