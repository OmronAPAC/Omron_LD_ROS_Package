#! /usr/bin/env python

import rospy
import actionlib
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from ld_actions.msg import PlayAction, PlayFeedback, PlayResult
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
            "play", PlayAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = PlayFeedback()
        result = PlayResult()
        task = goal.goal_play
        rate = rospy.Rate(10) # 10hz
        print(Style.RESET_ALL)
        print(Fore.GREEN)

        #send command to arcl
        command = "play {}".format(task)
        command = command.encode('ascii')
        socket.send(command+b"\r\n")
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Playing" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Playing' in line:
                            i = 1
                            doTask = line.split("Playing")
                            rospy.loginfo(",Playing".join(doTask)[1:])
                            rate.sleep()
                            success = True
                            rcv = str(rcv.splitlines())
                            result.status = (",Playing".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            break
                if "SetupError:" in rcv:
                    print "Failed to play file ", task
                    result.status = "Failed to play file ", task
                    self.a_server.set_succeeded(result)
                    return(0)
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
    rospy.init_node("play_action_server")
    s = ActionServer()
    rospy.spin()
