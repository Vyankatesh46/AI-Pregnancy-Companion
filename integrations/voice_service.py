"""
Voice Integration Service - Local Whisper Version (FREE)
Person 5: Voice + Integrations + DevOps
"""

import os
import whisper
from typing import Dict

# Load Whisper model (loads once)
model = whisper.load_model("tiny") 
# Options: tiny, base, small, medium, large
# For hackathon: use "base" (balanced speed & accuracy)


def transcribe_audio(file_path: str) -> str:
    """
    Transcribe audio file using Local Whisper model
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    try:
        result = model.transcribe(file_path, language="en")
        return result["text"]

    except Exception as e:
        raise Exception(f"Local Whisper transcription failed: {str(e)}")


def send_text_to_ml(text: str, ml_module) -> Dict:
    if not text or not isinstance(text, str):
        raise ValueError("Text must be a non-empty string")

    try:
        result = ml_module.process_voice_text(text)
        return result

    except Exception as e:
        raise Exception(f"ML processing failed: {str(e)}")


def process_voice_input(file_path: str, ml_module) -> Dict:
    transcribed_text = transcribe_audio(file_path)
    result = send_text_to_ml(transcribed_text, ml_module)
    return result