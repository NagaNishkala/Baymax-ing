import pyttsx3
import datetime
import json
from itertools import chain
import speech_recognition as sr
from playsound import playsound

from text2speech import *
from speech2text import *
from dataloader1 import *
from activity_choose import *

Flag_greet=True
shutdown_1=False

json_name='hiro_profile.json'
f=open(json_name)
data=json.load(f)
name=data['Name']
f.close()

flatten_list=load_data(json_name)
print(flatten_list)

while not shutdown_1:
    now = datetime.datetime.now()
    now = now.strftime('%H:%M:%S')

    if Flag_greet:
        greetings(name)
        Flag_greet=False
        #shutdown_1=True
    else:
        str1=HearMe()
        print(str1)
        if 'stop' in str1:
            break
        a=activity_choose(str1,json_name)
        print(a)

    if now in flatten_list:
        print('medicine time')
        index=[i for i,val in enumerate(flatten_list) if val==now]
        for i in index:
            print('Take medicine',flatten_list[i-1])

    if shutdown_1:
        break

#['Hi baymax, what is the time?','Hi baymax, what is the date?','Hi how are you doing?','Hi baymax, can you play a song?']
