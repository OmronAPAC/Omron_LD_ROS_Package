#!/usr/bin/env python
from om_aiv_util.srv import OmAivService, OmAivServiceResponse
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
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.122"
# port = 7171
connecttcp.connect(str(ip_address), port)

def handle_analogInputList(req):
    rcv = analogInputList()
    return rcv
def handle_analogInputQueryRaw(req):
    arg = req.a[0]
    rcv = analogInputQueryRaw(arg)
    return rcv
def handle_analogInputQueryVoltage(req):
    arg = req.a[0]
    rcv = analogInputQueryVoltage(arg)
    return rcv
def handle_configStart(req):
    rcv = configStart()
    return rcv
def handle_connectOutgoing(req):
    a = req.a[0]
    b = req.a[1]
    rcv = connectOutgoing(a, b)
    return rcv
def handle_doTaskInstant(req):
    a = req.a[0]
    b = req.a[1]
    rcv =  doTaskInstant(a, b)
    return rcv
def handle_enableMotors(req):
    rcv = enableMotors()
    return rcv
def handle_extIOAdd(req):
    name = req.a[0]
    num_inputs = req.a[1]
    num_outputs = req.a[2]
    rcv = extIOAdd(name, num_inputs, num_outputs)
    return rcv
def handle_extIODump(req):
    rcv = extIODump()
    return rcv
def handle_extIODumpLocal(req):
    rcv = extIODumpLocal()
    return rcv
def handle_extIOInputUpdate(req):
    name = req.a[0]
    value = req.a[1]
    rcv = extIOInputUpdate(name, value)
    return rcv
def handle_extIOInputUpdateBit(req):
    name = req.a[0]
    bit_postition = req.a[1]
    bit_value = req.a[2]
    rcv = extIOInputUpdateBit(name, bit_postition, bit_value)
    return rcv
def handle_extIOInputUpdateByte(req):
    name = req.a[0]
    byte_position = req.a[1]
    byte_value = req.a[2]
    rcv = extIOInputUpdateByte(name, byte_position, byte_value)
    return rcv
def handle_extIOOutputUpdate(req):
    name = req.a[0]
    value = req.a[1]
    rcv = extIOOutputUpdate(name, value)
    return rcv
def handle_extIOOutputUpdateBit(req):
    name = req.a[0]
    bit_postition = req.a[1]
    bit_value = req.a[2]
    rcv = extIOOutputUpdateBit(name, bit_postition, bit_value)
    return rcv
def handle_extIOOutputUpdateByte(req):
    name = req.a[0]
    byte_position = req.a[1]
    byte_value = req.a[2]
    rcv = extIOOutputUpdateByte(name, byte_position, byte_value)
    return rcv
def handle_extIORemove(req):
    name = req.a[0]
    rcv = extIORemove(name)
    return rcv
def handle_getConfigSectionInfo(req):
    section = req.a[0]
    rcv = getConfigSectionInfo(section)
    return rcv
def handle_getConfigSectionList(req):
    rcv = getConfigSectionList()
    return rcv
def handle_getConfigSectionValues(req):
    section = req.a[0]
    rcv = getConfigSectionValues(section)
    return rcv
def handle_inputList(req):
    rcv = inputList()
    return rcv
def handle_inputQuery(req):
    name = req.a[0]
    rcv = inputQuery(name)
    return rcv
def handle_odometerReset(req):
    rcv = odometerReset()
    return rcv
def handle_outputList(req):
    rcv = outputList()
    return rcv
def handle_outputOff(req):
    name = req.a[0]
    rcv = outputOff(name)
    return rcv
def handle_outputOn(req):
    name = req.a[0]
    rcv = outputOn(name)
    return rcv
def handle_outputQuery(req):
    name = req.a[0]
    rcv = outputQuery(name)
    return rcv
def handle_payloadQueryLocal(req):
    slot_num = req.a[0]
    rcv = payloadQueryLocal(slot_num)
    return rcv
def handle_payloadRemove(req):
    slot_num = req.a[0]
    rcv = payloadRemove(slot_num)
    return rcv

