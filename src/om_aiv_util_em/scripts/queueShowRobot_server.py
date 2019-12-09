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
# ip_address = "172.21.5.120"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import OmAivService,OmAivServiceResponse

def handle_queueShowRobot(req):
    robot_name = req.a[0]
    rcv = queueShowRobot(robot_name)
    return rcv

def queueShowRobot_server():
    rospy.init_node('queueShowRobot_server')
    s = rospy.Service('queueShowRobot', OmAivService, handle_queueShowRobot)
    rospy.spin()

def queueShowRobot(robot_name):
    command = "queueShowRobot {}".format(robot_name)
    command = command.encode('ascii')
    print "Running command: queueShowRobot"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndQueueShowRobot" in rcv:
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
    queueShowRobot_server()
