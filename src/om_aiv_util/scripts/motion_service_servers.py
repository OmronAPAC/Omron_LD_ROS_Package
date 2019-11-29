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

def hardware_servers(op):
    if op == "queueCancelLocal":
        rospy.loginfo("running queueCancelLocal")
        s1 = rospy.Service('queueCancelLocal', OmAivService, handle_queueCancelLocal)
    elif op == "QueryRaw":
        rospy.loginfo("running QueryRaw")
        s2 = rospy.Service('analogInputQueryRaw', OmAivService, handle_analogInputQueryRaw)

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


if __name__ == "__main__":
    rospy.init_node('hardware_servers')
    hardware_servers("queueCancelLocal")
    rospy.spin()
