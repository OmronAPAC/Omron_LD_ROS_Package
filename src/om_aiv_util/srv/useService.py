#!/usr/bin/env python

import rospy

from ld_services.srv import ServiceExample

import sys

rospy.init_node('use_service')

#wait the service to be advertised, otherwise the service use will fail
rospy.wait_for_service('service_example')

#setup a local proxy for the service
srv=rospy.ServiceProxy('service_example',ServiceExample)

#use the service and send it a value. In this case, I can send 1 or 0
service_example=srv(0)

#print the result from the service
print service_example
