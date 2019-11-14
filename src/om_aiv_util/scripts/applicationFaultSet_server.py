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

from om_aiv_util.srv import Service5,Service5Response
import rospy

def handle_applicationFaultClear(req):
    global a, b, c, d, e
    a = req.a
    b = req.b
    c = req.c
    d = req.d
    e = req.e
    applicationFaultClear()
    # return Service5Response(req.a + req.b + req.c + req.d + req.e)
    return rcv

def applicationFaultClear_server():
    rospy.init_node('applicationFaultClear_server')
    s = rospy.Service('applicationFaultClear', Service5, handle_applicationFaultClear)
    rospy.spin()

def applicationFaultClear():
    global rcv
    pub = rospy.Publisher('arcl_applicationFaultClear', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "applicationFaultSet {}".format(a + " " + b + " " + c + " " + d + " " + e)
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

if __name__ == "__main__":
    applicationFaultClear_server()
