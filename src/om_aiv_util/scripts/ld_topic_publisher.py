#!/usr/bin/env python
## publishes std_msgs/Strings messages
## to the 5 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from om_aiv_util.msg import Location
# from turtlesim.msg import Pose
import math
import numpy as np
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 1024
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.123"
# port = 7171
connecttcp.connect(str(ip_address), port)

def applicationFaultQuery():
    pub = rospy.Publisher('ldarcl_status_extended_status_for_humans', String, queue_size=10)
    rospy.init_node('ld_applicationFaultSet', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of faults..."
    command = "applicationFaultQuery"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    applicationFaultQuery = data.decode("utf-8")
    rospy.loginfo(applicationFaultQuery)
    pub.publish(str(applicationFaultQuery.splitlines()))
    rate.sleep()

def status():
    pub = rospy.Publisher('ldarcl_status_status', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print "Getting status..."

    for line in rcv.splitlines():
        if 'Status:' in line:
            status = line.split()[-1]
            rospy.loginfo(status)
            pub.publish(status)
            rate.sleep()
        else:
            pass


def state_of_charge():
    pub = rospy.Publisher('ldarcl_status_state_of_charge', Float32, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    print(Style.RESET_ALL)
    print(Fore.RED)
    print(Style.BRIGHT)
    print "Getting state_of_charge..."

    for line in rcv.splitlines():
        if 'StateOfCharge' in line:
            state_of_charge = line.split()[-1]

            rospy.loginfo(state_of_charge)
            pub.publish(float(state_of_charge))
            rate.sleep()
        else:
            pass

def location():
    pub = rospy.Publisher('ldarcl_status_location', Location, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
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
            # print np.rad2deg(-2)
        else:
            pass


    rospy.loginfo(msg)
    pub.publish(msg)
    # pub.publish(''.join(locationx))
    # pub.publish(''.join(locationy))
    # pub.publish(''.join(locationz))
    rate.sleep()

def localization_score():
    pub = rospy.Publisher('ldarcl_status_localization_score', Float32, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print "Getting localization_score..."
    for line in rcv.splitlines():
        if 'LocalizationScore' in line:
            localization_score = line.split()[-1]
            rospy.loginfo(localization_score)
            pub.publish(float(localization_score))
            rate.sleep()
        else:
            pass



def temperature():
    pub = rospy.Publisher('ldarcl_status_temperature', Float32, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting temperature..."
    for line in rcv.splitlines():
        if 'Temperature' in line:
            temperature = line.split()[-1]
            rospy.loginfo(temperature)
            pub.publish(float(temperature))
            rate.sleep()
        else:
            pass



if __name__ == '__main__':
    try:
        # extended_status_for_humans()
        # status()
        # state_of_charge()
        # location()
        # localization_score()
        # temperature()
        while not rospy.is_shutdown():
            applicationFaultQuery()

    except rospy.ROSInterruptException:
        pass
