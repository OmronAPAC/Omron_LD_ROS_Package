#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def createInfo_client(array):
    rospy.wait_for_service('createInfo')
    try:
        service = rospy.ServiceProxy('createInfo', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <infoName> <maxLen> <infoValue>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        info_name = str(sys.argv[1])
        max_len = str(sys.argv[2])
        info_value = str(sys.argv[3])
        array = [info_name, max_len, info_value]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print createInfo_client(array)
