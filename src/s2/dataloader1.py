import json
import pyttsx3
import datetime
from itertools import chain

def load_data(json_name):
    f=open(json_name)
    data=json.load(f)

    time_list=[]

    for med in data['Medicines']:
        now = datetime.datetime.now()
        time1 = data['Medicines'][med]['Time']

        baf = data['Medicines'][med]['BAF']

        bh,bm = data['Breakfast'].split(':')
        lh,lm = data['Lunch'].split(':')
        dh,dm = data['Dinner'].split(':')

        breakfast = datetime.datetime(2009,12,12,int(bh),int(bm),00,00).time()
        breakfast_A = breakfast.strftime('%H:%M:%S')
        lunch = datetime.datetime(2009,12,12,int(lh),int(lm),00,00).time()
        lunch_A = lunch.strftime('%H:%M:%S')
        dinner = datetime.datetime(2009,12,12,int(dh), int(dm),00,00).time()
        dinner_A = dinner.strftime('%H:%M:%S')

        breakfast1 = datetime.datetime(2009,12,12,int(bh)-1,int(bm),00,00).time()
        breakfast_B = breakfast1.strftime('%H:%M:%S')
        lunch1 = datetime.datetime(2009,12,12,int(lh)-1,int(lm),00,00).time()
        lunch_B = lunch1.strftime('%H:%M:%S')
        dinner1 = datetime.datetime(2009,12,12,int(dh)-1, int(dm),00,00).time()
        dinner_B = dinner1.strftime('%H:%M:%S')
        
        if baf=='A':
            if time1=='BLD':
                #print(med,' BLD ',data['Medicines'][med]['Time'])
                time_list.append((med,breakfast_A))
                time_list.append((med,lunch_A))
                time_list.append((med,dinner_A))
            elif time1=='BD':
                #print(med,' BD ',data['Medicines'][med]['Time'])
                time_list.append((med,breakfast_A))
                time_list.append((med,dinner_A))
            else:
                #print(med,' Hour:',time1.split(':')[0]," Min:",time1.split(':')[1])
                h=int(time1.split(':')[0])
                m=int(time1.split(':')[1])
                t=datetime.datetime(2009,12,12,h,m,00,00)
                t_A=t.strftime('%H:%M:%S')
                time_list.append((med,t_A))
        
        elif baf=='B':
            if time1=='BLD':
                #print(med,' BLD ',data['Medicines'][med]['Time'])
                time_list.append((med,breakfast_B))
                time_list.append((med,lunch_B))
                time_list.append((med,dinner_B))
            elif time1=='BD':
                #print(med,' BD ',data['Medicines'][med]['Time'])
                time_list.append((med,breakfast_B))
                time_list.append((med,dinner_B))
            else:
                #print(med,' Hour:',time1.split(':')[0]," Min:",time1.split(':')[1])
                h=int(time1.split(':')[0])-1
                m=int(time1.split(':')[1])
                t=datetime.datetime(2009,12,12,h,m,00,00).time()
                t_B=t.strftime('%H:%M:%S')
                time_list.append((med,t_B))
    
    flatten_list = list(chain.from_iterable(time_list))
    return flatten_list