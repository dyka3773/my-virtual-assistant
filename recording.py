import speech_recognition as sr
from speech_utils import speak

r = sr.Recognizer()

def record_audio(ask: str = None) -> str:
    """Records audio from the microphone and returns the recognized speech.

    Args:
        ask (str, optional): The message to be printed before recording audio. Defaults to None.
    
    Returns:
        str: The message that was recognized from the audio.
    """
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that", errlevel="error")
        except sr.RequestError:
            speak("Sorry, my speech service is down", errlevel="error")
        
        return voice_data.lower()