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

def handle_queuePickupDropoff(req):
    goal1_name = req.a[0]
    goal2_name = req.a[1]
    priority1 = req.a[2]
    priority2 = req.a[3]
    job_id = req.a[4]
    rcv = queuePickupDropoff(goal1_name, goal2_name, priority1, priority2, job_id)
    return rcv

def queuePickupDropoff_server():
    rospy.init_node('queuePickupDropoff_server')
    s = rospy.Service('queuePickupDropoff', OmAivService, handle_queuePickupDropoff)
    rospy.spin()

def queuePickupDropoff(goal1_name, goal2_name, priority1, priority2, job_id):
    command = "queuePickupDropoff {}".format(goal1_name + " " + goal2_name + " "
    + priority1 + " " + priority2 + " " + job_id)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "QueueUpdate" in rcv:
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
    queuePickupDropoff_server()
