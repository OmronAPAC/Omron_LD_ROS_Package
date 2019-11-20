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
# ip_address = "172.21.5.125"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import Service2,Service2Response

def handle_payloadSet(req):
    global a, b
    a = req.a
    b = req.b
    payloadSet()
    return rcv

def payloadSet_server():
    rospy.init_node('payloadSet_server')
    s = rospy.Service('payloadSet', Service2, handle_payloadSet)
    rospy.spin()

def payloadSet():
    global rcv
    pub = rospy.Publisher('arcl_payloadSet', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "payloadSet {}".format(a + " " + b)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "successfully set" in rcv:
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
    payloadSet_server()
