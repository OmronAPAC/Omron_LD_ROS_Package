#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def getDataStoreFieldInfo_client(x):
    rospy.wait_for_service('getDataStoreFieldInfo')
    try:
        service = rospy.ServiceProxy('getDataStoreFieldInfo', Service)
        resp1 = service(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <field>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print getDataStoreFieldInfo_client(x)
