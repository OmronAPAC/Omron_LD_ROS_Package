#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def enableMotors_client(x):
    service_name = "/{}".format(x + "/enableMotors")
    print service_name
    # rospy.wait_for_service('enableMotors')
    rospy.wait_for_service(service_name, timeout=30)
    # rospy.wait_for_service('/robot1/enableMotors')
    try:
        # service = rospy.ServiceProxy('robot1/enableMotors', Service)
        service = rospy.ServiceProxy(service_name, Service)
        resp1 = service(x)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        x = str(sys.argv[1])

    else:
        print usage()
        sys.exit(1)
    print "running command"
    print enableMotors_client(x)
