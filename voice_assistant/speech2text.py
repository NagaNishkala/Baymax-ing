import pyttsx3
import datetime
import json
from itertools import chain
import speech_recognition as sr

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-50)
    engine.say(command)
    engine.runAndWait()

def HearMe():
    try:
        with sr.Microphone() as source2:
            print('Speak')
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2,10,5)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            #print("Did you say "+MyText)
            #SpeakText(MyText)
            return MyText

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return 'request not processed'

    except sr.UnknownValueError:
        print("unknown error occured")
        SpeakText("I am unable to process the sentence, please repeat")
        return 'please repeat'
