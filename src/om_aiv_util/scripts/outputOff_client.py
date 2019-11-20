#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def outputOff_client(a):
    rospy.wait_for_service('outputOff')
    try:
        service = rospy.ServiceProxy('outputOff', Service)
        resp1 = service(a)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> Give device to turn off"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        a = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print outputOff_client(a)
