#!/usr/bin/env python
from connectwifi import connecttowifi
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
from doTask import DoTask, dt
from status import status
# s = connecttcp.sock
import socket
# import threading
import time
# import re
import sys
import rospy

rospy.init_node('node', anonymous=True)
# from std_msgs.msg import String
# BUFFER_SIZE = 1024

# connection_status = 
connecttcp.connect("172.21.5.33", 7171)

print connection_status

if connection_status != 1:
	rospy.loginfo("Connection Failed")
	rospy.loginfo(connection_status)
if connection_status == 1:
	rospy.loginfo("Connection Sucessful")

# dt.sendcommand("move 1000")
# s.shutdown(socket.SHUT_RDWR)
# s.close()
# connecttcp.connect("172.21.5.33", 7171)
# connecttcp.sendpassword("omron1")
# dt.sendcommand("move 200")

