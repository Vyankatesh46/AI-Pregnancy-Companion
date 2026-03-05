from integrations.audio_handler import process_voice_input

def process_voice_pipeline(audio_path, ml_module):
    """
    Complete voice processing pipeline

    Audio → Whisper → Text → ML Processing
    """

    # Step 1: Convert audio to text
    text_data = process_voice_input(audio_path)

    transcription = text_data["transcription"]

    # Step 2: Send text to ML model
    result = ml_module.process_voice_text(transcription)

    return {
        "transcription": transcription,
        "ml_result": result
    }