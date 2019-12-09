#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def doTaskInstant_client(array):
    rospy.wait_for_service('doTaskInstant')
    try:
        service = rospy.ServiceProxy('doTaskInstant', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <task> <argument> Must give task to do "%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        task = str(sys.argv[1])
        arg = str(sys.argv[2])
        array = [task, arg]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print doTaskInstant_client(array)
