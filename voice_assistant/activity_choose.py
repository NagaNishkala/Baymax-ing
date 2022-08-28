import datetime
import json
from gtts import gTTS
import os
from playsound import playsound
from text2speech import *

def activity_choose(i):
    if 'time' in i:
        print(i)
        now = datetime.datetime.now().strftime('%H:%M:%S')
        str1='The time is '+now
        print(str1)
        say_it(str1)
        print()
    elif 'date' in i:
        print(i)
        now = datetime.datetime.now().strftime('%c')
        date_str = now.split(' ')
        print(date_str)
        str1='The date is '+date_str[1]+' '+date_str[2]+' '+date_str[4]
        print(str1)
        say_it(str1)
        print()
    elif 'day' in i:
        print(i)
        now = datetime.datetime.now().strftime('%c')
        date_str = now.split(' ')
        str1='Today is '+date_str[0]
        print(str1)
        say_it(str1)
        print()
    elif 'song' in i and 'play' in i:
        print(i)
        str1='I will play a song'
        print(str1)
        say_it(str1)
        playsound("vdomusic.mp3")
        print()
    elif 'how are you' in i:
        print(i)
        str1='I am good'
        print(str1)
        say_it(str1)
        print()