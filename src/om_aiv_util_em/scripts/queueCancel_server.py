#!/usr/bin/env python
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
# ip_address = "172.21.5.120"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import OmAivService,OmAivServiceResponse

def handle_queueCancel(req):
    type = req.a[0]
    value = req.a[1]
    echo_str = req.a[2]
    reason = req.a[3]
    rcv = queueCancel(type, value, echo_str, reason)
    return rcv

def queueCancel_server():
    rospy.init_node('queueCancel_server')
    s = rospy.Service('queueCancel', OmAivService, handle_queueCancel)
    rospy.spin()

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

if __name__ == "__main__":
    queueCancel_server()
