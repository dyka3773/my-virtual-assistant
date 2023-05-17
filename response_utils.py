import time

import speech_utils as su
import action_utils as au

def there_exists(terms: list, voice_data: str) -> bool:
    """Checks if any of the terms are in the voice data.

    Args:
        terms (list): A list of terms to check for.
        voice_data (str): The message recorded from the microphone.

    Returns:
        bool: True if any of the terms are in the voice data, False otherwise.
    """
    for term in terms:
        if term in voice_data:
            return True

def respond(voice_data: str):
    if there_exists(["what is your name", "what's your name", "tell me your name"], voice_data):
        su.speak("My name is Jarvis")
    
    if there_exists(["what is the time", "what's the time", "tell me the time"], voice_data):
        su.speak(time.strftime("%H:%M"))    
    
    if there_exists(["what is the date", "what's the date", "tell me the date"], voice_data):
        su.speak(time.strftime("%A, %d %B %Y"))
    
    if there_exists(["search for", "google"], voice_data):
        search_term = voice_data.split("for")[-1] if "for" in voice_data else voice_data.split("google")[-1]
        url = f"https://google.com/search?q={search_term}"
        su.speak(f"Here is what I found for '{search_term}' on google")
        au.open_url(url)
    
    if there_exists(["youtube", "find videos for"], voice_data):
        search_term = voice_data.split("for")[-1] if "for" in voice_data else voice_data.split("youtube")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        search_term = search_term.strip()
        su.speak(f"Here is what I found for '{search_term}' on youtube")
        au.open_url(url)
    
    if there_exists(["what is the weather", "what's the weather", "show me the weather"], voice_data):
        if "weather in" in voice_data:
            city = voice_data.split("in")[-1]
            url = f"https://www.google.com/search?q=weather+in+{city}"
            su.speak(f"Here is the weather in {city} according to google")
            au.open_url(url)
        else:
            url = f"https://www.google.com/search?q=weather"
            su.speak("Here is the weather according to google")
            au.open_url(url)
    
    if there_exists(["take a note", "write this down"], voice_data):
        note = voice_data.split("note")[-1] if "note" in voice_data else voice_data.split("down")[-1]
        au.write_note(note)
        su.speak("I've made a note of that")
        
    
    if there_exists(["bye", "goodbye", "exit", "quit", "stop"], voice_data):
        su.speak("Goodbye")
        exit()