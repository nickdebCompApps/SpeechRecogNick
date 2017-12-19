import speech_recognition as sr
import speak
from time import ctime
import time
import sys
r = sr.Recognizer()
lang = 'en'
data = ''
# Enable Microphone and use for audio input

# Speech recognition using Google Speech Recognition

def spk(text, lang):
    speak.tts(text, lang)

def audioRecord():

    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        
    data = r.recognize_google(audio)
    print('You said ' + data)

    # speak.tts(data, lang)

    return data

def brain(data):
    if "how are you" in data:
        spk("I am fine", lang)
 
    if "what time is it" in data:
        spk(ctime(), lang)

    if "where am I" in data:
        spk('Ellington', lang)
        
    if "nothing" in data:
        spk('okay', lang)
        sys.exit()


# initialization
spk('hello nick, what can I do for you today', lang)
while 1:
    data = audioRecord()
    brain(data)
