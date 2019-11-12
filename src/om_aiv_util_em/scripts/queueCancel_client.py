#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueCancel_client(a, b , c, d):
    rospy.wait_for_service('queueCancel')
    try:
        add_two_ints = rospy.ServiceProxy('queueCancel', Service4)
        resp1 = add_two_ints(a, b, c, d)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <type> <value> [echoString or \"default\"] [reason]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
        d = str(sys.argv[4])
    elif len(sys.argv) == 3:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = ""
        d = ""

    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueCancel_client(a, b , c, d)
