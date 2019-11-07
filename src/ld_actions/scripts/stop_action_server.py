#! /usr/bin/env python

import rospy
import actionlib
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from ld_actions.msg import StopAction, StopFeedback, StopResult
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
# ip_address = rospy.get_param("ip_address")
# port = rospy.get_param("port")
ip_address = "172.21.5.125"
port = 7171
connecttcp.connect(str(ip_address), port)

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "stop", StopAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = StopFeedback()
        result = StopResult()
        task = goal.goal_stop
        rate = rospy.Rate(10) # 10hz
        print(Style.RESET_ALL)
        print(Fore.GREEN)

        #send command to arcl
        command = task
        command = command.encode('ascii')
        socket.send(command+b"\r\n")
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Stopped" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Stopped' in line:
                            doTask = line.split("Stopped")
                            rospy.loginfo(",Stopped".join(doTask)[1:])
                            rate.sleep()
                            success = True
                            rcv = str(rcv.splitlines())
                            result.status = (",Stopped".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                            break

                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')

        except Exception as e:
            rospy.logerr(e)
            result.status = str(e)
            self.a_server.set_succeeded(result)
            return e

        if success:
            self.a_server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("stop_action_server")
    s = ActionServer()
    rospy.spin()
