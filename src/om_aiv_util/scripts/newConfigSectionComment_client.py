#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def newConfigSectionComment_client(array):
    rospy.wait_for_service('newConfigSectionComment')
    try:
        service = rospy.ServiceProxy('newConfigSectionComment', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <section> <comment>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        section = str(sys.argv[1])
        comment = str(sys.argv[2])
        array = [section, comment]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print newConfigSectionComment_client(array)
