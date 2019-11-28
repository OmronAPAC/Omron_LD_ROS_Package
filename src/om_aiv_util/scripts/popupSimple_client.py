#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def popupSimple_client(array):
    rospy.wait_for_service('popupSimple')
    try:
        service = rospy.ServiceProxy('popupSimple', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <\"title\"> <\"message\"> <\"buttonLabel\"> <timeout>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        title = str(sys.argv[1])
        message = str(sys.argv[2])
        button_label = str(sys.argv[3])
        timeout = str(sys.argv[4])
        array = [title, message, button_label, timeout]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print popupSimple_client(array)
