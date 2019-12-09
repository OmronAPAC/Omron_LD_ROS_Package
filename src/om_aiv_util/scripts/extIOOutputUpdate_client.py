#!/usr/bin/env python
import sys
import rospy
from om_aiv_util.srv import *
def extIOOutputUpdate_client(array):
    rospy.wait_for_service('extIOOutputUpdate')
    try:
        service = rospy.ServiceProxy('extIOOutputUpdate', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

def usage():
    return "%s <name> <value>"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        name = str(sys.argv[1])
        value = str(sys.argv[2])
        array = [name, value]
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print extIOOutputUpdate_client(array)
