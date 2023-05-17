import speech_recognition as sr
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)
logger = logging.getLogger(__name__)

from response_utils import respond
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
            
def main():
    speak("Hello, I am your personal assistant")
    speak("How can I help you?")
    while True:
        voice_data = record_audio()
        if voice_data:
            speak(voice_data,actor="You")
            respond(voice_data)
  
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.error("|| User - Keyboard Interrupt ||")
    