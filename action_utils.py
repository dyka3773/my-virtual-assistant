import webbrowser
import os

def open_url(url):
    """Opens a URL in the default browser.

    Args:
        url (str): The URL to open.
    """
    webbrowser.open(url)
    
def write_note(note: str):
    """Writes a note to the notes.txt file.
    
    Args:
        note (str): The note to write.
    """
    os.system(f"echo {note} >> %HOMEPATH%/Desktop/assistant_notes.txt")
    