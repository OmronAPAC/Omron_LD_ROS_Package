#!/usr/bin/env python
from om_aiv_util.socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
import threading
import time
import re
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.120"
# port = 7171
connecttcp.connect(str(ip_address), port)

from om_aiv_util.srv import OmAivService,OmAivServiceResponse

def handle_queueMulti(req):
    arg = str(req.a)
    rcv = queueMulti(arg)
    return rcv

def queueMulti_server():
    rospy.init_node('queueMulti_server')
    s = rospy.Service('queueMulti', OmAivService, handle_queueMulti)
    rospy.spin()

def queueMulti(arg):
    arg = arg.replace(',', '')
    arg = arg.replace('[', '')
    arg = arg.replace(']', '')
    arg = arg.replace("'", '')
    command = "queueMulti {}".format(arg)
    command = command.encode('ascii')
    print "Running command: queueMulti"
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "QueueUpdate:" in rcv:
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
    queueMulti_server()
