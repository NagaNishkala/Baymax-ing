import datetime
import json
from gtts import gTTS
import os
from playsound import playsound
from text2speech import *

def activity_choose(i,json_name_profile):
    json_name='locations_set.json'
    f=open(json_name)
    data=json.load(f)
    f.close()

    f1=open(json_name_profile)
    data1=json.load(f1)
    f1.close()    

    f2=open('doctor_status.json')
    data2=json.load(f2)
    f2.close()

    if 'time' in i:
        print(i)
        now = datetime.datetime.now().strftime('%H:%M:%S')
        str1='The time is '+now
        print(str1)
        say_it(str1)
        print()
        return [None]
    elif 'date' in i:
        print(i)
        now = datetime.datetime.now().strftime('%c')
        date_str = now.split(' ')
        print(date_str)
        str1='The date is '+date_str[1]+' '+date_str[2]+' '+date_str[4]
        print(str1)
        say_it(str1)
        print()
        return [None]
    elif 'day' in i:
        print(i)
        now = datetime.datetime.now().strftime('%c')
        date_str = now.split(' ')
        str1='Today is '+date_str[0]
        print(str1)
        say_it(str1)
        print()
        return [None]
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
        return [None]
    elif 'who are you' in i:
        print(i)
        str1='Hi I am Bay max'
        print(str1)
        say_it(str1)
        print()
        return [None]
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
    elif 'take me' in i:
        if 'cafe' in i or 'restaurant' in i:
            print('Going to cafeteria')
            a1=data['Cafeteria']
            return a1
        elif 'my room' in i:
            print('Going to ward')
            wardno=data1['Ward']
            a1=data['Ward'][wardno]
            return a1
        elif 'washroom' in i or 'restroom' in i:
            print('Going to washroom')
            wardno="Ward"+data1['Ward']
            a1=data['Washroom'][wardno]
            return a1
        elif 'doctor' in i:
            print('Going to doctor cabin')
            doc1=data1['Doctor1']
            doc2=data1['Doctor2']
            doc1_stat=data2[doc1]
            doc2_stat=data2[doc2]
            print('doc1:',doc1,doc1_stat)
            print('doc2:',doc2,doc2_stat)
            if doc1_stat=='Free':
                return data['Cabin'][doc1]
            elif doc2_stat=='Free':
                return data['Cabin'][doc2]
            else:
                print('Doctors busy, calling nurse')
                return [None]