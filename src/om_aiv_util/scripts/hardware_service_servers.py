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
    arg = req.a[0]
    analogInputQueryRaw(arg)
    return rcv
def handle_analogInputQueryVoltage(req):
    arg = req.a[0]
    analogInputQueryVoltage(arg)
    return rcv
def handle_configStart(req):
    configStart()
    return rcv
def handle_connectOutgoing(req):
    a = req.a[0]
    b = req.a[1]
    connectOutgoing(a, b)
    return rcv
def handle_doTaskInstant(req):
    a = req.a[0]
    b = req.a[1]
    doTaskInstant(a, b)
    return rcv
def handle_enableMotors(req):
    enableMotors()
    return rcv
def handle_extIOAdd(req):
    name = req.a[0]
    numInputs = req.a[1]
    numOutputs = req.a[2]
    extIOAdd(name, numInputs, numOutputs)
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
    elif op == "ConfigStart":
        rospy.loginfo("running ConfigStart")
        s4 = rospy.Service('configStart', OmAivService, handle_configStart)
    elif op == "ConnectOutgoing":
        rospy.loginfo("running ConnectOutgoing")
        s4 = rospy.Service('connectOutgoing', OmAivService, handle_connectOutgoing)
    elif op == "DoTaskInstant":
        rospy.loginfo("running DoTaskInstant")
        s5 = rospy.Service('doTaskInstant', OmAivService, handle_doTaskInstant)
    elif op == "EnableMotors":
        rospy.loginfo("running EnableMotors")
        s6 = rospy.Service('enableMotors', OmAivService, handle_enableMotors)

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

def analogInputQueryRaw(arg):
    global rcv
    pub = rospy.Publisher('arcl_analogInputQueryRaw', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "analogInputQueryRaw {}".format(arg)
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

def analogInputQueryVoltage(arg):
    global rcv
    pub = rospy.Publisher('arcl_analogInputQueryVoltage', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "analogInputQueryVoltage {}".format(arg)
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

def configStart():
    global rcv
    pub = rospy.Publisher('arcl_configStart', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "configStart"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "New config starting" in rcv:
                print rcv
                return rcv
                break
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
                break
            if "Unknown command" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def connectOutgoing(a, b):
    global rcv
    pub = rospy.Publisher('arcl_connectOutgoing', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "connectOutgoing {}".format(a + " " + b)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "connected" in rcv:
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

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def doTaskInstant(a, b):
    global rcv
    pub = rospy.Publisher('arcl_doTaskInstant', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "doTaskInstant {}".format(a + " " + b)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Completed doing " in rcv:
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

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def enableMotors():
    global rcv
    rate = rospy.Rate(10) # 10hz
    command = "enableMotors"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Motors" in rcv:
                print rcv
                return rcv
                break
            if "EStop" in rcv:
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
    analogInputList_servers("ConfigStart")
    analogInputList_servers("ConnectOutgoing")
    analogInputList_servers("DoTaskInstant")
    analogInputList_servers("EnableMotors")
    rospy.spin()
