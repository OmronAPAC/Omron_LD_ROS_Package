#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def enableMotors_client(robot_name):
    service_name = "/{}".format(robot_name + "/enableMotors")
    print service_name
    rospy.wait_for_service(service_name, timeout=30)
    try:
        service = rospy.ServiceProxy(service_name, Service)
        resp1 = service(robot_name)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        robot_name = str(sys.argv[1])

    else:
        print usage()
        sys.exit(1)
    print "running command"
    print enableMotors_client(robot_name)
