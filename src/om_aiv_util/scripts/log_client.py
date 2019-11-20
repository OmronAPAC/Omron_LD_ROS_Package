#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def log_client(a, b):
    rospy.wait_for_service('log')
    try:
        service = rospy.ServiceProxy('log', Service2)
        resp1 = service(a, b)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <message> [level]"%sys.argv[0]

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
    print log_client(a, b)
