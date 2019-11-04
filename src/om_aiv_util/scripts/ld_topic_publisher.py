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
    applicationFaultQuery = data.encode('ascii', 'ignore')
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
    faultsGet = data.encode('ascii', 'ignore')
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
    getDateTime = data.encode('ascii', 'ignore')
    rospy.loginfo(getDateTime)
    pub.publish(str(getDateTime.splitlines()))
    rate.sleep()

def getGoals():
    pub = rospy.Publisher('ldarcl_getGoals', String, queue_size=10)
    rospy.init_node('ld_getGoals', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of goals found in current map..."
    command = "getGoals"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    getGoals = data.encode('ascii', 'ignore')
    rospy.loginfo(getGoals)
    pub.publish(str(getGoals.splitlines()))
    rate.sleep()

# def getInfoList():
#     pub = rospy.Publisher('ldarcl_getIn', String, queue_size=10)
#     rospy.init_node('ld_getGoals', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     print(Style.RESET_ALL)
#     print(Fore.GREEN)
#     print "Getting list infomation names..."
#     command = "getInfoList"
#     command = command.encode('ascii')
#     s.send(command+b"\r\n")
#     global rcv
#     data = s.recv(BUFFER_SIZE)
#     time.sleep(1)
#     getGoals = data.encode('ascii', 'ignore')
#     rospy.loginfo(getGoals)
#     pub.publish(str(getGoals.splitlines()))
#     rate.sleep()



def getMacros():
    pub = rospy.Publisher('ldarcl_getMacros', String, queue_size=10)
    rospy.init_node('ld_getMacros', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of macros found in current map..."
    command = "getMacros"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    getMacros = data.encode('ascii', 'ignore')
    rospy.loginfo(getMacros)
    pub.publish(str(getMacros.splitlines()))
    rate.sleep()

def getRoutes():
    pub = rospy.Publisher('ldarcl_getRoutes', String, queue_size=10)
    rospy.init_node('ld_getRoutes', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of route names found in current map..."
    command = "getRoutes"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    getRoutes = data.encode('ascii', 'ignore')
    rospy.loginfo(getRoutes)
    pub.publish(str(getRoutes.splitlines()))
    rate.sleep()

def geInputQuery():
    pub = rospy.Publisher('ldarcl_getRoutes', String, queue_size=10)
    rospy.init_node('ld_getRoutes', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of route names found in current map..."
    command = "getRoutes"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    getRoutes = data.encode('ascii', 'ignore')
    rospy.loginfo(getRoutes)
    pub.publish(str(getRoutes.splitlines()))
    rate.sleep()



if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            # applicationFaultQuery()
            # faultsGet()
            # getDateTime()
            # getGoals()
            # getMacros()
            getRoutes()

    except rospy.ROSInterruptException:
        pass
