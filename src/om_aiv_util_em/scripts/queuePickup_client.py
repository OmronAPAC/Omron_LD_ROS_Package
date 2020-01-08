#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queuePickup_client(array):
    rospy.wait_for_service('queuePickup')
    try:
        service = rospy.ServiceProxy('queuePickup', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <goalName> [priority or \"default\"] [jobId]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        goal_name = str(sys.argv[1])
        priority = str(sys.argv[2])
        job_id = str(sys.argv[3])
        array = [goal_name, priority, job_id]
    elif len(sys.argv) == 3:
        goal_name = str(sys.argv[1])
        priority = str(sys.argv[2])
        nil = ""
        array = [goal_name, priority, nil]
    elif len(sys.argv) == 2:
        goal_name = str(sys.argv[1])
        nil1 = ""
        nil2 = ""
        array = [goal_name, nil1, nil2]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queuePickup_client(array)
