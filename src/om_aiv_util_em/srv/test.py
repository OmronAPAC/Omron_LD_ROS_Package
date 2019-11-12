#!/usr/bin/env python
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
import threading
import time
import re
import sys
import rospy
from std_msgs.msg import String
BUFFER_SIZE = 1024
# ip_address = rospy.get_param("ip_address")
# port = rospy.get_param("port")
ip_address = "172.21.5.125"
port = 7171
connecttcp.connect(str(ip_address), port)

from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    device()
    print device
    analogInputList()
    '''
    Callback function used by the service server to process
    requests from clients. It returns a TriggerResponse
    '''
    return TriggerResponse(

        success=True,
        message= rcv
    )

def analogInputList():
    global rcv
    pub = rospy.Publisher('arcl_analogInputList', String, queue_size=10)
    # rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    command = "analogInputList {}".format("device")
    print command
    command = command.encode('ascii')
    s.send(command+b"\r\n")
    try:
        data = s.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #check for required data
            if "End of AnalogInputList" in rcv:

                print rcv
                rcv = str(rcv.splitlines())
                break

            else:
                data = s.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')

    except socket.error as e:
        print("Connection  failed")
        return e



rospy.init_node('test_service')                     # initialize a ROS node
my_service = rospy.Service(                        # create a service, specifying its name,
    '/service', Trigger, trigger_response         # type, and callback
)
rospy.spin()                                       # Keep the program from exiting, until Ctrl + C is pressed
