import pyttsx3
from pyttsx3 import engine
import speech_recognition as sr
import eel
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
  
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 150) # Change index to change voices
    engine.say(text)
    engine.runAndWait()
@eel.expose    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")  
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=10,phrase_time_limit=8)
    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        speak(query)
        eel.DisplayMessage(query)
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


#speak("Hello, I am Sophia, your personal assistant.")  
#text = takeCommand() 
#speak(text) 