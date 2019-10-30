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

class commandtosend:
     command = "enableMotors"
sendcommand = commandtosend()

def talker():
    global manager
    global s
    global data
    pub = rospy.Publisher('arcl_enableMotors', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
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
                sendcommand.command = sendcommand.command.encode('ascii')
                s.send(sendcommand.command+b"\r\n")
                print "Enabling Motors..."
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
        talker()
    except rospy.ROSInterruptException:
        pass



