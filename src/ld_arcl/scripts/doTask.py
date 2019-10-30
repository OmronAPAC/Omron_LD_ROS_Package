#!/usr/bin/env python
from connectwifi import connecttowifi

# from socketconnection import socketconnect
# from socketconnection import data, s

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

# connecttcp.connect("172.21.5.33", 7171)
# connecttcp.sendpassword("omron1")

class DoTask(object):
    def sendcommand(self, commandarg):
        global s
        global data
        global pub
        pub = rospy.Publisher('arcl_doTask', String, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(10) # 10hz
        self.commandarg = commandarg
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
                    cmd = "dotask {}".format(commandarg)
                    cmd = cmd.encode('ascii')
                    s.send(cmd+b"\r\n")
                    print "running command:" ,cmd 
                    time.sleep(1)
                    data = s.recv(BUFFER_SIZE)
                    rcv = data.decode("utf-8")
                
                    pubout = str(data.splitlines())
                    pub.publish(pubout)
                    time.sleep(1)
                    rospy.loginfo(rcv)
                    time.sleep(2)
                    return 
            
            else:
                flag == 0
                data = s.recv(BUFFER_SIZE)
                rcv = data.decode("utf-8")
dt = DoTask()

# dt.sendcommand("move 1000")

# if __name__ == '__main__':
#     try:
#         dotask.sendcommand("move 1000")
#     except rospy.ROSInterruptException:
#         pass             


# #!/usr/bin/env python
# from connectwifi import connecttowifi

# # from socketconnection import socketconnect
# # from socketconnection import data, s

# from socketconnection_class import ConnectSocket, connecttcp

# s = connecttcp.sock
# import socket
# import threading
# import time
# import re
# import sys
# import rospy
# from std_msgs.msg import String
# BUFFER_SIZE = 1024

# # connecttcp.connect("172.21.5.33", 7171)
# # connecttcp.sendpassword("omron1")

# def dotask():
#     global s
#     global data
#     pub = rospy.Publisher('arcl_doTask', String, queue_size=10)
#     rospy.init_node('talker', anonymous=True)
#     rate = rospy.Rate(10) # 10hz
#     command = raw_input("Enter task and argement in this format: doTask <task> <argument>\r\ndoTask ")
    
#     global rcv
#     global i
#     i = 1
#     flag = 0
#     data = s.recv(BUFFER_SIZE)
#     rcv = data.decode("utf-8")
#     while (flag == 0):
#         if "End of commands" in rcv:
#             flag == 1
#             while not rospy.is_shutdown():
#                 cmd = "dotask {}".format(command)
#                 cmd = cmd.encode('ascii')
#                 s.send(cmd+b"\r\n")
#                 print "running command:" ,cmd 
#                 time.sleep(1)
#                 data = s.recv(BUFFER_SIZE)
#                 rcv = data.decode("utf-8")
            
#                 pubout = str(data.splitlines())
#                 pub.publish(pubout)
#                 time.sleep(1)
#                 rospy.loginfo(rcv)
#                 time.sleep(2)
#                 return(0)
            

#         else:
#             flag == 0
#             data = s.recv(BUFFER_SIZE)
#             rcv = data.decode("utf-8")

                
# if __name__ == '__main__':
#     try:
#         dotask()
#     except rospy.ROSInterruptException:
#         pass









