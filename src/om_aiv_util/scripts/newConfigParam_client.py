#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def newConfigParam_client(a, b , c, d, e, f, g, h, i):
    rospy.wait_for_service('newConfigParam')
    try:
        add_two_ints = rospy.ServiceProxy('newConfigParam', Service9)
        resp1 = add_two_ints(a, b, c, d, e, f, g, h, i)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s<section> <name> <description> <priority_level> <type> <default_value> <min> <max> <DisplayHint>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 10:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
        d = str(sys.argv[4])
        e = str(sys.argv[5])
        f = str(sys.argv[6])
        g = str(sys.argv[7])
        h = str(sys.argv[8])
        i = str(sys.argv[9])

    else:
        print usage()
        sys.exit(1)
    print "running command"
    print newConfigParam_client(a, b , c, d, e, f, g, h, i)
