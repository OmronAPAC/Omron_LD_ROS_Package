#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def log_client(array):
    rospy.wait_for_service('log')
    try:
        service = rospy.ServiceProxy('log', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <message> [level]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        message = str(sys.argv[1])
        level = str(sys.argv[2])
        array = [message, level]
    elif len(sys.argv) == 2:
        message = str(sys.argv[1])
        nil = ""
        array = [message, nil]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print log_client(array)
