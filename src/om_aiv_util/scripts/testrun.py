#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import String
from om_aiv_util.srv import *
from queueDropoff_client import analogInputQueryRaw_client

rospy.init_node('test')
battery_level = rospy.wait_for_message('/ldarcl_status_state_of_charge', Float32)
print battery_level
battery_level = str(battery_level)
battery_level = battery_level.strip("data:")
battery_level = float(battery_level)
if battery_level <= 50:
        print "battery less than 50%"
        exit(0)

a = "goal1"
b = ""
c = ""
print analogInputQueryRaw_client(a, b , c)

a = "goal4"
b = ""
c = ""
print analogInputQueryRaw_client(a, b, c)
