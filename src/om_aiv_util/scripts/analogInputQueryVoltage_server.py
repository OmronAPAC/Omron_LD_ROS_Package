#!/usr/bin/env python
from socketconnection_class import ConnectSocket, connecttcp
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
# ip_address = "168.3.201.123"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import Service,ServiceResponse
import rospy

def handle_analogInputQueryVoltage(req):
    global text
    text = req.a
    analogInputQueryVoltage()
    # return ServiceResponse(req.a)
    return rcv

def analogInputQueryVoltage_server():
    rospy.init_node('analogInputQueryVoltage_server')
    s = rospy.Service('analogInputQueryVoltage', Service, handle_analogInputQueryVoltage)
    rospy.spin()

def analogInputQueryVoltage():
    global rcv
    pub = rospy.Publisher('arcl_analogInputQueryVoltage', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    command = "analogInputQueryVoltage {}".format(text)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "AnalogInputVoltage:" in rcv:
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

    except socket.error as e:
        print("Connection  failed")
        return e

if __name__ == "__main__":
    analogInputQueryVoltage_server()
