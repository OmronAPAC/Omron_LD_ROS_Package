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
ip_address = "172.21.5.125"
port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import Service4,Service4Response
import rospy

def handle_queueCancelLocal(req):
    global a, b, c, d
    a = req.a
    b = req.b
    c = req.c
    d = req.d
    queueCancelLocal()
    # return Service5Response(req.a + req.b + req.c + req.d + req.e)
    return rcv

def queueCancelLocal_server():
    rospy.init_node('queueCancelLocal_server')
    s = rospy.Service('queueCancelLocal', Service4, handle_queueCancelLocal)
    rospy.spin()

def queueCancelLocal():
    global rcv
    pub = rospy.Publisher('arcl_queueCancelLocal', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "queueCancelLocal {}".format(a + " " + b + " \"" + c + "\" " + d)
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
    queueCancelLocal_server()
