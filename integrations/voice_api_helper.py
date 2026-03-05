# integrations/voice_api_helper.py
from integrations.audio_handler import process_voice_input

def handle_voice_file(audio_path):
    result = process_voice_input(audio_path)
    return result