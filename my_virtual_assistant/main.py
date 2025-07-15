import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)
logger = logging.getLogger(__name__)

from .action_utils import delete_all_data
from .recording import record_audio
from .response_utils import activate_assistant, there_exists
from .speech_utils import speak


def main():
    speak("Your personal assistant is ready")
    speak("In order to activate me, say 'Activate Assistant'")
    while True:
        voice_data = record_audio()
        if voice_data == "activate assistant":
            activate_assistant()
        elif there_exists(["quit", "exit", "stop"], voice_data):
            speak("Goodbye")
            delete_all_data()
            exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.error("|| User - Keyboard Interrupt ||")
    except Exception as e:
        logger.error(e)
    finally:
        delete_all_data()
