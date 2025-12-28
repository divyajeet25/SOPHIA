from playsound import playsound
import eel
def playAssistantSound():
    music_dir = "www\\assets\\audio\\sound-effect-13362.mp3"
    playsound(music_dir)
@eel.expose
def playClickSound():
    music_dir = "www\\assets\\audio\\mixkit-sci-fi-click-900.wav"
    playsound(music_dir)    