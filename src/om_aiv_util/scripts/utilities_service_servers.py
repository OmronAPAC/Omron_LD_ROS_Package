#!/usr/bin/env python
from om_aiv_util.srv import OmAivService, OmAivServiceResponse
import rospy
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
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

def handle_applicationFaultClear(req):
    name = req.a[0]
    rcv = applicationFaultClear(name)
    return rcv
def handle_applicationFaultSet(req):
    name = req.a[0]
    short_description = req.a[1]
    long_description = req.a[2]
    bool_driving = req.a[3]
    bool_critical = req.a[4]
    rcv = applicationFaultSet(name, short_description, long_description, bool_driving, bool_critical)
    return rcv
def handle_arclSendText(req):
    string = req.a[0]
    rcv = arclSendText(string)
    return rcv
def handle_configAdd(req):
    configuration_section = req.a[0]
    value = req.a[1]
    rcv = configAdd(configuration_section, value)
    return rcv
def handle_configParse(req):
    rcv = configParse()
    return rcv
def handle_createInfo(req):
    info_name = req.a[0]
    max_len = req.a[1]
    info_value = req.a[2]
    rcv = createInfo(info_name, max_len, info_value)
    return rcv
def handle_echo(req):
    state = req.a[0]
    rcv = echo(state)
    return rcv


def hardware_servers(op):
    if op == "applicationFaultClear":
        rospy.loginfo("running applicationFaultClear")
        s1 = rospy.Service('applicationFaultClear', OmAivService, handle_applicationFaultClear)
    elif op == "applicationFaultSet":
        rospy.loginfo("running applicationFaultSet")
        s2 = rospy.Service('applicationFaultSet', OmAivService, handle_applicationFaultSet)
    elif op == "arclSendText":
        rospy.loginfo("running arclSendText")
        s3 = rospy.Service('arclSendText', OmAivService, handle_arclSendText)
    elif op == "configAdd":
        rospy.loginfo("running configAdd")
        s4 = rospy.Service('configAdd', OmAivService, handle_configAdd)
    elif op == "configParse":
        rospy.loginfo("running configParse")
        s5 = rospy.Service('configParse', OmAivService, handle_configParse)
    elif op == "createInfo":
        rospy.loginfo("running createInfo")
        s6 = rospy.Service('createInfo', OmAivService, handle_createInfo)
    elif op == "echo":
        rospy.loginfo("running echo")
        s6 = rospy.Service('echo', OmAivService, handle_echo)

def applicationFaultClear(name):
    command = "applicationFaultClear {}".format(name)
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "ApplicationFaultClear cleared" in rcv:
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

def applicationFaultSet(name, short_description, long_description, bool_driving, bool_critical):
    command = "applicationFaultSet {}".format(name + " " + short_description
    + " " + long_description + " " + bool_driving + " " + bool_critical)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Fault:" in rcv:
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

def arclSendText(string):
    command = "arclSendText {}".format(string)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if string in rcv:
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

def configAdd(configuration_section, value):
    command = "configAdd {}".format(configuration_section + " " + value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Added" in rcv:
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

def configParse():
    command = "configParse"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Config parsed fine" in rcv:
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

def createInfo(info_name, max_len, info_value):
    command = "createInfo {}".format(info_name + " " + max_len + " " + info_value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Created info" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def echo(state):
    command = "echo {}".format(state)
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Echo is" in rcv:
                print rcv
                return rcv
            if "Echo turned" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e


if __name__ == "__main__":
    rospy.init_node('utilities_service_servers')
    hardware_servers("applicationFaultClear")
    hardware_servers("applicationFaultSet")
    hardware_servers("arclSendText")
    hardware_servers("configAdd")
    hardware_servers("configParse")
    hardware_servers("createInfo")
    hardware_servers("echo")
    rospy.spin()
