#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def analogInputQueryRaw_client(a, b , c, d, e):
    rospy.wait_for_service('applicationFaultClear')
    try:
        add_two_ints = rospy.ServiceProxy('applicationFaultClear', Service5)
        resp1 = add_two_ints(a, b, c, d, e)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> <short description> <long description> <bool:drivingFault> <bool:criticalFault>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 6:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
        d = str(sys.argv[4])
        e = str(sys.argv[5])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    # analogInputQueryRaw_client(a, b, c, d, e)
    print analogInputQueryRaw_client(a, b , c, d, e)
