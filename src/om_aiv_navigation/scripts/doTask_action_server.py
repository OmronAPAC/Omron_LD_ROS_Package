#! /usr/bin/env python

import rospy
import actionlib
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from om_aiv_navigation.msg import DoTaskAction, DoTaskFeedback, DoTaskResult
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
            "doTask", DoTaskAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = DoTaskFeedback()
        result = DoTaskResult()
        task = goal.goaltask
        rate = rospy.Rate(10)
        print(Style.RESET_ALL)
        print(Fore.GREEN)

        #send command to arcl
        command = "doTask {}".format(task)
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
                    for line in rcv.splitlines():
                        #print required data
                        if 'Completed' in line:
                            doTask = line.split("Completed")
                            rospy.loginfo(",Completed".join(doTask)[1:])

                            rate.sleep()
                            success = True
                            rcv = str(rcv.splitlines())
                            result.status = (",Completed".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            break
                if "Failed" in rcv:
                    print "Failed to do task"
                    result.status = "Failed to do task"
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
    rospy.init_node("doTask_action_server")
    s = ActionServer()
    rospy.spin()
