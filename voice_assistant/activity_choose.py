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
        str1='The date is '+date_str[1]+' '+date_str[3]+' '+date_str[5]
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
        str1='I will play the song'
        song1="vdomusic.mp3"
        if 'immortals' in i:
            str1='Playing immortals from big hero 6'
            song1="vdomusic1.mp3"
        print(str1)
        say_it(str1)
        playsound(song1)
        print()
    elif 'how are you' in i:
        print(i)
        str1='I am good'
        print(str1)
        say_it(str1)
        print()
    elif 'who are you' in i:
        print(i)
        str1='Hi I am Bay max, your healthcare companion'
        print(str1)
        say_it(str1)
        print()
    elif 'good morning' in i:
        print(i)
        str1='Good morning. Have a nice day'
        print(str1)
        say_it(str1)
        print()
    elif 'good afternoon' in i:
        print(i)
        str1='Good afternoon. Have a nice day'
        print(str1)
        say_it(str1)
        print()
    elif 'good evening' in i:
        print(i)
        str1='Good evening. Hope you had a nice day'
        print(str1)
        say_it(str1)
        print()
    elif 'good night' in i:
        print(i)
        str1='Good night. Sleep well.'
        print(str1)
        say_it(str1)
        print()