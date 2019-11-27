#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def payloadSlotCountLocal_client(array):
    rospy.wait_for_service('payloadSlotCountLocal')
    try:
        service = rospy.ServiceProxy('payloadSlotCountLocal', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = ""
        array = [x]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print payloadSlotCountLocal_client(array)
