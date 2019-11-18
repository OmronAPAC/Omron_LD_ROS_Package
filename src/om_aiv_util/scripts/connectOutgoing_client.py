#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def analogInputQueryRaw_client(a, b):
    rospy.wait_for_service('connectOutgoing')
    try:
        add_two_ints = rospy.ServiceProxy('connectOutgoing', Service2)
        resp1 = add_two_ints(a, b)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <hostname> <port>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print analogInputQueryRaw_client(a, b)
