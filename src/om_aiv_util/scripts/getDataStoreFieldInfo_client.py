#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def getDataStoreFieldInfo_client(array):
    rospy.wait_for_service('getDataStoreFieldInfo')
    try:
        service = rospy.ServiceProxy('getDataStoreFieldInfo', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <field>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        field = str(sys.argv[1])
        array = [field]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print getDataStoreFieldInfo_client(array)
