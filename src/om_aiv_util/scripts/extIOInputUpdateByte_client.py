#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def extIOInputUpdateByte_client(array):
    rospy.wait_for_service('extIOInputUpdateByte')
    try:
        service = rospy.ServiceProxy('extIOInputUpdateByte', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> <byte position> <value>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        name = str(sys.argv[1])
        byte_position = str(sys.argv[2])
        byte_value = str(sys.argv[3])
        array = [name, byte_position, byte_value]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print extIOInputUpdateByte_client(array)
