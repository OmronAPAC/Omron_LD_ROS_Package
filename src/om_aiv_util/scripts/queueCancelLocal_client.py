#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueCancelLocal_client(array):
    rospy.wait_for_service('queueCancelLocal')
    try:
        service = rospy.ServiceProxy('queueCancelLocal', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <cancelType> <cancalValue> [echoString] [reason]"%sys.argv[0]

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
        nil = ""
        nil2 = ""
        array = [type, value, nil, nil2]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueCancelLocal_client(array)
