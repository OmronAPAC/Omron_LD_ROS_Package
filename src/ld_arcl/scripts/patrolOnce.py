#!/usr/bin/env python
from connectwifi import connecttowifi
from connectwifi import manager, connection_path, settings_path, connection_params, connection_path, manager_props
from socketconnection import socketconnect
from socketconnection import data, s

import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024

def talker():
    global manager
    global s
    global data
    pub = rospy.Publisher('arcl_patrolOnce', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    socketconnect()

    cmd = raw_input("Enter the name of the route you want the robot to patrol once. Enter an optional index value. No value or 0 instructs the robot to start at the beginning of the route.\r\n")
    
    global rcv
    global i
    i = 1
    flag = 0
    # data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while (flag == 0):
        if "End of commands" in rcv:
            flag == 1
            while not rospy.is_shutdown():
                command = "patrolOnce {}".format(cmd)
                command = command.encode('ascii')
                s.send(command+b"\r\n")
                print "running command:" ,command
                time.sleep(1)
                data = s.recv(BUFFER_SIZE)
                rcv = data.decode("utf-8")
                
                pubout = str(data.splitlines())
                pub.publish(pubout)
                time.sleep(1)
                rospy.loginfo(rcv)
                time.sleep(2)
                exit(0)

        else:
            flag == 0
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")
                
if __name__ == '__main__':
    try:
        connecttowifi()
        talker()
    except rospy.ROSInterruptException:
        pass









