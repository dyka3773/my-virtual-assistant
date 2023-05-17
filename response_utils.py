import time
import pyjokes
import wikipedia

import speech_utils as su
import action_utils as au
import recording as rec

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
        au.open_url(url)
        su.speak(f"Here is what I found for '{search_term}' on google")
    
    if there_exists(["youtube", "find videos for"], voice_data):
        search_term = voice_data.split("for")[-1] if "for" in voice_data else voice_data.split("youtube")[-1]
        url = f"https://www.youtube.com/results?search_query={search_term}"
        search_term = search_term.strip()
        au.open_url(url)
        su.speak(f"Here is what I found for '{search_term}' on youtube")
    
    if there_exists(["what is the weather", "what's the weather", "show me the weather"], voice_data):
        if "weather in" in voice_data:
            city = voice_data.split("in")[-1]
            url = f"https://www.google.com/search?q=weather+in+{city}"
            au.open_url(url)
            su.speak(f"Here is the weather in {city} according to google")
        else:
            url = f"https://www.google.com/search?q=weather"
            au.open_url(url)
            su.speak("Here is the weather according to google")
    
    if there_exists(["take a note", "write this down", "remember this"], voice_data):
        note = rec.record_audio("What would you like me to write down?")
        au.write_note(note)
        su.speak("I've made a note of that")
    
    if there_exists(["tell a joke", "tell me a joke"], voice_data):
        answer = "yes"
        while answer == "yes":
            su.speak(pyjokes.get_joke())
            answer = rec.record_audio("Would you like to hear another joke?")
            su.speak(answer, actor="You")
        su.speak("OK, I'll stop telling jokes")
        su.speak("How can I help you?")
        
    if there_exists(["who is", "what is", "what's the definition of"], voice_data):
        search_term = voice_data.split("is")[-1] if "is" in voice_data else voice_data.split("of")[-1]
        try:
            su.speak(wikipedia.summary(search_term, sentences=2))
        except:
            su.speak("I don't know that")
    
    if there_exists(["bye", "goodbye", "exit", "quit", "stop"], voice_data):
        su.speak("Goodbye")
        au.delete_all_data()
        exit()
        
    if there_exists(["delete notes", "delete my notes"], voice_data):
        au.delete_notes()
        su.speak("I've deleted all of your notes")
        
    if there_exists(["delete all data", "delete my data"], voice_data):
        au.delete_all_data()
        su.speak("I've deleted all of your data")
        
    if there_exists(["deactivate assistant"], voice_data):
        su.speak("OK, I'll be here if you need me. In order to activate me again, say 'Activate Assistant'")
        return True
    
def activate_assistant():
    su.speak("Hello, I am your personal assistant")
    su.speak("How can I help you?")
    while True:
        voice_data = rec.record_audio()
        if voice_data:
            su.speak(voice_data,actor="You")
            if respond(voice_data):
                break