#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def extIOOutputUpdateBit_client(array):
    rospy.wait_for_service('extIOOutputUpdateBit')
    try:
        service = rospy.ServiceProxy('extIOOutputUpdateBit', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> <bit position> <0 or 1(bit value)>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        name = str(sys.argv[1])
        bit_position = str(sys.argv[2])
        bit_value = str(sys.argv[3])
        array = [name, bit_position, bit_value]
        print array
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print extIOOutputUpdateBit_client(array)
