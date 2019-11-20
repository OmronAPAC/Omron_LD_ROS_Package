#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def payloadRemove_client(x):
    rospy.wait_for_service('payloadRemove')
    try:
        service = rospy.ServiceProxy('payloadRemove', Service)
        resp1 = service(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <slot_number>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print payloadRemove_client(x)
