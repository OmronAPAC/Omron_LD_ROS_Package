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

from om_aiv_util.srv import Service,ServiceResponse

def handle_payloadSlotCountLocal(req):
    payloadSlotCountLocal()
    return rcv

def payloadSlotCountLocal_server():
    rospy.init_node('payloadSlotCountLocal_server')
    s = rospy.Service('payloadSlotCountLocal', Service, handle_payloadSlotCountLocal)
    rospy.spin()

def payloadSlotCountLocal():
    global rcv
    pub = rospy.Publisher('arcl_payloadSlotCountLocal', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "payloadSlotCountLocal"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndPayloadSlotCount" in rcv:
                print rcv
                return rcv
                break
            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e

if __name__ == "__main__":
    payloadSlotCountLocal_server()
