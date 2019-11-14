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
import rospy

def handle_getDataStoreGroupInfo(req):
    global text
    print "Returning", req.a
    text = req.a
    getDataStoreGroupInfo()
    # return ServiceResponse(req.a)
    return rcv

def getDataStoreGroupInfo_server():
    rospy.init_node('getDataStoreGroupInfo_server')
    s = rospy.Service('getDataStoreGroupInfo', Service, handle_getDataStoreGroupInfo)
    rospy.spin()

def getDataStoreGroupInfo():
    global rcv
    pub = rospy.Publisher('arcl_getDataStoreGroupInfo', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "getDataStoreGroupInfo {}".format(text)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "EndOfGetDataStoreGroupInfo" in rcv:
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
    getDataStoreGroupInfo_server()
