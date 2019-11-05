#! /usr/bin/env python

import rospy
import actionlib
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from ld_actions.msg import DockAction, DockFeedback, DockResult
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
ip_address = "172.21.5.123"
port = 7171
connecttcp.connect(str(ip_address), port)

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "dock", DockAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        global rcv
        success = True
        last_dish_washed = ''
        feedback = DockFeedback()
        result = DockResult()
        rate = rospy.Rate(1)
        for i in range(1, goal.isdocked):
            i == 1
            if self.a_server.is_preempt_requested():
                self.a_server.set_preempted()
                success = False
                break

            dock()
            feedback.received_data = rcv
            print(Style.RESET_ALL)
            print(Fore.YELLOW)
            print i
            print(Style.RESET_ALL)

            self.a_server.publish_feedback(feedback)
            rate.sleep()
        if success:
            self.a_server.set_succeeded(result)




def dock():
    global rcv
    global i
    pub = rospy.Publisher('ldarcl_dock', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    print(Style.RESET_ALL)
    print(Fore.GREEN)
    print "Docking..."
    #send command to arcl
    command = "dock"
    command = command.encode('ascii')
    socket.send(command+b"\r\n")
    try:
        data = socket.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "DockingState:" in rcv:
                break
            else:
                data = socket.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e
    while not rospy.is_shutdown():
        for line in rcv.splitlines():
            #print required data
            if 'DockingState:' in line:
                i = 1
                dock = line.split("DockingState:")
                rospy.loginfo(",DockingState:".join(dock)[1:])
                pub.publish(''.join(dock))
                rate.sleep()
                data = socket.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

                if 'Docked' in line:
                    i = 4
                    success = True
                    result.docking_status.append(rcv)
                    self.a_server.set_succeeded(result)
                    break

if __name__ == "__main__":
    rospy.init_node("action_server")
    s = ActionServer()
    rospy.spin()
