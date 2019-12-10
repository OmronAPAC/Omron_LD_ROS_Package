#! /usr/bin/env python

import rospy
import actionlib
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from om_aiv_navigation.msg import ActionAction, ActionFeedback, ActionResult
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
from om_aiv_util.socketconnection_class import ConnectSocket, connecttcp
global s
socket = connecttcp.sock
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.123"
# port = 7171
connecttcp.connect(str(ip_address), port)

class ActionServer():
    action_command = None
    def dock(self,result,feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Docked" in rcv:
                    break
                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    rcv = str(rcv.replace("\r\n",""))
                    feedback.received_data = rcv
                    self.a_server.publish_feedback(feedback)

        except socket.error as e:
            print("Connection  failed")
            return e
        while not rospy.is_shutdown():
            for line in rcv.splitlines():
                #print required data
                if 'Docked' in line:
                    doTask = line.split("Docked")
                    rospy.loginfo(",Docked".join(doTask)[1:])
                    success = True
                    rcv = str(rcv.splitlines())
                    result.status = (",Docked".join(doTask)[1:])
                    self.a_server.set_succeeded(result)
                    return(0)

    def doTask(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            feedback.received_data = rcv
            print rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Completed" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Completed' in line:
                            doTask = line.split("Completed")
                            rospy.loginfo(",Completed".join(doTask)[1:])
                            rcv = str(rcv.splitlines())
                            result.status = (",Completed".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
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

    def executeMacro(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Executing" in rcv:
                    time.sleep(3)
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    rcv = str(rcv.replace("\r\n",""))
                    feedback.received_data = rcv
                    self.a_server.publish_feedback(feedback)
                    break
                if "Completed" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Completed macro' in line:
                            executeMacro = line.split("Completed macro")
                            rospy.loginfo(",Completed macro".join(executeMacro)[1:])
                            # pub.publish(''.join(executeMacro))
                            success = True
                            rcv = str(rcv.splitlines())
                            result.status = (",Completed macro".join(executeMacro)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                            break
                if "Failed" in rcv:
                    print "Failed to execute macro"
                    result.status = "Failed to execute macro"
                    self.a_server.set_succeeded(result)
                    return(0)
                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    feedback.received_data = rcv
                    self.a_server.publish_feedback(feedback)

        except Exception as e:
            rospy.logerr(e)
            result.status = str(e)
            self.a_server.set_succeeded(result)
            return e

        data = socket.recv(BUFFER_SIZE)
        rcv = rcv + data.encode('ascii', 'ignore')
        print rcv

        if success:
            self.a_server.set_succeeded(result)

    def goTo(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Arrived" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Arrived' in line:
                            doTask = line.split("Arrived")
                            rospy.loginfo(",Arrived".join(doTask)[1:])
                            rcv = str(rcv.splitlines())
                            result.status = (",Arrived".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                if "Failed" in rcv:
                    print "Failed to go to goal"
                    result.status = "Failed to go to goal"
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

    def patrol(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Finished patrolling" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Finished patrolling' in line:
                            doTask = line.split("Finished")
                            rospy.loginfo(",Finished".join(doTask)[1:])
                            rcv = str(rcv.splitlines())
                            result.status = (",Finished".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                            break
                if "Failed" in rcv:
                    print "Failed to patrol"
                    result.status = "Failed to patrol"
                    self.a_server.set_succeeded(result)
                    return(0)
                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    feedback.received_data = rcv
                    self.a_server.publish_feedback(feedback)

        except Exception as e:
            rospy.logerr(e)
            result.status = str(e)
            self.a_server.set_succeeded(result)
            return e

    def patrolOnce(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Finished patrolling" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Finished patrolling' in line:
                            doTask = line.split("Finished")
                            rospy.loginfo(",Finished".join(doTask)[1:])
                            rcv = str(rcv.splitlines())
                            result.status = (",Finished".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                            break
                if "Failed" in rcv:
                    print "Failed to patrol"
                    result.status = "Failed to patrol"
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

    def patrolResume(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Finished patrolling" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Finished patrolling' in line:
                            doTask = line.split("Finished")
                            rospy.loginfo(",Finished".join(doTask)[1:])
                            rcv = str(rcv.splitlines())
                            result.status = (",Finished".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                            break
                if "Failed" in rcv:
                    print "Failed to patrol"
                    result.status = "Failed to patrol"
                    self.a_server.set_succeeded(result)
                    return(0)
                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    rcv = str(rcv.replace("\r\n",""))

        except Exception as e:
            rospy.logerr(e)
            result.status = str(e)
            self.a_server.set_succeeded(result)
            return e

    def play(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Playing" in rcv:
                    for line in rcv.splitlines():
                        #print required data
                        if 'Playing' in line:
                            doTask = line.split("Playing")
                            rospy.loginfo(",Playing".join(doTask)[1:])
                            rcv = str(rcv.splitlines())
                            result.status = (",Playing".join(doTask)[1:])
                            self.a_server.set_succeeded(result)
                            return(0)
                            break
                if "SetupError:" in rcv:
                    print "Failed to play file"
                    result.status = "Failed to play file"
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

    def queueDropoff(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Completed" in rcv:
                    print rcv
                    rcv = str(rcv.replace("\r\n",""))
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
                if "Failed" in rcv:
                    print rcv
                    result.status = (rcv)
                    self.a_server.set_succeeded(result)
                    return(0)
                    break
                else:
                    data = socket.recv(BUFFER_SIZE)
                    rcv = rcv + data.encode('ascii', 'ignore')
                    rcv = str(rcv.replace("\r\n",""))
                    feedback.received_data = rcv
                    self.a_server.publish_feedback(feedback)

        except socket.error as e:
            print("Connection  failed")
            return e

    def stop(self, result, feedback):
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
                            success = True
                            rcv = str(rcv.splitlines())
                            result.status = (",Stopped".join(doTask)[1:])
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

    def undock(self, result, feedback):
        try:
            data = socket.recv(BUFFER_SIZE)
            rcv = data.encode('ascii', 'ignore')
            rcv = str(rcv.replace("\r\n",""))
            feedback.received_data = rcv
            self.a_server.publish_feedback(feedback)
            while not rospy.is_shutdown():
                #check for required data
                if "Undocked" in rcv:
                    break
                if "Undocking" in rcv:
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
                if 'Undocked' in line:
                    # doTask = line.split("Undocked")
                    # rospy.loginfo(",Undocked".join(doTask)[1:])
                    rospy.loginfo(rcv)
                    # rcv = str(rcv.splitlines())
                    # result.status = (",Undocked".join(doTask)[1:])
                    result.status = rcv
                    self.a_server.set_succeeded(result)
                    return(0)
                if 'Undocking' in line:
                    # doTask = line.split("Undocked")
                    # rospy.loginfo(",Undocked".join(doTask)[1:])
                    rospy.loginfo(rcv)
                    # rcv = str(rcv.splitlines())
                    # result.status = (",Undocked".join(doTask)[1:])
                    result.status = rcv
                    self.a_server.set_succeeded(result)
                    return(0)

    def __init__(self, action_name):
        self.action_command = action_name
        self.a_server = actionlib.SimpleActionServer(
            action_name, ActionAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def execute_cb(self, goal):
        success = True
        feedback = ActionFeedback()
        result = ActionResult()
        task = goal.goal_goal
        print(Style.RESET_ALL)
        print(Fore.GREEN)
        #send command to arcl
        command = self.action_command + " " + task
        print command
        command = command.encode('ascii')
        socket.send(command+b"\r\n")
        if self.action_command == "doTask":
            self.doTask(result, feedback)
        if self.action_command == "dock":
            self.dock(result, feedback)
        if self.action_command == "executeMacro":
            self.executeMacro(result, feedback)
        if self.action_command == "goTo":
            self.goTo(result, feedback)
        if self.action_command == "patrol":
            self.patrol(result, feedback)
        if self.action_command == "patrolOnce":
            self.patrolOnce(result, feedback)
        if self.action_command == "patrolResume":
            self.patrolOnce(result, feedback)
        if self.action_command == "play":
            self.play(result, feedback)
        if self.action_command == "queueDropoff":
            self.queueDropoff(result, feedback)
        if self.action_command == "stop":
            self.stop(result, feedback)
        if self.action_command == "undock":
            self.undock(result, feedback)

if __name__ == "__main__":
    rospy.init_node("doTask_action_server")
    s = ActionServer("doTask")
    s = ActionServer("dock")
    s = ActionServer("executeMacro")
    s = ActionServer("goTo")
    s = ActionServer("patrol")
    s = ActionServer("patrolOnce")
    s = ActionServer("patrolResume")
    s = ActionServer("play")
    s = ActionServer("queueDropoff")
    s = ActionServer("stop")
    s = ActionServer("undock")
    rospy.spin()
