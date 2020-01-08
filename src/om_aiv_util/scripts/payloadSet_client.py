#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def payloadSet_client(array):
    rospy.wait_for_service('payloadSet')
    try:
        service = rospy.ServiceProxy('payloadSet', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <slot_number> <slot_string>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        slot_num = str(sys.argv[1])
        slot_str = str(sys.argv[2])
        array = [slot_num, slot_str]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print payloadSet_client(array)
