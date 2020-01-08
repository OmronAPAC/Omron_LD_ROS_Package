#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def analogInputQueryRaw_client(array):
    rospy.wait_for_service('connectOutgoing')
    try:
        service = rospy.ServiceProxy('connectOutgoing', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <hostname> <port> No hostname and/or port given"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        a = str(sys.argv[1])
        b = str(sys.argv[2])
        array = [ a, b ]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print analogInputQueryRaw_client(array)
