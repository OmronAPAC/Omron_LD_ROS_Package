#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def configAdd_client(array):
    rospy.wait_for_service('configAdd')
    try:
        service = rospy.ServiceProxy('configAdd', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <configuration> <value>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        configuration = str(sys.argv[1])
        value = str(sys.argv[2])
        array = [configuration, value]
    elif len(sys.argv) == 2:
        section = str(sys.argv[1])
        # b = ""
        array = [section]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print configAdd_client(array)
