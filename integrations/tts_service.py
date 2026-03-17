import pyttsx3
import tempfile

engine = pyttsx3.init()

def text_to_speech(text: str):

    # create temporary audio file
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    audio_path = temp_audio.name

    # save audio
    engine.save_to_file(text, audio_path)

    # SPEAK the text
    engine.say(text)

    engine.runAndWait()

    return audio_path