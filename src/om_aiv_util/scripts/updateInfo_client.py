#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def updateInfo_client(array):
    rospy.wait_for_service('updateInfo')
    try:
        service = rospy.ServiceProxy('updateInfo', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <infoName> <infoValue>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        info_name = str(sys.argv[1])
        info_value = str(sys.argv[2])
        array = [info_name, info_value]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print updateInfo_client(array)
