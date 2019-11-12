#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queuePickupDropoff_client(a, b , c, d, e):
    rospy.wait_for_service('queuePickupDropoff')
    try:
        add_two_ints = rospy.ServiceProxy('queuePickupDropoff', Service5)
        resp1 = add_two_ints(a, b, c, d, e)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <goal1Name> <goal2Name> [priority1 or \"default\"] [priority2 or \"default\"] [jobId]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 6:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
        d = str(sys.argv[4])
        e = str(sys.argv[5])
    elif len(sys.argv) == 5:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = str(sys.argv[3])
        d = str(sys.argv[4])
        e = ""
    elif len(sys.argv) == 3:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        c = ""
        d = ""
        e = ""
    else:
        print usage()
        sys.exit(1)
    print "running command"
    # print "Requesting", x
    # analogInputQueryRaw_client(a, b, c, d, e)
    print queuePickupDropoff_client(a, b , c, d, e)
