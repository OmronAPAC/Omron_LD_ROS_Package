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

from om_aiv_util.srv import Service3,Service3Response

def handle_queueModifyLocal(req):
    global a, b, c
    a = req.a
    b = req.b
    c = req.c
    queueModifyLocal()
    # return Service5Response(req.a + req.b + req.c + req.d + req.e)
    return rcv

def queueModifyLocal_server():
    rospy.init_node('queueModifyLocal_server')
    s = rospy.Service('queueModifyLocal', Service3, handle_queueModifyLocal)
    rospy.spin()

def queueModifyLocal():
    global rcv
    pub = rospy.Publisher('arcl_queueModifyLocal', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "queueModifyLocal {}".format(a + " " + b + " " + c)
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

if __name__ == "__main__":
    queueModifyLocal_server()
