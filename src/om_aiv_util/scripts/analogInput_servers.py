#!/usr/bin/env python
from om_aiv_util.srv import OmAivService,OmAivServiceResponse
import rospy
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024
# ip_address = rospy.get_param("ip_address")
# port = rospy.get_param("port")
ip_address = "172.21.5.123"
port = 7171
connecttcp.connect(str(ip_address), port)

def handle_analogInputList(req):
    analogInputList()
    return rcv
def handle_analogInputQueryRaw(req):
    global text
    text = req.a
    analogInputQueryRaw()
    return rcv
def handle_analogInputQueryVoltage(req):
    global text
    text = req.a
    analogInputQueryVoltage()
    return rcv

def analogInputList_servers(op):
    # print op
    if op == "List":
        rospy.loginfo("running List")
        s1 = rospy.Service('analogInputList', OmAivService, handle_analogInputList)
    elif op == "QueryRaw":
        rospy.loginfo("running QueryRaw")
        s2 = rospy.Service('analogInputQueryRaw', OmAivService, handle_analogInputQueryRaw)
    elif op == "QueryVoltage":
        rospy.loginfo("running QueryVoltage")
        s3 = rospy.Service('analogInputQueryVoltage', OmAivService, handle_analogInputQueryVoltage)

def analogInputList():
    global rcv
    pub = rospy.Publisher('arcl_analogInputList', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    command = "analogInputList"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of AnalogInputList" in rcv:

                print rcv
                rcv = str(rcv.splitlines())
                break

            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def analogInputQueryRaw():
    global rcv
    pub = rospy.Publisher('arcl_analogInputQueryRaw', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "analogInputQueryRaw {}".format(text)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "AnalogInputRaw:" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def analogInputQueryVoltage():
    global rcv
    pub = rospy.Publisher('arcl_analogInputQueryVoltage', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "analogInputQueryVoltage {}".format(text)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "AnalogInputVoltage:" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e


if __name__ == "__main__":
    rospy.init_node('analogInput_servers')
    analogInputList_servers("List")
    analogInputList_servers("QueryRaw")
    analogInputList_servers("QueryVoltage")
    rospy.spin()
