from integrations.voice_service import transcribe_audio

def process_voice_input(audio_path):
    text = transcribe_audio(audio_path)

    return {
        "transcription": text
    }