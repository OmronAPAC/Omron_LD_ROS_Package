#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def mapObjectList_client(x):
    rospy.wait_for_service('mapObjectList')
    try:
        add_two_ints = rospy.ServiceProxy('mapObjectList', Service)
        resp1 = add_two_ints(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <type>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print mapObjectList_client(x)
