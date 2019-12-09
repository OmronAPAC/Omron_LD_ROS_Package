#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def inputList_client(array):
    rospy.wait_for_service('inputList')
    try:
        service = rospy.ServiceProxy('inputList', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        nil = ""
        array = [nil]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print inputList_client(array)
