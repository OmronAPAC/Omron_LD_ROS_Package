#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def waitTaskCancel_client():
    rospy.wait_for_service('waitTaskCancel')
    try:
        add_two_ints = rospy.ServiceProxy('waitTaskCancel', OmAivService)
        resp1 = add_two_ints()
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print waitTaskCancel_client()
