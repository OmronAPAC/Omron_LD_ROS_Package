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

from om_aiv_util.srv import Service,ServiceResponse
import rospy

def handle_outputOn(req):
    global a
    a = req.a
    outputOn()
    return rcv

def outputOn_server():
    rospy.init_node('outputOn_server')
    s = rospy.Service('outputOn', Service, handle_outputOn)
    rospy.spin()

def outputOn():
    global rcv
    pub = rospy.Publisher('arcl_outputOn', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "outputOn {}".format(a)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "Output:" in rcv:
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
    outputOn_server()
