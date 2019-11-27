#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def analogInputQueryRaw_client(array):
    rospy.wait_for_service('getConfigSectionList')
    try:
        service = rospy.ServiceProxy('getConfigSectionList', OmAivService)
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
    print analogInputQueryRaw_client(array)
