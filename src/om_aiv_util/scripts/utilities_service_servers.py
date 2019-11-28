#!/usr/bin/env python
from om_aiv_util.srv import OmAivService, OmAivServiceResponse
import rospy
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
ip_address = rospy.get_param("ip_address")
port = rospy.get_param("port")
# ip_address = "172.21.5.122"
# port = 7171
connecttcp.connect(str(ip_address), port)

def handle_analogInputList(req):
    rcv = analogInputList()
    return rcv
def handle_extIOOutputUpdateByte(req):
    name = req.a[0]
    byte_position = req.a[1]
    byte_value = req.a[2]
    rcv = extIOOutputUpdateByte(name, byte_position, byte_value)
    return rcv


def hardware_servers(op):
    if op == "List":
        rospy.loginfo("running List")
        s1 = rospy.Service('analogInputList', OmAivService, handle_analogInputList)
    # elif op == "QueryRaw":
    #     rospy.loginfo("running QueryRaw")
    #     s2 = rospy.Service('analogInputQueryRaw', OmAivService, handle_analogInputQueryRaw)




# def payloadSet(slot_num, slot_str):
#     command = "payloadSet {}".format(slot_num + " " + slot_str)
#     command = command.encode('ascii')
#     print "Running command: ", command
#     s.send(command+b"\r\n")
#     try:
#         data = s.recv(BUFFER_SIZE)
#         rcv = data.encode('ascii', 'ignore')
#         while not rospy.is_shutdown():
#             #check for required data
#             if "successfully set" in rcv:
#                 print rcv
#                 return rcv
#                 break
#             if "CommandErrorDescription" in rcv:
#                 print rcv
#                 return rcv
#                 break
#             else:
#                 data = s.recv(BUFFER_SIZE)
#                 rcv = rcv + data.encode('ascii', 'ignore')
#
#     except socket.error as errormsg:
#         print("Connection  failed")
#         return errormsg



if __name__ == "__main__":
    rospy.init_node('utilities_service_servers')
    hardware_servers("List")
    rospy.spin()
