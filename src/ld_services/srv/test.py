
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
    analogInputList()
    '''
    Callback function used by the service server to process
    requests from clients. It returns a TriggerResponse
    '''
    return TriggerResponse(

        success=True,
        message="Hey, roger that; we'll be right there!"
    )


def analogInputList():
    global s
    global data
    pub = rospy.Publisher('arcl_analogInputList', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    global rcv
    global i
    i = 1
    flag = 0
    data = s.recv(BUFFER_SIZE)
    rcv = data.decode("utf-8")
    while (flag == 0):
        if "End of commands" in rcv:
            flag == 1
            while not rospy.is_shutdown():
                command = "analogInputList"
                command = command.encode('ascii')
                s.send(command+b"\r\n")
                print "Running Command: ",command
                time.sleep(1)
                data = s.recv(BUFFER_SIZE)
                rcv = data.decode("utf-8")

                pubout = str(data.splitlines())
                pub.publish(pubout)
                time.sleep(1)
                rospy.loginfo(rcv)
                time.sleep(2)
                exit(0)

        else:
            flag == 0
            data = s.recv(BUFFER_SIZE)
            rcv = data.decode("utf-8")






rospy.init_node('sos_service')                     # initialize a ROS node
my_service = rospy.Service(                        # create a service, specifying its name,
    '/service', Trigger, trigger_response         # type, and callback
)
rospy.spin()                                       # Keep the program from exiting, until Ctrl + C is pressed
