#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def extIOOutputUpdateByte_client(array):
    rospy.wait_for_service('extIOOutputUpdateByte')
    try:
        service = rospy.ServiceProxy('extIOOutputUpdateByte', OmAivService)
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
        print array
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print extIOOutputUpdateByte_client(array)
