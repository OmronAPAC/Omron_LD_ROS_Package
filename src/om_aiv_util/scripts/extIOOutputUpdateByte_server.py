#!/usr/bin/env python
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
import threading
import time
import re
import sys
from std_msgs.msg import String
BUFFER_SIZE = 1024
# ip_address = rospy.get_param("ip_address")
# port = rospy.get_param("port")
ip_address = "168.3.201.123"
port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import Service3,Service3Response
import rospy

def handle_extIOOutputUpdateByte(req):
    global a, b, c
    a = req.a
    b = req.b
    c = req.c
    extIOOutputUpdateByte()
    return rcv

def extIOOutputUpdateByte_server():
    rospy.init_node('extIOOutputUpdateByte_server')
    s = rospy.Service('extIOOutputUpdateByte', Service3, handle_extIOOutputUpdateByte)
    rospy.spin()

def extIOOutputUpdateByte():
    global rcv
    pub = rospy.Publisher('arcl_extIOOutputUpdateByte', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "extIOOutputUpdateByte {}".format(a + " " + b + " " + c)
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

if __name__ == "__main__":
    extIOOutputUpdateByte_server()
