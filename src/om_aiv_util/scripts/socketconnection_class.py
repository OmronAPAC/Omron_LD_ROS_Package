#!/usr/bin/env python
import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024
class ConnectSocket(object):

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(5)
        else:
            self.sock = sock

    #send password to arcl to login to server
    def sendpassword(self, password="omron1"): 
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
            while not rospy.is_shutdown():
                if "End of commands" in rcv:
                    print("Connected")
                    break
                else:
                    data = self.sock.recv(BUFFER_SIZE)
                    rcv = data.decode("utf-8")
            return 1    
                       
        except socket.error as e:
            print("Connection  failed")
            return e

    #host = ip address        
    def connect(self, host, port):

        try:
            self.sock.connect((host, port))

        except socket.error as e:
            print("Connection  failed")
            return e

        status = self.sendpassword()
        return status


        
    
connecttcp = ConnectSocket()


connecttcp.connect("172.21.5.33", 7171)
# connecttcp.sendpassword("omron1")


    # connecttcp.sendcommand("status")
    # def sendcommand(self, command):
    #     global rcv
    #     BUFFER_SIZE = 1024
    #     flag = 0
    #     data = self.sock.recv(BUFFER_SIZE)
    #     rcv = data.decode("utf-8")
    #     while (flag == 0):
    #         if "End of commands" in rcv:
    #             flag == 1
    #             while not rospy.is_shutdown():
    #                 self.command = command
    #                 command = command.encode('ascii')
    #                 self.sock.send(command+b"\r\n")
    #                 print "Running Command: ", command  
    #                 time.sleep(1)
    #                 data = self.sock.recv(BUFFER_SIZE)
    #                 rcv = data.decode("utf-8")
    #                 time.sleep(1)
    #                 print(rcv)

                
    #                 # pubout = str(data.splitlines())
    #                 # pub.publish(pubout)
    #                 # time.sleep(1)
    #                 # rospy.loginfo(rcv)

    #                 # time.sleep(2)
    #                 # exit(0)

    #         else:
    #             flag == 0
    #             data = self.sock.recv(BUFFER_SIZE)
    #             rcv = data.decode("utf-8")





