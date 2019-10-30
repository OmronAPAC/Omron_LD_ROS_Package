#!/usr/bin/env python
import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024


def socketconnect():
	global s
	global data
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(5)
	# print("socket timeout:" , s.gettimeout(),"s")
	TCP_IP = "172.21.5.33"
	TCP_PORT = 7171

	s.connect((TCP_IP, TCP_PORT))
	data = s.recv(BUFFER_SIZE)
	password = "omron1"
	pswd = password+"\r\n"
	pswd = pswd.encode('ascii')
	s.send(pswd)

socketconnect()