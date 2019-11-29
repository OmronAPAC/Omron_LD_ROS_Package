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
rospy.init_node('ld_topic_publisher', anonymous=True)

def runCommand(command, command2, text):
    #specify topic name
    topic_name = "ldarcl_{}".format(command)
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    #specify node name
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Running command: ", command
    #send command to arcl
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "End of {}".format(command2) in rcv:
                break
            if "Unknown command {}".format(command) in rcv:
                rospy.logerr(rcv)
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if "{}:".format(command2) in line:
            cmd = line.split("{}:".format(command2))
            #print required data
            rospy.loginfo(",{}:".format(command2).join(cmd)[1:])
            #publish data
            pub.publish(''.join(cmd))
            break
        #if there are no faults print "Np faults"
        if "{}:".format(command2) not in line:
            rospy.loginfo(text)
            pub.publish(text)

def runCommand(command, command2, text):
    #specify topic name
    topic_name = "ldarcl_{}".format(command)
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    #specify node name
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Running command: ", command
    #send command to arcl
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if "End of {}".format(command2) in rcv:
                break
            if "Unknown command {}".format(command) in rcv:
                rospy.logerr(rcv)
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
    except socket.error as e:
        print("Connection  failed")
        return e
    #check for required data
    for line in rcv.splitlines():
        if "{}:".format(command2) in line:
            cmd = line.split("{}:".format(command2))
            #print required data
            rospy.loginfo(",{}:".format(command2).join(cmd)[1:])
            #publish data
            pub.publish(''.join(cmd))
            break
        #if there are no faults print "Np faults"
        if "{}:".format(command2) not in line:
            rospy.loginfo(text)
            pub.publish(text)


if __name__ == '__main__':
    try:
        while not rospy.is_shutdown():
            runCommand('ApplicationFaultQuery', 'ApplicationFaultQuery', 'ApplicationFaultQuery: No Faults')
            runCommand('FaultsGet', 'FaultList', 'FaultsGet: No Faults')


    except rospy.ROSInterruptException:
        pass
