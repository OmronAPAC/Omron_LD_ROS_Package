#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queuePickupDropoff_client(array):
    rospy.wait_for_service('queuePickupDropoff')
    try:
        service = rospy.ServiceProxy('queuePickupDropoff', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <goal1Name> <goal2Name> [priority1 or \"default\"] [priority2 or \"default\"] [jobId]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 6:
        goal1_name = str(sys.argv[1])
        goal2_name = str(sys.argv[2])
        priority1 = str(sys.argv[3])
        priority2 = str(sys.argv[4])
        job_id = str(sys.argv[5])
        array = [goal1_name, goal2_name, priority1, priority2, job_id]
    elif len(sys.argv) == 5:
        goal1_name = str(sys.argv[1])
        goal2_name = str(sys.argv[2])
        priority1 = str(sys.argv[3])
        priority2 = str(sys.argv[4])
        nil = ""
        array = [goal1_name, goal2_name, priority1, priority2, nil]
    elif len(sys.argv) == 3:
        goal1_name = str(sys.argv[1])
        goal2_name = str(sys.argv[2])
        nil1 = ""
        nil2 = ""
        nil3 = ""
        array = [goal1_name, goal2_name, nil1, nil2, nil3]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print queuePickupDropoff_client(array)
