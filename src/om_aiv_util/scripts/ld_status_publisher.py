#!/usr/bin/env python
## publishes std_msgs messages to the 6 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from om_aiv_util.msg import Location
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 2056
#import socketconnection class to connect to robot
#requires socketconnection_class.py file in the same folder
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
#get ip address and port from launch file
# ip_address = rospy.get_param("ip_address")
# port = rospy.get_param("port")

ip_address = "168.3.201.123"
port = 7171

connecttcp.connect(str(ip_address), port)
rospy.init_node('ld_status', anonymous=True)

def sendcommand():
    #send status command
    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    data2 = s.recv(BUFFER_SIZE)
    time.sleep(1)
    rcv = data.decode("utf-8") + data2.decode("utf-8")
    print rcv

def extended_status_for_humans():
    pub = rospy.Publisher('ldarcl_status_extended_status_for_humans', String, queue_size=10)
    #  # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting extended_status_for_humans..."
    #extract required status
    for line in rcv.splitlines():
        if 'ExtendedStatusForHumans' in line:
            extended_status_for_humans = line.split("ExtendedStatusForHumans:")
    #print required status
    rospy.loginfo(",ExtendedStatusForHumans:".join(extended_status_for_humans)[1:])
    #publish required status
    pub.publish(''.join(extended_status_for_humans))
    #

def status():
    pub = rospy.Publisher('ldarcl_status_status', String, queue_size=10)
     # 10hz

    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print "Getting status..."

    for line in rcv.splitlines():
        if 'Status:' in line:
            status = line.split("Status:")
            rospy.loginfo(status)
            pub.publish(''.join(status))

        else:
            pass


def state_of_charge():
    pub = rospy.Publisher('ldarcl_status_state_of_charge', Float32, queue_size=10)
     # 10hz

    print(Style.RESET_ALL)
    print(Fore.RED)
    print(Style.BRIGHT)
    print "Getting state_of_charge..."

    for line in rcv.splitlines():
        if 'StateOfCharge' in line:
            state_of_charge = line.split()[-1]

            rospy.loginfo(state_of_charge)
            pub.publish(float(state_of_charge))

        else:
            pass

def location():
    pub = rospy.Publisher('ldarcl_status_location', Location, queue_size=10)
     # 10hz
    msg = Location()

    print(Style.RESET_ALL)
    print(Fore.MAGENTA)
    print(Style.BRIGHT)
    print "Getting location..."
    for line in rcv.splitlines():
        if 'Location' in line:
            locationx = line.split()[-3]
            locationy = line.split()[-2]
            locationtheta = line.split()[-1]
            PI = 3.1415926535897
            relative_angle = float(locationtheta)*180/PI
            # print relative_angle
            msg.x = float(locationx)
            msg.y = float(locationy)
            msg.theta = float(locationtheta)
            # print locationz
            # print .rad2deg(-2)
        else:
            pass


    rospy.loginfo(msg)
    pub.publish(msg)
    # pub.publish(''.join(locationx))
    # pub.publish(''.join(locationy))
    # pub.publish(''.join(locationz))


def localization_score():
    pub = rospy.Publisher('ldarcl_status_localization_score', Float32, queue_size=10)
     # 10hz
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print "Getting localization_score..."
    for line in rcv.splitlines():
        if 'LocalizationScore' in line:
            localization_score = line.split()[-1]
            rospy.loginfo(localization_score)
            pub.publish(float(localization_score))

        else:
            pass



def temperature():
    pub = rospy.Publisher('ldarcl_status_temperature', Float32, queue_size=10)
     # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting temperature..."
    for line in rcv.splitlines():
        if 'Temperature' in line:
            temperature = line.split()[-1]
            rospy.loginfo(temperature)
            pub.publish(float(temperature))

        else:
            pass



if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            sendcommand()
            extended_status_for_humans()
            status()
            state_of_charge()
            location()
            localization_score()
            temperature()
    except rospy.ROSInterruptException:
        pass
