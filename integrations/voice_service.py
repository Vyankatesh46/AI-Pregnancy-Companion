import whisper

# Load faster model for CPU
model = whisper.load_model("tiny")

def transcribe_audio(file_path: str):
    result = model.transcribe(
        file_path,
        language="en",     # force English
        task="transcribe"  # ensure transcription not translation
    )
    
    return result["text"].strip()