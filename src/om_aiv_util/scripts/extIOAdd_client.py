#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def extIOAdd_client(array):
    rospy.wait_for_service('extIOAdd')
    try:
        service = rospy.ServiceProxy('extIOAdd', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> <numInputs> <numOutputs>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
        array = [a, b, c]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print extIOAdd_client(array)
