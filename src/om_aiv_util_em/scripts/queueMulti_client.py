#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def analogInputQueryRaw_client(a):
    rospy.wait_for_service('createInfo')
    try:
        add_two_ints = rospy.ServiceProxy('createInfo', Service)
        resp1 = add_two_ints(a)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <number of goals> <number of fields per goal> <goal1> <goal1 args> <goal2> <goal2 args> ... <goalN> <goalN args> [jobid]"%sys.argv[0]

if __name__ == "__main__":
    a = str(sys.argv[1:])
    print "running command"
    a = a.replace(',', '')
    a = a.replace('[', '')
    a = a.replace(']', '')
    a = a.replace("'", '')
    # print "Requesting", x
    print analogInputQueryRaw_client(a)
