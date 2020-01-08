#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def queueMulti_client(array):
    rospy.wait_for_service('queueMulti')
    try:
        service = rospy.ServiceProxy('queueMulti', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <number of goals> <number of fields per goal> <goal1> <goal1 args> <goal2> <goal2 args> ... <goalN> <goalN args> [jobid]"%sys.argv[0]

if __name__ == "__main__":
    arg = str(sys.argv[1:])
    print "running command"
    arg = arg.replace(',', '')
    arg = arg.replace('[', '')
    arg = arg.replace(']', '')
    arg = arg.replace("'", '')
    array = [arg]
    print queueMulti_client(array)
