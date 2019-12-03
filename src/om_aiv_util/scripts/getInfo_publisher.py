#!/usr/bin/env python
## publishes std_msgs messages to the 5 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Point
from om_aiv_util.msg import Location
import math
import numpy as np
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 2056
#import socketconnection class to connect to robot
#requires socketconnection_class.py file in the same folder
from socketconnection_class import ConnectSocket
connecttcp = ConnectSocket()
s = connecttcp.sock
#get ip adress and port from launch file
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.123"
# port = 7171
connecttcp.connect(str(ip_address), port)
rospy.init_node('getInfo_publisher', anonymous=True)

def getInfo_WirelessLink():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_WirelessLink', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo WirelessLink"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_WirelessQuality():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_WirelessQuality', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo WirelessQuality"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Odometer():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Odometer', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Odometer(KM)"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Odometer(KM)" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Odometer(KM)' in line:
            info = line.split("Odometer(KM)")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("Odometer(KM):".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_HourMeter():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_HourMeter', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo HourMeter"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'HourMeter' in line:
            info = line.split("Hourmeter")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("Hourmeter:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Temperature():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Temperature', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Temperature(C)"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Temperature(C)' in line:
            # info = line.split("Temperature(C)")
            # infonum = [int(i) for i in line.split() if i.isdigit()]
            # infonum = int("".join(map(str, infonum)))
            # #print required data
            # rospy.loginfo(",Info:".join(info)[1:])
            # #publish data
            # pub.publish(infonum)
            info = line.split("Temperature(C)")
            #print required data
            rospy.loginfo("Temperature(C)".join(info))
            #publish data
            pub.publish(''.join(info))

            break

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_LaserScore():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_LaserScore', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo LaserScore"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'LaserScore' in line:
            info = line.split("LaserScore")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("LaserScore:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_LaserLock():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_LaserLock', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo LaserLock"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'LaserLock' in line:
            info = line.split("LaserLock")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("LaserLock:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")



def getInfo_LaserNumSamples():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_LaserNumSamples', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo LaserNumSamples"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'LaserNumSamples' in line:
            info = line.split("LaserNumSamples")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("LaserNumSamples:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_LaserNumPeaks():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_LaserNumPeaks', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo LaserNumPeaks"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'LaserNumPeaks' in line:
            info = line.split("LaserNumPeaks")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("LaserNumPeaks:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Mpacs():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Mpacs', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Mpacs"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'MPacs' in line:
            info = line.split("Mpacs")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("MPacs:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Laser_1_Pacs():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Laser_1_Pacs', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Laser_1 Pacs"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Laser_1 Pacs' in line:
            info = line.split("Laser_1 Pacs")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("Laser_1 Pacs:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_SBC_Uptime():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_SBC_Uptime', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo SBC Uptime"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'SBC Uptime' in line:
            info = line.split("SBC Uptime")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("SBC Uptime:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_ARAM_Uptime():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_ARAM_Uptime', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo ARAM Uptime"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'ARAM Uptime' in line:
            info = line.split("ARAM Uptime")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("ARAM Uptime:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Idle():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Idle', Int32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Idle"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Idle' in line:
            info = line.split("Idle")
            infonum = [int(i) for i in line.split() if i.isdigit()]
            infonum = int("".join(map(str, infonum)))
            #print required data
            rospy.loginfo("Idle:".join(info))
            #publish data
            pub.publish(infonum)

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_TipAngle():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_TipAngle', Float32, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo TipAngle"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'TipAngle' in line:
            info = line.split("TipAngle")
            line = line.strip("deg")
            line2 = line.split("TipAngle")
            line3 = line.strip(",")
            line4 = line.strip("Info: TipAngle")

            rospy.loginfo("TipAngle:".join(info))
            #publish data
            pub.publish(float(line4))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_IsTipped():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_IsTipped', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo IsTipped"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Queue_ID():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Queue_ID', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Queue ID"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_Queue_Job_ID():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_Queue_Job_ID', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo Queue Job ID"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_DebugLogState():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_DebugLogState', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo DebugLogState"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")


def getInfo_DebugLogSeconds():
    #specify topic name
    pub = rospy.Publisher('ldarcl_getInfo_DebugLogSeconds', String, queue_size=10)
    #specify node name


    print(Style.RESET_ALL)
    print(Fore.GREEN)
    #send command to arcl
    command = "getInfo DebugLogSeconds"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "Info" in rcv:
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if 'Info:' in line:
            info = line.split("Info:")
            #print required data
            rospy.loginfo(",Info:".join(info)[1:])
            #publish data
            pub.publish(''.join(info))

            break

        if 'Info:' not in line:
            rospy.loginfo("No info")
            pub.publish("No info")

if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            getInfo_WirelessLink()
            getInfo_WirelessQuality()
            getInfo_Odometer()
            getInfo_HourMeter()
            getInfo_Temperature()
            getInfo_LaserScore()
            getInfo_LaserLock()
            getInfo_LaserNumSamples()
            getInfo_LaserNumPeaks()
            getInfo_Mpacs()
            getInfo_Laser_1_Pacs()
            getInfo_SBC_Uptime()
            getInfo_ARAM_Uptime()
            getInfo_Idle()
            getInfo_TipAngle()
            getInfo_IsTipped()
            getInfo_Queue_ID()
            getInfo_Queue_Job_ID()
            getInfo_DebugLogState()
            getInfo_DebugLogSeconds()

    except rospy.ROSInterruptException:
        pass
