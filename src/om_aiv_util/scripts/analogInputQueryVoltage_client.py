#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def analogInputQueryVoltage_client(array):
    rospy.wait_for_service('analogInputQueryVoltage')
    try:
        service = rospy.ServiceProxy('analogInputQueryVoltage', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s <name> Give device to query"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        name = str(sys.argv[1])
        array = [name]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print analogInputQueryVoltage_client(array)
