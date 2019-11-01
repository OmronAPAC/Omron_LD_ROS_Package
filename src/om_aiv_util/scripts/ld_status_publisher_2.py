#!/usr/bin/env python
## publishes std_msgs/Strings messages
## to the 5 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
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
from socketconnection_class2 import ConnectSocket, connecttcp
s = connecttcp.sock

def extended_status_for_humans():
    pub = rospy.Publisher('robot2/ldarcl_status_extended_status_for_humans', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print(Fore.YELLOW)
    print(Style.BRIGHT)
    print "Getting extended_status_for_humans..."
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while not rospy.is_shutdown():
        if "ExtendedStatusForHumans" in rcv:
            break
        else:
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

    # for line in data.splitlines():
    #     if 'ExtendedStatusForHumans' in line:
    #         extended_status_for_humans = line.split()[-1]
    #
    # rospy.loginfo(extended_status_for_humans)

    for line in data.splitlines():
        if 'ExtendedStatusForHumans' in line:
            extended_status_for_humans = line.split("ExtendedStatusForHumans:")
    rospy.loginfo(",ExtendedStatusForHumans:".join(extended_status_for_humans)[1:])

    pub.publish(''.join(extended_status_for_humans))
    rate.sleep()

def status():
    pub = rospy.Publisher('robot2/ldarcl_status_status', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print "Getting status..."
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while not rospy.is_shutdown():
        if "Status:" in rcv:
            break
        else:
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

    # for line in data.splitlines():
    #     if 'DockingState:' in line:
    #         Status1 = line.split()[-6], line.split()[-5]
    # rospy.loginfo(Status1)
    #
    # for line in data.splitlines():
    #     if 'ForcedState' in line:
    #         Status2 = line.split()[-4], line.split()[-3]
    # rospy.loginfo(Status2)
    #
    # for line in data.splitlines():
    #     if 'ChargeState' in line:
    #         Status3 = line.split()[-2], line.split()[-1]
    # rospy.loginfo(Status3)
    #
    # pub.publish(''.join(Status1))
    # pub.publish(''.join(Status2))
    # pub.publish(''.join(Status3))

    for line in data.splitlines():
        if 'Status:' in line:
            status = line.split("Status:")
    rospy.loginfo(",Status:".join(status)[1:])
    pub.publish(''.join(status))
    rate.sleep()

def state_of_charge():
    pub = rospy.Publisher('robot2/ldarcl_status_state_of_charge', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print(Fore.RED)
    print(Style.BRIGHT)
    print "Getting state_of_charge..."
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while not rospy.is_shutdown():
        if "StateOfCharge" in rcv:
            break
        else:
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

    for line in data.splitlines():
        if 'StateOfCharge' in line:
            state_of_charge = line.split()[-1]

    rospy.loginfo(state_of_charge)
    pub.publish(state_of_charge)
    rate.sleep()

def location():
    pub = rospy.Publisher('robot2/ldarcl_status_location', Location, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg = Location()
    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print(Fore.MAGENTA)
    print(Style.BRIGHT)
    print "Getting location..."
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")

    while not rospy.is_shutdown():
        if "Location" in rcv:
            break
        else:
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

    # for line in data.splitlines():
    #     if 'Location' in line:
    #         location = line.split()[-3], line.split()[-2], line.split()[-1]

    for line in data.splitlines():
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

    rospy.loginfo(msg)
    pub.publish(msg)
    # pub.publish(''.join(locationx))
    # pub.publish(''.join(locationy))
    # pub.publish(''.join(locationz))
    rate.sleep()

def localization_score():
    pub = rospy.Publisher('robot2/ldarcl_status_localization_score', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print(Fore.BLUE)
    print(Style.BRIGHT)
    print "Getting localization_score..."
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while not rospy.is_shutdown():
        if "LocalizationScore" in rcv:
            break
        else:
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

    for line in data.splitlines():
        if 'LocalizationScore' in line:
            localization_score = line.split()[-1]

    rospy.loginfo(localization_score)
    pub.publish(localization_score)
    rate.sleep()

def temperature():
    pub = rospy.Publisher('robot2/ldarcl_status_temperature', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting temperature..."
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while not rospy.is_shutdown():
        if "Temperature" in rcv:
            break
        else:
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")

    for line in data.splitlines():
        if 'Temperature' in line:
            temperature = line.split()[-1]

    rospy.loginfo(temperature)
    pub.publish(temperature)
    rate.sleep()

if __name__ == '__main__':
    try:
        # extended_status_for_humans()
        # status()
        # state_of_charge()
        # location()
        # localization_score()
        # temperature()
        while not rospy.is_shutdown():
            extended_status_for_humans()
            status()
            state_of_charge()
            location()
            localization_score()
            temperature()
    except rospy.ROSInterruptException:
        pass
