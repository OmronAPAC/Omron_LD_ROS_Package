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

def handle_queueCancelLocal(req):
    type = req.a[0]
    value = req.a[1]
    echo_str = req.a[2]
    reason = req.a[3]
    rcv = queueCancelLocal(type, value, echo_str, reason)
    return rcv
def handle_queueDropoff(req):
    goal_name = req.a[0]
    priority = req.a[1]
    job_id = req.a[2]
    rcv = queueDropoff(goal_name, priority, job_id)
    return rcv
def handle_queueModifyLocal(req):
    id = req.a[0]
    type = req.a[1]
    value = req.a[2]
    rcv = queueModifyLocal(id, type, value)
    return rcv
def handle_queueQueryLocal(req):
    type = req.a[0]
    value = req.a[1]
    echo_str = req.a[2]
    rcv = queueQueryLocal(type, value, echo_str)
    return rcv

def hardware_servers(op):
    if op == "queueCancelLocal":
        rospy.loginfo("running queueCancelLocal")
        s1 = rospy.Service('queueCancelLocal', OmAivService, handle_queueCancelLocal)
    elif op == "queueDropoff":
        rospy.loginfo("running queueDropoff")
        s2 = rospy.Service('queueDropoff', OmAivService, handle_queueDropoff)
    elif op == "queueModifyLocal":
        rospy.loginfo("running queueModifyLocal")
        s3 = rospy.Service('queueModifyLocal', OmAivService, handle_queueModifyLocal)
    elif op == "queueQueryLocal":
        rospy.loginfo("running queueQueryLocal")
        s4 = rospy.Service('queueQueryLocal', OmAivService, handle_queueQueryLocal)

def queueCancelLocal(type, value, echo_str, reason):
    command = "queueCancelLocal {}".format(type + " " + value + " \"" + echo_str + "\" " + reason)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "queuecancel" in rcv:
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

def queueDropoff(goal_name, priority, job_id):
    command = "queueDropoff {}".format(goal_name + " " + priority + " " + job_id)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Completed" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
                print rcv
                return rcv

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def queueModifyLocal(id, type, value):
    command = "queueModifyLocal {}".format(id + " " + type + " " + value)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "modiying" in rcv:
                print rcv
                return rcv
            if "CommandErrorDescription" in rcv:
                print rcv
                return rcv
            if "QueueUpdate:" in rcv:
                print rcv
                return rcv
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def queueQueryLocal(type, value, echo_str):
    command = "queueQueryLocal {}".format(type + " " + value + " " + echo_str)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndQueueQuery" in rcv:
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


if __name__ == "__main__":
    rospy.init_node('hardware_servers')
    hardware_servers("queueCancelLocal")
    hardware_servers("queueDropoff")
    hardware_servers("queueModifyLocal")
    hardware_servers("queueQueryLocal")
    rospy.spin()
