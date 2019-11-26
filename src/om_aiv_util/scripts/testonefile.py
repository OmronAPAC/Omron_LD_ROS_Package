#!/usr/bin/env python
from socketconnection_class import ConnectSocket, connecttcp
s = connecttcp.sock
import socket
from threading import Thread
import time
import re
import sys
import rospy
from std_msgs.msg import String
import analogInputList_server
# import analogInputQueryRaw_server


if __name__ == "__main__":
    analogInputList_server()
    # analogInputQueryRaw_server()
