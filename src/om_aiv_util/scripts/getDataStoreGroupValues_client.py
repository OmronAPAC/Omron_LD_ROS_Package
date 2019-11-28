#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def getDataStoreGroupValues_client(array):
    rospy.wait_for_service('getDataStoreGroupValues')
    try:
        service = rospy.ServiceProxy('getDataStoreGroupValues', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <group>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        group = str(sys.argv[1])
        array = [group]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print getDataStoreGroupValues_client(array)
