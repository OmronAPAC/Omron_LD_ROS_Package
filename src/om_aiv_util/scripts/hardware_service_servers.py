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
ip_address = "172.21.5.122"
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
def handle_extIODump(req):
    extIODump()
    return rcv
def handle_extIODumpLocal(req):
    extIODumpLocal()
    return rcv
def handle_extIOInputUpdate(req):
    name = req.a[0]
    value = req.a[1]
    extIOInputUpdate(name, value)
    return rcv
def handle_extIOInputUpdateBit(req):
    name = req.a[0]
    bit_postition = req.a[1]
    bit_value = req.a[2]
    extIOInputUpdateBit(name, bit_postition, bit_value)
    return rcv
def handle_extIOInputUpdateByte(req):
    name = req.a[0]
    byte_position = req.a[1]
    byte_value = req.a[2]
    extIOInputUpdateByte(name, byte_position, byte_value)
    return rcv
def handle_extIOOutputUpdate(req):
    name = req.a[0]
    value = req.a[1]
    extIOOutputUpdate(name, value)
    return rcv


def analogInputList_servers(op):
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
        s5 = rospy.Service('connectOutgoing', OmAivService, handle_connectOutgoing)
    elif op == "DoTaskInstant":
        rospy.loginfo("running DoTaskInstant")
        s6 = rospy.Service('doTaskInstant', OmAivService, handle_doTaskInstant)
    elif op == "EnableMotors":
        rospy.loginfo("running EnableMotors")
        s7 = rospy.Service('enableMotors', OmAivService, handle_enableMotors)
    elif op == "ExtIOAdd":
        rospy.loginfo("running ExtIOAdd")
        s8 = rospy.Service('extIOAdd', OmAivService, handle_extIOAdd)
    elif op == "ExtIODump":
        rospy.loginfo("running ExtIODump")
        s9 = rospy.Service('extIODump', OmAivService, handle_extIODump)
    elif op == "ExtIODumpLocal":
        rospy.loginfo("running ExtIODumpLocal")
        s10 = rospy.Service('extIODumpLocal', OmAivService, handle_extIODumpLocal)
    elif op == "ExtIOInputUpdate":
        rospy.loginfo("running ExtIOInputUpdate")
        s11 = rospy.Service('extIOInputUpdate', OmAivService, handle_extIOInputUpdate)
    elif op == "ExtIOInputUpdateBit":
        rospy.loginfo("running ExtIOInputUpdateBit")
        s12 = rospy.Service('extIOInputUpdateBit', OmAivService, handle_extIOInputUpdateBit)
    elif op == "ExtIOInputUpdateByte":
        rospy.loginfo("running ExtIOInputUpdateByte")
        s13 = rospy.Service('extIOInputUpdateByte', OmAivService, handle_extIOInputUpdateByte)
    elif op == "ExtIOOuputUpdate":
        rospy.loginfo("running ExtIOOuputUpdate")
        s14 = rospy.Service('extIOOutputUpdate', OmAivService, handle_extIOOutputUpdate)

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

def extIOAdd(name, numInputs, numOutputs):
    global rcv
    pub = rospy.Publisher('arcl_extIOAdd', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOAdd {}".format(name + " " + numInputs + " " + numOutputs)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOAdd:" in rcv:
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

def extIODump():
    global rcv
    pub = rospy.Publisher('arcl_extIODump', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIODump"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndExtIODump" in rcv:
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

def extIODumpLocal():
    global rcv
    pub = rospy.Publisher('arcl_extIODumpLocal', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIODumpLocal"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndExtIODumpLocal" in rcv:
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

def extIOInputUpdate(name, value):
    global rcv
    pub = rospy.Publisher('arcl_extIOInputUpdate', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOInputUpdate {}".format(name + " " + value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOInputUpdate:" in rcv:
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

def extIOInputUpdateBit(name, bit_postition, bit_value):
    global rcv
    pub = rospy.Publisher('arcl_extIOInputUpdateBit', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOInputUpdateBit {}".format(name + " " + bit_postition + " " + bit_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOInputUpdateBit:" in rcv:
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

def extIOInputUpdateByte(name, byte_position, byte_value):
    global rcv
    pub = rospy.Publisher('arcl_extIOInputUpdateByte', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOInputUpdateByte {}".format(name + " " + byte_position + " " + byte_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOInputUpdateByte:" in rcv:
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

def extIOOutputUpdate(name, value):
    global rcv
    pub = rospy.Publisher('arcl_extIOOutputUpdate', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOOutputUpdate {}".format(name + " " + value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOOutputUpdate:" in rcv:
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

if __name__ == "__main__":
    rospy.init_node('analogInput_servers')
    analogInputList_servers("List")
    analogInputList_servers("QueryRaw")
    analogInputList_servers("QueryVoltage")
    analogInputList_servers("ConfigStart")
    analogInputList_servers("ConnectOutgoing")
    analogInputList_servers("DoTaskInstant")
    analogInputList_servers("EnableMotors")
    analogInputList_servers("ExtIOAdd")
    analogInputList_servers("ExtIODump")
    analogInputList_servers("ExtIODumpLocal")
    analogInputList_servers("ExtIOInputUpdate")
    analogInputList_servers("ExtIOInputUpdateBit")
    analogInputList_servers("ExtIOInputUpdateByte")
    analogInputList_servers("ExtIOOuputUpdate")
    rospy.spin()
