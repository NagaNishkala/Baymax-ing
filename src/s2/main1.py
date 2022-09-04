#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import Header
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped,Pose,Point,Quaternion,Twist
from tf.transformations import euler_from_quaternion
global pose12
import time
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

def getdist(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

x1,y1,z1=0,0,0
def odom_callback(data):
    global x1,y1,z1
    x1 = data.pose.pose.position.x
    y1 = data.pose.pose.position.y
    z1 = data.pose.pose.position.z

    #global x1, y1, z1, w1
    x1 = data.pose.pose.position.x
    y1 = data.pose.pose.position.y
    z1 = data.pose.pose.orientation.z
    w1 = data.pose.pose.orientation.w

    # pose12 = [data.pose.pose.position.x, data.pose.pose.position.y, euler_from_quaternion([x,y,z,w])[2]]

rospy.init_node('move_base_sequence')

pub1 = rospy.Publisher('/ateks0/cmd_vel', Twist, queue_size=10)#Declaring the node to be a publisher, publishing the message of type 'Twist' of the geometry_msg, of the topic '/cmd_vel'
pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)#Declaring the node to be a publisher, publishing the message of type 'Twist' of the geometry_msg, of the topic '/cmd_vel'
rospy.Subscriber('/ateks0/odom', Odometry, odom_callback)#Declaring the node to be a subscriber, subscribing to a message of type 'Odometry' of nav_msg, of the topic '/odom'
rate = rospy.Rate(5)

Flag_greet=True
shutdown_1=False

Flag = True
i=0

velocity_msg = Twist()#message of type 'Twist' of geometry_msg
velocity_msg.linear.x = 0.0
velocity_msg.angular.z = 0
pub1.publish(velocity_msg)

rospy.sleep(1)
points = [[3, 0,0],[5, 2,0],[6, 3,0]]
velocity_msg.linear.x = 0.0
velocity_msg.angular.z = 0
pub1.publish(velocity_msg)

json_name='hiro_profile.json'
f=open(json_name)
data=json.load(f)
name=data['Name']
f.close()

flatten_list=load_data(json_name)
print(flatten_list)

x,y=x1,y1

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

        if a[0] is None:
            pass
        else:
            x,y,z=a.split(",")
            x=float(x)
            y=float(y)
            print(type(x1))

    if now in flatten_list:
        print('medicine time')
        index=[i for i,val in enumerate(flatten_list) if val==now]
        for i in index:
            print('Take medicine',flatten_list[i-1])

    if shutdown_1:
        break

    poseStamped1=PoseStamped()
    poseStamped1.header.stamp=rospy.Time.now()
    poseStamped1.header.frame_id="map0"
    poseStamped1.pose.position.x=x
    poseStamped1.pose.position.y=y
    poseStamped1.pose.position.z=0
    poseStamped1.pose.orientation.x=0
    poseStamped1.pose.orientation.y=0
    poseStamped1.pose.orientation.z=0
    poseStamped1.pose.orientation.w=1

    if Flag:
        pub.publish(poseStamped1)
        Flag = False 

    dist=getdist(x,y,x1,y1)
    print('At i:',i,'dist to',x1,y1,':',dist,'\n')

    if(dist<=0.3):
        Flag = True

    rate.sleep()

#['Hi baymax, what is the time?','Hi baymax, what is the date?','Hi how are you doing?','Hi baymax, can you play a song?']
