#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueDropoff_client(a, b , c):
    rospy.wait_for_service('queueDropoff')
    try:
        service = rospy.ServiceProxy('queueDropoff', Service3)
        resp1 = service(a, b, c)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <goalName> [priority] [jobId]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
    elif len(sys.argv) == 2:
        a = str(sys.argv[1])
        b = ""
        c = ""
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    print queueDropoff_client(a, b , c)
