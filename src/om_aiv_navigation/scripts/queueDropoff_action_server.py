#! /usr/bin/env python

import rospy
import actionlib
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from om_aiv_navigation.msg import QueueDropoffAction, QueueDropoffFeedback, QueueDropoffResult
import math
import numpy as np
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 2056
#import socketconnection class to connect to robot
#requires socketconnection_class.py file in the same folder
from socketconnection_class import ConnectSocket, connecttcp
global s
socket = connecttcp.sock
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "168.3.201.123"
# port = 7171
connecttcp.connect(str(ip_address), port)

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "queueDropoff", QueueDropoffAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = QueueDropoffFeedback()
        result = QueueDropoffResult()
        goal = goal.goal_queueDropoff
        rate = rospy.Rate(10) # 10hz
        print(Style.RESET_ALL)
        print(Fore.GREEN)

        #send command to arcl
        command = "queueDropoff {}".format(goal)
        command = command.encode('ascii')
        socket.send(command+b"\r\n")
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Completed" in rcv:
                    print rcv
                    result.status = (rcv)
                    self.a_server.set_succeeded(result)
                    return(0)
                    break
                if "CommandErrorDescription" in rcv:
                    print rcv
                    result.status = (rcv)
                    self.a_server.set_succeeded(result)
                    return(0)
                    break
                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    feedback.received_data = rcv
                    self.a_server.publish_feedback(feedback)

        except socket.error as e:
            print("Connection  failed")
            return e

        if success:
            self.a_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("queueDropoff_action_server")
    s = ActionServer()
    rospy.spin()
