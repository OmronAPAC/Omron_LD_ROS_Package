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

from om_aiv_util.srv import Service2,Service2Response
import rospy

def handle_extIOInputUpdate(req):
    global a, b
    a = req.a
    b = req.b
    extIOInputUpdate()
    # return Service5Response(req.a + req.b + req.c + req.d + req.e)
    return rcv

def extIOInputUpdate_server():
    rospy.init_node('extIOInputUpdate_server')
    s = rospy.Service('extIOInputUpdate', Service2, handle_extIOInputUpdate)
    rospy.spin()

def extIOInputUpdate():
    global rcv
    pub = rospy.Publisher('arcl_extIOInputUpdate', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "extIOInputUpdate {}".format(a + " " + b)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "extIOInputUpdate:" in rcv:
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
    extIOInputUpdate_server()
