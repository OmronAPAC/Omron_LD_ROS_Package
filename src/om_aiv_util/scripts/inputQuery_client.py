#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def inputQuery_client(array):
    rospy.wait_for_service('inputQuery')
    try:
        service = rospy.ServiceProxy('inputQuery', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <name> Give device to query"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        name = str(sys.argv[1])
        array = [name]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print inputQuery_client(array)
