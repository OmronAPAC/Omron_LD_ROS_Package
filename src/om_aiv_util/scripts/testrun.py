#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
from queueDropoff_client import analogInputQueryRaw_client
a = "goal1"
b = ""
c = ""
print analogInputQueryRaw_client(a, b , c)
a = "goal4"
b = ""
c = ""
print analogInputQueryRaw_client(a, b, c)
