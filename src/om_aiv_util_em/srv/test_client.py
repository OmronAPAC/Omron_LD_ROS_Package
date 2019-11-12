#! /usr/bin/env python

import rospy
from std_srvs.srv import Trigger, TriggerRequest

# init a node as usual
rospy.init_node('service_client')

# wait for this sevice to be running
rospy.wait_for_service('/service')

# Create the connection to the service. Remember it's a Trigger service

analogInputList_service = rospy.ServiceProxy('/service', Trigger)


# Create an object of the type TriggerRequest. We nned a TriggerRequest for a Trigger service
sos = TriggerRequest()

# Now send the request through the connection
result = analogInputList_service(sos)

# Done
print result
