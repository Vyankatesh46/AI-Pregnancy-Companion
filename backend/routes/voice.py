from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os

from integrations.voice_service import transcribe_audio
from integrations.tts_service import text_to_speech
import ml_engine.mood_model as mood_model

router = APIRouter()


@router.post("/voice/transcribe")
async def transcribe_voice(audio_file: UploadFile = File(...)):

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        content = await audio_file.read()
        tmp.write(content)
        tmp_path = tmp.name

    text = transcribe_audio(tmp_path)

    os.unlink(tmp_path)

    return {
        "transcription": text
    }


@router.post("/voice/process")
async def process_voice(audio_file: UploadFile = File(...)):

    try:
        # save audio
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            content = await audio_file.read()
            tmp.write(content)
            tmp_path = tmp.name

        # Step 1 — Whisper transcription
        transcription = transcribe_audio(tmp_path)

        # Step 2 — ML prediction
        try:
            ml_result = mood_model.predict_mood_risk([1,1,1,1,1], 7)
        except Exception as ml_error:
            print("ML ERROR:", ml_error)
            ml_result = {
                "status": "ML model not ready",
                "message": str(ml_error)
            }

        # Step 3 — Generate voice response
        response_text = f"Your mood risk level is {ml_result.get('risk_level', 'unknown')}"

        audio_response = text_to_speech(response_text)

        os.unlink(tmp_path)

        return {
            "transcription": transcription,
            "ml_result": ml_result,
            "audio_response_file": audio_response
        }

    except Exception as e:
        print("VOICE PROCESS ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))