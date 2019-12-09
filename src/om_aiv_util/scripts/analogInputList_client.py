#!/usr/bin/env python

import sys
import rospy
from om_aiv_util.srv import *

def analogInputList_client(array):
    #service name have to be defined correctly if using multiple robots
    rospy.wait_for_service('analogInputList')
    try:
        service = rospy.ServiceProxy('analogInputList', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [device]"%sys.argv[0]

if __name__ == "__main__":
    #take in command line arguents if required
    if len(sys.argv) == 1:
        nil = ""
        array = [nil]
    #check if correct number of command line arguments is entered
    else:
        print usage()
        sys.exit(1)
    print "running command"
    print analogInputList_client(array)
