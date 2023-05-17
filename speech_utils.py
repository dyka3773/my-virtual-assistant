import logging
# from playsound import playsound
import winsound
import os
# import pyttsx3

import tts_transformer

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)

logger = logging.getLogger(__name__)

def assistant_speak(audio: str, voice: int = 2271):
    """Speaks the given audio.

    Args:
        audio (str): The audio to be spoken.
        voice (int, optional): The voice to use. Defaults to 2271 (US female).
    """
    
    # speaker ids from the embeddings dataset
    
    # speakers = {
    #     'awb': 0,     # Scottish male
    #     'bdl': 1138,  # US male
    #     'clb': 2271,  # US female
    #     'jmk': 3403,  # Canadian male
    #     'ksp': 4535,  # Indian male
    #     'rms': 5667,  # US male
    #     'slt': 6799   # US female
    # }
    
    file_name = tts_transformer.save_text_to_speech(audio, speaker=voice)
    
    winsound.PlaySound(file_name, winsound.SND_FILENAME)
    

def speak(message: str, actor: str = "Assistant", errlevel: str = "info"):
    """Prints the given message with the given actor and also logs it to the app.log file with the given error level.

    Args:
        message (str): The message to be printed and logged.
        actor (str, optional): The actor that speaks. Defaults to "Assistant".
        errlevel (str, optional): This dictates whether there has been an error when recognizing speech. Defaults to "info".
    """
    logger.info(f"|| {actor} - {message} ||") if errlevel == "info" else logger.error(f"|| {actor} - {message} ||")
    print(f"{actor}: {message}")
    if actor == "Assistant":
        assistant_speak(message)
        