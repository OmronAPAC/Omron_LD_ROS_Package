#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def getConfigSectionInfo_client(array):
    rospy.wait_for_service('getConfigSectionInfo')
    try:
        service = rospy.ServiceProxy('getConfigSectionInfo', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <section>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
        array = [x]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print getConfigSectionInfo_client(array)
