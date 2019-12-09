#!/usr/bin/env python
from om_aiv_util.socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
import threading
import time
import re
import rospy
import sys
from std_msgs.msg import String
BUFFER_SIZE = 1024
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.120"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import OmAivService,OmAivServiceResponse

def handle_payloadQuery(req):
    robot_name = req.a[0]
    slot_num = req.a[1]
    rcv = payloadQuery(robot_name, slot_num)
    return rcv

def payloadQuery_server():
    rospy.init_node('payloadQuery_server')
    s = rospy.Service('payloadQuery', OmAivService, handle_payloadQuery)
    rospy.spin()

def payloadQuery(robot_name, slot_num):
    command = "payloadQuery {}".format(robot_name + " " + slot_num)
    command = command.encode('ascii')
    print "Running command: payloadQuery"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndPayloadQuery" in rcv:
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
    payloadQuery_server()
