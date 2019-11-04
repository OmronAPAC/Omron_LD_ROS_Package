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
BUFFER_SIZE = 2056
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.123"
# port = 7171
connecttcp.connect(str(ip_address), port)

def applicationFaultQuery():
    pub = rospy.Publisher('ldarcl_applicationFaultQuery', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of application faults..."
    command = "applicationFaultQuery"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    try:
        data = s.recv(BUFFER_SIZE)
        time.sleep(1)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "ApplicationFaultQuery:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                time.sleep(1)
                rcv = data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'ApplicationFaultQuery:' in line:
            applicationFaultQuery = line.split("ApplicationFaultQuery:")
            rospy.loginfo(",ApplicationFaultQuery:".join(applicationFaultQuery)[1:])
            pub.publish(''.join(applicationFaultQuery))
            rate.sleep()


def faultsGet():
    pub = rospy.Publisher('ldarcl_faultsGet', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.YELLOW)
    print "Getting list of faults..."
    command = "faultsGet"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    try:
        data = s.recv(BUFFER_SIZE)
        time.sleep(1)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "FaultList:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                time.sleep(1)
                rcv = data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'FaultList:' in line:
            faultsGet = line.split("FaultList:")
            rospy.loginfo(",FaultList:".join(faultsGet)[1:])
            pub.publish(''.join(faultsGet))
            rate.sleep()

def getDateTime():
    pub = rospy.Publisher('ldarcl_getDateTime', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting date and time..."
    command = "getDateTime"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    try:
        data = s.recv(BUFFER_SIZE)
        time.sleep(1)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            if "DateTime:" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                time.sleep(1)
                rcv = data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

    for line in rcv.splitlines():
        if 'DateTime:' in line:
            getDateTime = line.split("DateTime:")
            rospy.loginfo(",ApplicationFaultQuery:".join(getDateTime)[1:])
            pub.publish(''.join(getDateTime))
            rate.sleep()

def getGoals():
    pub = rospy.Publisher('ldarcl_getGoals', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
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
    rospy.init_node('ld_topic_publisher', anonymous=True)
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
    rospy.init_node('ld_topic_publisher', anonymous=True)
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

# def geInputQuery():
#     pub = rospy.Publisher('ldarcl_InputQuery', String, queue_size=10)
#     rospy.init_node('ld_InputQuery', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     print(Style.RESET_ALL)
#     print(Fore.GREEN)
#     print "Getting list of inputs..."
#     command = "InputQuery"
#     command = command.encode('ascii')
#     s.send(command+b"\r\n")
#     global rcv
#     data = s.recv(BUFFER_SIZE)
#     time.sleep(1)
#     InputQuery = data.encode('ascii', 'ignore')
#     rospy.loginfo(InputQuery)
#     pub.publish(str(InputQuery.splitlines()))
#     rate.sleep()

def mapObjectTypeList():
    pub = rospy.Publisher('ldarcl_mapObjectTypeList', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting list of types of map objects in the map..."
    command = "mapObjectTypeList"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    mapObjectTypeList = data.encode('ascii', 'ignore')
    rospy.loginfo(mapObjectTypeList)
    pub.publish(str(mapObjectTypeList.splitlines()))
    rate.sleep()

def odometer():
    pub = rospy.Publisher('ldarcl_odometer', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting odometer readings..."
    command = "odometer"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    odometer = data.encode('ascii', 'ignore')
    rospy.loginfo(odometer)
    pub.publish(str(odometer.splitlines()))
    rate.sleep()

def oneLineStatus():
    pub = rospy.Publisher('ldarcl_oneLineStatus', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting one line status..."
    command = "oneLineStatus"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    oneLineStatus = data.encode('ascii', 'ignore')
    rospy.loginfo(oneLineStatus)
    pub.publish(str(oneLineStatus.splitlines()))
    rate.sleep()

def queryDockStatus():
    pub = rospy.Publisher('ldarcl_queryDockStatus', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting docking/charging status..."
    command = "queryDockStatus"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    queryDockStatus = data.encode('ascii', 'ignore')
    rospy.loginfo(queryDockStatus)
    pub.publish(str(queryDockStatus.splitlines()))
    rate.sleep()

def queryMotors():
    pub = rospy.Publisher('ldarcl_queryMotors', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting state of robot motors..."
    command = "queryMotors"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    queryMotors = data.encode('ascii', 'ignore')
    rospy.loginfo(queryMotors)
    pub.publish(str(queryMotors.splitlines()))
    rate.sleep()

# def queueShow():
#     pub = rospy.Publisher('ldarcl_queueShow', String, queue_size=10)
#     rospy.init_node('ld_queueShow', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     print(Style.RESET_ALL)
#     print(Fore.GREEN)
#     print "Getting status of last 11 jobs in queue..."
#     command = "queueShow"
#     command = command.encode('ascii')
#     s.send(command+b"\r\n")
#     global rcv
#     data = s.recv(BUFFER_SIZE)
#     time.sleep(1)
#     queueShow = data.encode('ascii', 'ignore')
#     rospy.loginfo(queueShow)
#     pub.publish(str(queueShow.splitlines()))
#     rate.sleep()

def queueShowRobotLocal():
    pub = rospy.Publisher('ldarcl_queueShowRobotLocal', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting status of robot..."
    command = "queueShowRobotLocal"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    queueShowRobotLocal = data.encode('ascii', 'ignore')
    rospy.loginfo(queueShowRobotLocal)
    pub.publish(str(queueShowRobotLocal.splitlines()))
    rate.sleep()

def waitTaskState():
    pub = rospy.Publisher('ldarcl_waitTaskState', String, queue_size=10)
    rospy.init_node('ld_topic_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Getting status of wait task..."
    command = "waitTaskState"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    global rcv
    data = s.recv(BUFFER_SIZE)
    time.sleep(1)
    waitTaskState = data.encode('ascii', 'ignore')
    rospy.loginfo(waitTaskState)
    pub.publish(str(waitTaskState.splitlines()))
    rate.sleep()


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            applicationFaultQuery()
            faultsGet()
            getDateTime()
            # getGoals()
            # getMacros()
            # getRoutes()
            # mapObjectTypeList()
            # odometer()
            # oneLineStatus()
            # queryDockStatus()
            # queryMotors()
            # # queueShow()
            # queueShowRobotLocal()
            # waitTaskState()

    except rospy.ROSInterruptException:
        pass
