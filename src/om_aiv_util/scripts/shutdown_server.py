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

def handle_shutdown(req):
    global fault
    fault = req.a
    shutdown()
    # return ServiceResponse(req.a)
    return rcv

def shutdown_server():
    rospy.init_node('shutdown_server')
    s = rospy.Service('shutdown', Service, handle_shutdown)
    rospy.spin()

def shutdown():
    global rcv
    pub = rospy.Publisher('arcl_shutdown', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    command = "shutdown"
    print "Running command: ", command
    command = command.encode('ascii')
    s.send(command+b"\r\n")

    except socket.error as e:
        print("Connection  failed")
        return e

if __name__ == "__main__":
    shutdown_server()
