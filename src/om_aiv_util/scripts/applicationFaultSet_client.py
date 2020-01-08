#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def applicationFaultSet_client(array):
    rospy.wait_for_service('applicationFaultSet')
    try:
        service = rospy.ServiceProxy('applicationFaultSet', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> <short description> <long description> <bool:drivingFault> <bool:criticalFault>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 6:
        name = str(sys.argv[1])
        short_description = str(sys.argv[2])
        long_description = str(sys.argv[3])
        bool_driving = str(sys.argv[4])
        bool_critical = str(sys.argv[5])
        array = [name, short_description, long_description, bool_driving, bool_critical]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print applicationFaultSet_client(array)
