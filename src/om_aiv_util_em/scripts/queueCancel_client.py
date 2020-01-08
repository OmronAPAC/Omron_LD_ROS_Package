#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueCancel_client(array):
    rospy.wait_for_service('queueCancel')
    try:
        service = rospy.ServiceProxy('queueCancel', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <type> <value> [echoString or \"default\"] [reason]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        type = str(sys.argv[1])
        value = str(sys.argv[2])
        echo_str = str(sys.argv[3])
        reason = str(sys.argv[4])
        array = [type, value, echo_str, reason]
    elif len(sys.argv) == 3:
        type = str(sys.argv[1])
        value = str(sys.argv[2])
        nil1 = ""
        nil2 = ""
        array = [type, value, nil1, nil2]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueCancel_client(array)
