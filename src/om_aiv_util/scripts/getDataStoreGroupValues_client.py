#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def getDataStoreGroupValues_client(x):
    rospy.wait_for_service('getDataStoreGroupValues')
    try:
        service = rospy.ServiceProxy('getDataStoreGroupValues', Service)
        resp1 = service(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <group>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print getDataStoreGroupValues_client(x)
