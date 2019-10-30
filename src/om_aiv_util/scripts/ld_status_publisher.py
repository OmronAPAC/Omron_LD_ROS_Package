#!/usr/bin/env python
## publishes std_msgs/Strings messages
## to the 5 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
import socket
import threading
import time
import re
import sys
BUFFER_SIZE = 1024
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock

def extended_status_for_humans():
    pub = rospy.Publisher('ldarcl_status_extended_status_for_humans', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    command = "status"
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    print(Style.RESET_ALL)
    print "Getting robot status..." 
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")

    print(Fore.BLUE)
    print(Style.BRIGHT)
    for line in data.splitlines():
        if 'ExtendedStatusForHumans' in line:
            ExtendedStatusForHumans = line.split()[-1]
    

    extended_status_for_humans = ExtendedStatusForHumans
    
    rospy.loginfo(extended_status_for_humans)
    pub.publish(extended_status_for_humans)
    rate.sleep()

def status():
    pub = rospy.Publisher('ldarcl_status_status', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    status = "Status: DockingState: Docked ForcedState: Unforced ChargeState: Bulk"
    rospy.loginfo(status)
    pub.publish(status)
    rate.sleep()

def state_of_charge():
    pub = rospy.Publisher('ldarcl_status_state_of_charge', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    state_of_charge = "StateOfCharge: 100.0"
    rospy.loginfo(state_of_charge)
    pub.publish(state_of_charge)
    rate.sleep()

def location():
    pub = rospy.Publisher('ldarcl_status_location', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    location = "Location: 1264 37074 -89 %s" % rospy.get_time()
    rospy.loginfo(location)
    pub.publish(location)
    rate.sleep()

def localization_score():
    pub = rospy.Publisher('ldarcl_status_localization_score', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    localization_score = "LocalizationScore: 0.743697 %s" % rospy.get_time()
    rospy.loginfo(localization_score)
    pub.publish(localization_score)
    rate.sleep()

def temperature():
    pub = rospy.Publisher('ldarcl_status_temperature', String, queue_size=10)
    rospy.init_node('ld_status', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    temperature = "Temperature: 30 %s" % rospy.get_time()
    rospy.loginfo(temperature)
    pub.publish(temperature)
    rate.sleep()

if __name__ == '__main__':
    try:
        extended_status_for_humans()   
        # while not rospy.is_shutdown():
        #     extended_status_for_humans()
        #     status()
        #     state_of_charge()
        #     location()
        #     localization_score()
        #     temperature()
    except rospy.ROSInterruptException:
        pass
