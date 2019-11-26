#!/usr/bin/env python
import sys
import rospy
import numpy
from om_aiv_util.srv import *
def echo_client(array):
    rospy.wait_for_service('echo')
    try:
        # a = b = c = d = e = f = g = h = None
        service = rospy.ServiceProxy('echo', Service9)
        # resp1 = service(x, a, b, c, d, e, f, g, h)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <on/off>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
        array = [ x ]
        # x = array[0]
        # a = "test"
        # x = str(numpy.array([a], dtype=numpy.str))
        print array
    elif len(sys.argv) == 1:
        array = None
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print echo_client(array)
