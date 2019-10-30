#!/usr/bin/env python
from colorama import init
init()
from colorama import Fore, Back, Style

from connectwifi import connecttowifi

# from socketconnection import socketconnect
# from socketconnection import data, s

from socketconnection_class import ConnectSocket, connecttcp

s = connecttcp.sock
import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024

# connecttcp.connect("172.21.5.33", 7171)
# connecttcp.sendpassword()

def status():
    global s
    global data
    pub = rospy.Publisher('arcl_status', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
   
    while not rospy.is_shutdown():
        command = "status"
        command = command.encode('ascii')
        s.send(command+b"\r\n")
        print(Style.RESET_ALL)
        print "Getting robot status..." 
        data = s.recv(BUFFER_SIZE)
        rcv = data.decode("utf-8")

        print(Fore.GREEN)
        print(Style.BRIGHT)
        pubout = str(data.splitlines())
        pub.publish(pubout)
        time.sleep(1)
        rospy.loginfo(rcv)
        print(Style.RESET_ALL)
        time.sleep(2)
        print(Fore.BLUE)
        print(Style.BRIGHT)
        # line = data.rpartition('\n')[-1]
        # print(line)
        # print(Style.RESET_ALL)
        for line in data.splitlines():
            if 'ExtendedStatusForHumans' in line:
                ExtendedStatusForHumans = line.split()[-1]
        print ExtendedStatusForHumans
        print(Style.RESET_ALL)
        

        # else:
        #     flag == 0
        #     data = s.recv(BUFFER_SIZE)
        #     rcv = data.decode("utf-8")

                
if __name__ == '__main__':
    try:
        status()
    except rospy.ROSInterruptException:
        pass








