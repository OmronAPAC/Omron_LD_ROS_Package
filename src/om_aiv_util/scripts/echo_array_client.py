#!/usr/bin/env python
import sys
import rospy
import numpy
from om_aiv_util.srv import *
def echo_client(x):
    rospy.wait_for_service('echo')
    try:
        a = b = c = d = e = f = g = h = None
        service = rospy.ServiceProxy('echo', Service9)
        resp1 = service(x, a, b, c, d, e, f, g, h)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <on/off>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
        x = str(numpy.array(["test", "test"], dtype=numpy.str))
    elif len(sys.argv) == 1:
        x = ""
        x = str(numpy.array(["test test"], dtype=numpy.str))
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print echo_client(x)
