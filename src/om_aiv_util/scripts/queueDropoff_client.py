#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueDropoff_client(array):
    rospy.wait_for_service('queueDropoff')
    try:
        service = rospy.ServiceProxy('queueDropoff', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <goalName> [priority] [jobId]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        goal_name = str(sys.argv[1])
        priority = str(sys.argv[2])
        job_id = str(sys.argv[3])
        array = [goal_name, priority, job_id]
    elif len(sys.argv) == 2:
        goal_name = str(sys.argv[1])
        nil = ""
        nil2 = ""
        array = [goal_name, nil, nil2]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queueDropoff_client(array)
