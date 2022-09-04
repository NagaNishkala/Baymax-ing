#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import Header
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped,Pose,Point,Quaternion,Twist
from tf.transformations import euler_from_quaternion
global pose12
import time

def getdist(x1,y1,x2,y2):
    return math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))

def odom_callback(data):
    global x,y,z
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z

    global x1, y1, z1, w1
    x1 = data.pose.pose.position.x
    y1 = data.pose.pose.position.y
    z1 = data.pose.pose.orientation.z
    w1 = data.pose.pose.orientation.w

    # pose12 = [data.pose.pose.position.x, data.pose.pose.position.y, euler_from_quaternion([x,y,z,w])[2]]

rospy.init_node('move_base_sequence')

pub1 = rospy.Publisher('/cmd_vel', Twist, queue_size=10)#Declaring the node to be a publisher, publishing the message of type 'Twist' of the geometry_msg, of the topic '/cmd_vel'
pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)#Declaring the node to be a publisher, publishing the message of type 'Twist' of the geometry_msg, of the topic '/cmd_vel'
rospy.Subscriber('/lio_sam/mapping/odometry', Odometry, odom_callback)#Declaring the node to be a subscriber, subscribing to a message of type 'Odometry' of nav_msg, of the topic '/odom'
rate = rospy.Rate(5) 

print('Disconnect cables')
# time.sleep(40)
print('Moving')

velocity_msg = Twist()#message of type 'Twist' of geometry_msg
velocity_msg.linear.x = 0.0
velocity_msg.angular.z = 0
pub1.publish(velocity_msg)

rospy.sleep(1)
points = [[3, 0,0],[5, 2,0],[6, 3,0]]
velocity_msg.linear.x = 0.0
velocity_msg.angular.z = 0
pub1.publish(velocity_msg)

Flag = True
i=0

while not rospy.is_shutdown():
    
    x1=points[i][0]
    y1=points[i][1]
    poseStamped1=PoseStamped()
    poseStamped1.header.stamp=rospy.Time.now()
    poseStamped1.header.frame_id="map"
    poseStamped1.pose.position.x=x1
    poseStamped1.pose.position.y=y1
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
        i=i+1
        if(i==3):
            break

    rate.sleep()

print('Mission accomplished')