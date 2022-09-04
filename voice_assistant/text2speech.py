import pyttsx3
import datetime
import json
from itertools import chain
import sys
import os

def say_it(str1):
    if sys.platform == 'win32':
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty('rate',rate-50)
        engine.say(str1)
        engine.runAndWait()

    elif sys.platform == 'Linux' or sys.platform == 'linux' or sys.platform == 'Ubuntu':
        tts_engine = 'espeak'
        print("Baymax: " + ' ' + str1 + '')
        return os.system(tts_engine + ' "' + str1 + '"')

def greetings(name):
    str1='Hello, I am Bay max, your personal healthcare companion.'
    say_it(str1)
    now = datetime.datetime.now()
    today12pm = datetime.datetime(2009,12,31,12,00,00,00)
    today4pm = datetime.datetime(2009,12,31,16,00,00,00)

    if now.time()<today12pm.time():
        say_it('Good morning,'+name)
    elif now.time()>=today12pm.time() and now.time()<today4pm.time():
        say_it('Good afternoon,'+name)
    elif now.time()>=today4pm.time():
        say_it('Good evening,'+name)
