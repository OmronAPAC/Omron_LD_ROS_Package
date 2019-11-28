#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def mapObjectTypeInfo_client(array):
    rospy.wait_for_service('mapObjectTypeInfo')
    try:
        service = rospy.ServiceProxy('mapObjectTypeInfo', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <type>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        type = str(sys.argv[1])
        array = [type]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print mapObjectTypeInfo_client(array)
