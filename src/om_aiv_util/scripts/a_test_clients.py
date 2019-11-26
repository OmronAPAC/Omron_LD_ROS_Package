#!/usr/bin/env python

import sys
import rospy
from om_aiv_util.srv import *

def op_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    print "ok"
    rospy.wait_for_service('minus_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        minus_two_ints = rospy.ServiceProxy('minus_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y)
        print resp1
        # return resp1.sum
        resp2 = minus_two_ints(x, y)
        print "rep2", resp2
        # return resp1.sum
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    # print "Requesting %s+%s"%(x, y)
    # print "%s + %s = %s"%(x, y, add_two_ints_client(x, y))
    op_two_ints_client(x, y)
