#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueQueryLocal_client(array):
    rospy.wait_for_service('queueQueryLocal')
    try:
        service = rospy.ServiceProxy('queueQueryLocal', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <type> <value> [echo_string]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        type = str(sys.argv[1])
        value = str(sys.argv[2])
        echo_str  = str(sys.argv[3])
        array = [type, value, echo_str]
    elif len(sys.argv) == 3:
        type = str(sys.argv[1])
        value = str(sys.argv[2])
        nil = ""
        array = [type, value, nil]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueQueryLocal_client(array)
