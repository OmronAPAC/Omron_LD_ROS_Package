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
    pub = rospy.Publisher('ldarcl_applicationFaultQuery', String, queue_size=10)
    rospy.init_node('ld_applicationFaultQuery', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of application faults..."
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

def faultsGet():
    pub = rospy.Publisher('ldarcl_faultsGet', String, queue_size=10)
    rospy.init_node('ld_faultsGet', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of faults..."
    command = "faultsGet"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    faultsGet = data.decode("utf-8")
    rospy.loginfo(faultsGet)
    pub.publish(str(faultsGet.splitlines()))
    rate.sleep()


def getDateTime():
    pub = rospy.Publisher('ldarcl_getDateTime', String, queue_size=10)
    rospy.init_node('ld_getDateTime', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting date and time..."
    command = "getDateTime"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    getDateTime = data.decode("utf-8")
    rospy.loginfo(getDateTime)
    pub.publish(str(getDateTime.splitlines()))
    rate.sleep()

def location():
    pub = rospy.Publisher('ldarcl_getDateTime', String, queue_size=10)
    rospy.init_node('ld_getDateTime', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting date and time..."
    command = "getDateTime"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    getDateTime = data.decode("utf-8")
    rospy.loginfo(getDateTime)
    pub.publish(str(getDateTime.splitlines()))
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
        while not rospy.is_shutdown():
            # applicationFaultQuery()
            # faultsGet()
            getDateTime()

    except rospy.ROSInterruptException:
        pass
