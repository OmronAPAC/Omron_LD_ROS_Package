#!/usr/bin/env python

import sys
import rospy
from om_aiv_util.srv import *

def analogInputList_client(x):
    rospy.wait_for_service('analogInputList')
    try:
        add_two_ints = rospy.ServiceProxy('analogInputList', Service)
        resp1 = add_two_ints(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [device]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = str(sys.argv[0])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    # analogInputList_client(x)
    print analogInputList_client(x)
