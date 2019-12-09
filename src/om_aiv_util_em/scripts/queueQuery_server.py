#!/usr/bin/env python
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
# ip_address = "172.21.5.120"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import OmAivService,OmAivServiceResponse

def handle_queueQuery(req):
    type = req.a[0]
    value = req.a[1]
    echo_str = req.a[2]
    rcv = queueQuery(type, value, echo_str)
    return rcv

def queueQuery_server():
    rospy.init_node('queueQuery_server')
    s = rospy.Service('queueQuery', OmAivService, handle_queueQuery)
    rospy.spin()

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

if __name__ == "__main__":
    queueQuery_server()
