# test_voice.py
from integrations.voice_service import transcribe_audio

result = transcribe_audio(r"C:\AI_PREGNANCY_COMPANION\AI-Pregnancy-Companion\sample_01.ogg")
print(result)