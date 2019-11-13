#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueModify_client(a, b , c):
    rospy.wait_for_service('queueModify')
    try:
        add_two_ints = rospy.ServiceProxy('queueModify', Service3)
        resp1 = add_two_ints(a, b, c)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <id> <type> <value>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print queueModify_client(a, b , c)