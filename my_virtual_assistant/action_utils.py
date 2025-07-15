import webbrowser
import os
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)

logger = logging.getLogger(__name__)

def open_url(url):
    """Opens a URL in the default browser.

    Args:
        url (str): The URL to open.
    """
    logger.info(f"Attempting to open {url}")
    webbrowser.open(url)
    logger.info(f"Successfully opened {url}")
    
def write_note(note: str):
    """Writes a note to the notes.txt file.
    
    Args:
        note (str): The note to write.
    """
    logger.info(f"Attempting to write '{note}' to notes.txt")
    os.system(f"echo {note} >> %HOMEPATH%/Desktop/assistant_notes.txt")
    logger.info(f"Successfully wrote to notes.txt")
    
def delete_notes():
    """Deletes the notes.txt file."""
    if os.path.exists(fr"%HOMEPATH%\Desktop\assistant_notes.txt"):
        logger.info("Attempting to delete notes.txt")
        os.system(fr"del %HOMEPATH%\Desktop\assistant_notes.txt")
        logger.info("Successfully deleted notes.txt")
    
def delete_all_data():
    """Deletes all data that the assistant has stored."""
    delete_notes()
    logger.info("Attempting to delete all output files")
    os.system(f"del output-*.wav")
    logger.info("Successfully deleted all output files")