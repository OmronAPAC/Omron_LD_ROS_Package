#!/usr/bin/env python
import socket
import threading
import time
import re
import sys
import rospy
import datetime
from std_msgs.msg import String
BUFFER_SIZE = 1024
class ConnectSocket(object):

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(60)
        else:
            self.sock = sock

    #send password to arcl to login to server
    def sendpassword(self, password="adept"):
        global data
        BUFFER_SIZE = 1024
        data = self.sock.recv(BUFFER_SIZE)
        self.password = password
        pswd = password+"\r\n"
        pswd = pswd.encode('ascii')
        self.sock.send(pswd)
        try:
            data = self.sock.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
            #wait until server prints out full list of commands
            while not rospy.is_shutdown():
                if "End of commands" in rcv:
                    print("Connected to robot")
                    break
                else:
                    data = self.sock.recv(BUFFER_SIZE)
                    rcv = data.decode("utf-8")
            return 1

        except socket.error as e:
            print("Connection to robot failed")
            return e

    #host = ip address
    def connect(self, host, port):
        #try to connect to server
        try:
            self.sock.connect((host, port))
            print datetime.datetime.now(),"connecting to", host 

        except socket.error as e:
            print("Connection  failed")
            return e
        #send password if connection successful
        status = self.sendpassword()
        return status




connecttcp = ConnectSocket()
