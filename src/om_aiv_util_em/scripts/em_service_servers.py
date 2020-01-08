#!/usr/bin/env python
from om_aiv_util.srv import OmAivService, OmAivServiceResponse
import rospy
from om_aiv_util.socketconnection_class import ConnectSocket, connecttcp
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

def handle_payloadQuery(req):
    robot_name = req.a[0]
    slot_num = req.a[1]
    rcv = payloadQuery(robot_name, slot_num)
    return rcv
def handle_payloadSlotCount(req):
    robot_name = req.a[0]
    rcv = payloadSlotCount(robot_name)
    return rcv
def handle_queueCancel(req):
    type = req.a[0]
    value = req.a[1]
    echo_str = req.a[2]
    reason = req.a[3]
    rcv = queueCancel(type, value, echo_str, reason)
    return rcv
def handle_queueModify(req):
    id = req.a[0]
    type = req.a[1]
    value = req.a[2]
    rcv = queueModify(id, type, value)
    return rcv
def handle_queueMulti(req):
    arg = str(req.a)
    rcv = queueMulti(arg)
    return rcv
def handle_queuePickup(req):
    goal_name = req.a[0]
    priority = req.a[1]
    job_id = req.a[2]
    rcv = queuePickup(goal_name, priority, job_id)
    return rcv
def handle_queuePickupDropoff(req):
    goal1_name = req.a[0]
    goal2_name = req.a[1]
    priority1 = req.a[2]
    priority2 = req.a[3]
    job_id = req.a[4]
    rcv = queuePickupDropoff(goal1_name, goal2_name, priority1, priority2, job_id)
    return rcv
def handle_queueQuery(req):
    type = req.a[0]
    value = req.a[1]
    echo_str = req.a[2]
    rcv = queueQuery(type, value, echo_str)
    return rcv
def handle_queueShowRobot(req):
    robot_name = req.a[0]
    rcv = queueShowRobot(robot_name)
    return rcv

def em_service_servers(op):
    if op == "payloadQuery":
        rospy.loginfo("running payloadQuery")
        s1 = rospy.Service('payloadQuery', OmAivService, handle_payloadQuery)
    elif op == "payloadSlotCount":
        rospy.loginfo("running payloadSlotCount")
        s2 = rospy.Service('payloadSlotCount', OmAivService, handle_payloadSlotCount)
    elif op == "queueCancel":
        rospy.loginfo("running queueCancel")
        s3= rospy.Service('queueCancel', OmAivService, handle_queueCancel)
    elif op == "queueModify":
        rospy.loginfo("running queueModify")
        s4 = rospy.Service('queueModify', OmAivService, handle_queueModify)
    elif op == "queueMulti":
        rospy.loginfo("running queueMulti")
        s5 = rospy.Service('queueMulti', OmAivService, handle_queueMulti)
    elif op == "queuePickup":
        rospy.loginfo("running queuePickup")
        s6 = rospy.Service('queuePickup', OmAivService, handle_queuePickup)
    elif op == "queuePickupDropoff":
        rospy.loginfo("running queuePickupDropoff")
        s7 = rospy.Service('queuePickupDropoff', OmAivService, handle_queuePickupDropoff)
    elif op == "queueQuery":
        rospy.loginfo("running queueQuery")
        s8 = rospy.Service('queueQuery', OmAivService, handle_queueQuery)
    elif op == "queueShowRobot":
        rospy.loginfo("running queueShowRobot")
        s9 = rospy.Service('queueShowRobot', OmAivService, handle_queueShowRobot)

def payloadQuery(robot_name, slot_num):
    command = "payloadQuery {}".format(robot_name + " " + slot_num)
    command = command.encode('ascii')
    print "Running command: payloadQuery"
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
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as errormsg:
        print("Connection  failed")
        return errormsg

def payloadSlotCount(robot_name):
    command = "payloadSlotCount {}".format(robot_name)
    command = command.encode('ascii')
    print "Running command: payloadSlotCount"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndPayloadSlotCount" in rcv:
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

def queueCancel(type, value, echo_str, reason):
    command = "queueCancel {}".format(type + " " + value + " \"" + echo_str + "\" " + reason)
    command = command.encode('ascii')
    print "Running command: queueCancel"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "failed" in rcv:
                print rcv
                return rcv
                break
            if "queuecancel" in rcv:
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

def queueModify(id, type, value):
    command = "queueModify {}".format(id + " " + type + " " + value)
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

def queueMulti(arg):
    arg = arg.replace(',', '')
    arg = arg.replace('[', '')
    arg = arg.replace(']', '')
    arg = arg.replace("'", '')
    command = "queueMulti {}".format(arg)
    command = command.encode('ascii')
    print "Running command: queueMulti"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "QueueUpdate:" in rcv:
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

def queuePickup(goal_name, priority, job_id):
    command = "queuePickup {}".format(goal_name + " " + priority + " " + job_id)
    command = command.encode('ascii')
    print "Running command: queuePickup"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "QueueUpdate:" in rcv:
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

def queuePickupDropoff(goal1_name, goal2_name, priority1, priority2, job_id):
    command = "queuePickupDropoff {}".format(goal1_name + " " + goal2_name + " "
    + priority1 + " " + priority2 + " " + job_id)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "QueueUpdate" in rcv:
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

def queueQuery(type, value, echo_str):
    command = "queueQuery {}".format(type + " " + value + " " + echo_str)
    command = command.encode('ascii')
    print "Running command: queueQuery"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndQueueQuery" in rcv:
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

def queueShowRobot(robot_name):
    command = "queueShowRobot {}".format(robot_name)
    command = command.encode('ascii')
    print "Running command: queueShowRobot"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndQueueShowRobot" in rcv:
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
    rospy.init_node('em_service_servers')
    em_service_servers("payloadQuery")
    em_service_servers("payloadSlotCount")
    em_service_servers("queueCancel")
    em_service_servers("queueModify")
    em_service_servers("queueMulti")
    em_service_servers("queuePickup")
    em_service_servers("queuePickupDropoff")
    em_service_servers("queueQuery")
    em_service_servers("queueShowRobot")
    rospy.spin()
