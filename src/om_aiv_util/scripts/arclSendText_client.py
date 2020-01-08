#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def arclSendText_client(array):
    rospy.wait_for_service('arclSendText')
    try:
        service = rospy.ServiceProxy('arclSendText', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s Give text to send"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        string = str(sys.argv[1])
        array = [string]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print arclSendText_client(array)
