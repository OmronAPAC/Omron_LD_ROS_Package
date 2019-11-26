#!/usr/bin/env python
import sys
import rospy
import numpy
from om_aiv_util.srv import *
def analogInputQueryRaw_client(array):
    rospy.wait_for_service('analogInputQueryRaw')
    try:
        service = rospy.ServiceProxy('analogInputQueryRaw', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <name> Give device to query"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
        array = [ x ]
        print array
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print analogInputQueryRaw_client(array)
