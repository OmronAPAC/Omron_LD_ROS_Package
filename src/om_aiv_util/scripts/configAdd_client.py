#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def configAdd_client(a, b):
    rospy.wait_for_service('configAdd')
    try:
        service = rospy.ServiceProxy('configAdd', Service2)
        resp1 = service(a, b)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <configuration> <value>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
    elif len(sys.argv) == 2:
        a = str(sys.argv[1])
        b = ""
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print configAdd_client(a, b)
