from fastapi import APIRouter, UploadFile, File
import shutil
import os

from integrations.audio_handler import process_voice_input
from ml_engine import ml_model

router = APIRouter()


@router.post("/voice/transcribe")
async def transcribe_voice(audio_file: UploadFile = File(...)):

    temp_path = f"temp_{audio_file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    result = process_voice_input(temp_path)

    os.remove(temp_path)

    return result



@router.post("/voice/process")
async def process_voice(audio_file: UploadFile = File(...)):

    temp_path = f"temp_{audio_file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    # Step 1: Transcribe
    voice_result = process_voice_input(temp_path)

    transcription = voice_result["transcription"]

    # Step 2: Send to ML
    ml_result = ml_model.process_voice_text(transcription)

    os.remove(temp_path)

    return {
        "transcription": transcription,
        "ml_result": ml_result
    }