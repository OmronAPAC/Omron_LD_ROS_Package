#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def payloadQuery_client(array):
    rospy.wait_for_service('payloadQuery')
    try:
        service = rospy.ServiceProxy('payloadQuery', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s [robotName or \"default\"] [slotNumber or \"default\"]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        robot_name = str(sys.argv[1])
        slot_num = str(sys.argv[2])
        array = [robot_name, slot_num]
    elif len(sys.argv) == 2:
        robot_name = str(sys.argv[1])
        nil = ""
        array = [robot_name, nil]
    elif len(sys.argv) == 1:
        nil1 = ""
        nil2 = ""
        array = [nil1, nil2]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print payloadQuery_client(array)
