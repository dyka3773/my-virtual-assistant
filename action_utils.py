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
    
def delete_notes():
    """Deletes the notes.txt file."""
    if os.path.exists(fr"%HOMEPATH%\Desktop\assistant_notes.txt"):
        os.system(fr"del %HOMEPATH%\Desktop\assistant_notes.txt")
    
def delete_all_data():
    """Deletes all data that the assistant has stored."""
    delete_notes()
    os.system(f"del output-*.wav")