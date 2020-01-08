#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueQuery_client(array):
    rospy.wait_for_service('queueQuery')
    try:
        service = rospy.ServiceProxy('queueQuery', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <type> <value> [echoString]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        type = str(sys.argv[1])
        value = str(sys.argv[2])
        nil = ""
        array = [type, value, nil]
    elif len(sys.argv) == 4:
        type = str(sys.argv[1])
        value = str(sys.argv[2])
        echo_str = str(sys.argv[3])
        array = [type, value, echo_str]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueQuery_client(array)
