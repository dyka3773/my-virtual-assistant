import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)

logger = logging.getLogger(__name__)

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
        
def assistant_speak(audio):
    pass