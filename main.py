import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)
logger = logging.getLogger(__name__)

from response_utils import respond
from speech_utils import speak
from recording import record_audio

            
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
    