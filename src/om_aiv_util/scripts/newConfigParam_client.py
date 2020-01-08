#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def newConfigParam_client(array):
    rospy.wait_for_service('newConfigParam')
    try:
        service = rospy.ServiceProxy('newConfigParam', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s<section> <name> <description> <priority_level> <type> <default_value> <min> <max> <DisplayHint>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 10:
        section = str(sys.argv[1])
        name = str(sys.argv[2])
        description = str(sys.argv[3])
        priority_level = str(sys.argv[4])
        type = str(sys.argv[5])
        default_value = str(sys.argv[6])
        min = str(sys.argv[7])
        max = str(sys.argv[8])
        display_hint = str(sys.argv[9])
        array = [section, name, description, priority_level, type, default_value, min, max, display_hint]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print newConfigParam_client(array)
