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

def handle_mapObjectTypeInfo(req):
    global text
    text = req.a
    mapObjectTypeInfo()
    # return ServiceResponse(req.a)
    return rcv

def mapObjectTypeInfo_server():
    rospy.init_node('mapObjectTypeInfo_server')
    s = rospy.Service('mapObjectTypeInfo', Service, handle_mapObjectTypeInfo)
    rospy.spin()

def mapObjectTypeInfo():
    global rcv
    pub = rospy.Publisher('arcl_mapObjectTypeInfo', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "mapObjectTypeInfo {}".format(text)
    command = command.encode('ascii')
    print "Running command: ", command
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of MapObjectTypeInfo" in rcv:
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
    mapObjectTypeInfo_server()