def hardware_servers(op):
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
    elif op == "ExtIOOuputUpdateBit":
        rospy.loginfo("running ExtIOOuputUpdateBit")
        s15 = rospy.Service('extIOOutputUpdateBit', OmAivService, handle_extIOOutputUpdateBit)
    elif op == "ExtIOOuputUpdateByte":
        rospy.loginfo("running ExtIOOuputUpdateByte")
        s16 = rospy.Service('extIOOutputUpdateByte', OmAivService, handle_extIOOutputUpdateByte)
    elif op == "ExtIORemove":
        rospy.loginfo("running ExtIORemove")
        s17 = rospy.Service('extIORemove', OmAivService, handle_extIORemove)
    elif op == "GetConfigSectionInfo":
        rospy.loginfo("running GetConfigSectionInfo")
        s18 = rospy.Service('getConfigSectionInfo', OmAivService, handle_getConfigSectionInfo)
    elif op == "GetConfigSectionList":
        rospy.loginfo("running GetConfigSectionList")
        s19 = rospy.Service('getConfigSectionList', OmAivService, handle_getConfigSectionList)
    elif op == "GetConfigSectionValues":
        rospy.loginfo("running GetConfigSectionValues")
        s20 = rospy.Service('getConfigSectionValues', OmAivService, handle_getConfigSectionValues)
    elif op == "InputList":
        rospy.loginfo("running InputList")
        s21 = rospy.Service('inputList', OmAivService, handle_inputList)
    elif op == "InputQuery":
        rospy.loginfo("running InputQuery")
        s22 = rospy.Service('inputQuery', OmAivService, handle_inputQuery)
    elif op == "OdometerReset":
        rospy.loginfo("running OdometerReset")
        s23 = rospy.Service('odometerReset', OmAivService, handle_odometerReset)
    elif op == "OutputList":
        rospy.loginfo("running OutputList")
        s24 = rospy.Service('outputList', OmAivService, handle_outputList)
    elif op == "OutputOff":
        rospy.loginfo("running OutputOff")
        s25 = rospy.Service('outputOff', OmAivService, handle_outputOff)
    elif op == "OutputOn":
        rospy.loginfo("running OutputOn")
        s25 = rospy.Service('outputOn', OmAivService, handle_outputOn)
    elif op == "OutputQuery":
        rospy.loginfo("running OutputQuery")
        s26 = rospy.Service('outputQuery', OmAivService, handle_outputQuery)
    elif op == "PayloadQueryLocal":
        rospy.loginfo("running PayloadQueryLocal")
        s27 = rospy.Service('payloadQueryLocal', OmAivService, handle_payloadQueryLocal)
    elif op == "PayloadRemove":
        rospy.loginfo("running PayloadRemove")
        s28 = rospy.Service('payloadRemove', OmAivService, handle_payloadRemove)

def analogInputList():
    command = "analogInputList"
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of AnalogInputList" in rcv:
                print rcv
                rcv = str(rcv.splitlines())
                return rcv
                break

            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def analogInputQueryRaw(arg):
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

def extIOAdd(name, num_inputs, num_outputs):
    command = "extIOAdd {}".format(name + " " + num_inputs + " " + num_outputs)
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
    # pub = rospy.Publisher('arcl_extIOInputUpdateByte', String, queue_size=10)
    # rate = rospy.Rate(10) # 10hz
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

def extIOOutputUpdateBit(name, bit_postition, bit_value):
    pub = rospy.Publisher('arcl_extIOOutputUpdateBit', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOOutputUpdateBit {}".format(name + " " + bit_postition + " " + bit_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOOutputUpdateBit:" in rcv:
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

def extIOOutputUpdateByte(name, byte_position, byte_value):
    command = "extIOOutputUpdateByte {}".format(name + " " + byte_position + " " + byte_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOOutputUpdateByte:" in rcv:
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

def extIORemove(name):
    command = "extIORemove {}".format(name)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIORemove:" in rcv:
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

def getConfigSectionInfo(section):
    command = "getConfigSectionInfo {}".format(section)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetConfigSectionInfo" in rcv:
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

def getConfigSectionList():
    command = "getConfigSectionList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetConfigSectionList" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def getConfigSectionValues(section):
    command = "getConfigSectionValues {}".format(section)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetConfigSectionValues" in rcv:
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

def inputList():
    command = "inputList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of InputList" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def inputQuery(name):
    command = "inputQuery {}".format(name)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Input:" in rcv:
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

def odometerReset():
    command = "odometerReset"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Reset odometer" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def outputList():
    command = "outputList"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of OutputList" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

def outputOff(name):
    global rcv
    pub = rospy.Publisher('arcl_outputOff', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "outputOff {}".format(name)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Output:" in rcv:
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

def outputOn(name):
    global rcv
    pub = rospy.Publisher('arcl_outputOn', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "outputOn {}".format(name)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Output:" in rcv:
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

def outputQuery(name):
    command = "outputQuery {}".format(name)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Output:" in rcv:
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

def payloadQueryLocal(slot_num):
    command = "payloadQueryLocal {}".format(slot_num)
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndPayloadQuery" in rcv:
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

def payloadRemove(slot_num):
    command = "payloadRemove {}".format(slot_num)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "PayloadUpdate" in rcv:
                print rcv
                return rcv
                break
            if "failed" in rcv:
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
    rospy.init_node('hardware_servers')
    hardware_servers("List")
    hardware_servers("QueryRaw")
    hardware_servers("QueryVoltage")
    hardware_servers("ConfigStart")
    hardware_servers("ConnectOutgoing")
    hardware_servers("DoTaskInstant")
    hardware_servers("EnableMotors")
    hardware_servers("ExtIOAdd")
    hardware_servers("ExtIODump")
    hardware_servers("ExtIODumpLocal")
    hardware_servers("ExtIOInputUpdate")
    hardware_servers("ExtIOInputUpdateBit")
    hardware_servers("ExtIOInputUpdateByte")
    hardware_servers("ExtIOOuputUpdate")
    hardware_servers("ExtIOOuputUpdateBit")
    hardware_servers("ExtIOOuputUpdateByte")
    hardware_servers("ExtIORemove")
    hardware_servers("GetConfigSectionInfo")
    hardware_servers("GetConfigSectionList")
    hardware_servers("GetConfigSectionValues")
    hardware_servers("InputList")
    hardware_servers("InputQuery")
    hardware_servers("OdometerReset")
    hardware_servers("OutputList")
    hardware_servers("OutputOff")
    hardware_servers("OutputOn")
    hardware_servers("OutputQuery")
    hardware_servers("PayloadQueryLocal")
    hardware_servers("PayloadRemove")
    rospy.spin()
