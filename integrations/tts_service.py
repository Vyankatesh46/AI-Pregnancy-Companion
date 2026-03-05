import pyttsx3

def text_to_speech(text: str):
    """
    Convert text output into speech
    """

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()