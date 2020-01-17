#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import socket
from om_aiv_util.socketconnection_class import ConnectSocket

socket_conn = None
# Topics are not published in order.
topics_to_pub = {
    "ApplicationFaultQuery": ("End of ApplicationFaultQuery", "ApplicationFaultQuery:"),    
    "GetDateTime": ("DateTime:", "DateTime:"),
    "OneLineStatus": ("Status:", "Status:"),
    "QueryMotors": ("Motors", "Motors"),
    "Odometer": ("Odometer:", "Odometer:")

} # TODO: Put all commands to request in separate file.
publishers = {}

PUB_RATE = 10
BUFFER_SIZE = 2048
NODE_NAME_STRING = "ld_topic_publisher"
FAIL_CONN_STRING = "Connection failed"
ESTOP_PRESS_STRING = "EStop pressed"
ESTOP_RELIEVE_STRING = "EStop relieved but motors still disabled"
UNKNOWN_CMD_STRING = "Unknown command {}"

# TODO: Instead of continuously sending requests to the ARCL server, configure the ARCL server to output
# commands and then in here, we look for those output strings in that output socket. Then we parse those
# output and publishes to respective topics accordingly.

#Sends the given ARCL command to socket and retrieve response from ARCL server.
#arcl_command = actual command to be sent
#end_string = end of required data that is sent back from arcl. Example: "End of End of ApplicationFaultQuery"
#reply_header = required data to be printed out. Example: "ApplicationFaultQuery:..............."
def run_command(arcl_command, end_string, reply_header, pub):
    #send command to arcl
    arcl_command = arcl_command.encode('ascii')
    socket_conn.sock.send(arcl_command+b"\r\n")
    try:
        data = socket_conn.sock.recv(BUFFER_SIZE)
        rcv = data.encode('ascii', 'ignore')
        while not rospy.is_shutdown():
            #keep receiving data until require data is received
            if end_string in rcv:
                break
            if ESTOP_PRESS_STRING in rcv:
                rospy.logerr(ESTOP_PRESS_STRING)
                pub.publish(ESTOP_PRESS_STRING)
                return rcv
            if ESTOP_RELIEVE_STRING in rcv:
                rospy.logerr(ESTOP_RELIEVE_STRING)
                pub.publish(ESTOP_RELIEVE_STRING)
                return rcv
            if UNKNOWN_CMD_STRING.format(arcl_command) in rcv:
                rospy.logerr(rcv)
                return rcv
            else:
                data = socket_conn.sock.recv(BUFFER_SIZE)
                rcv = rcv + data.encode('ascii', 'ignore')
    except socket.error as e:
        print(FAIL_CONN_STRING)
        return e
    #check for required data
    for line in rcv.splitlines():
        if reply_header in line:
            rospy.loginfo(line)
            pub.publish(line)
            break

# Initialises this node along with all the topics required for the commands to be sent (specified in topics_to_pub).
# This continuously send requests for all the specified ARCL commands.
def pub_topics():
    for topic in topics_to_pub.keys():
        pub = rospy.Publisher(topic, String, queue_size=10)
        publishers[topic] = pub
    rospy.init_node(NODE_NAME_STRING, log_level=rospy.DEBUG)
    rate = rospy.Rate(PUB_RATE)

    # Create a socket connection to ARCL
    # TODO: somehow share the same connection with other nodes.
    global socket_conn
    try:
        socket_conn = ConnectSocket()
    except Exception as err:
        rospy.logerr(err.message)
        raise rospy.ROSInterruptException()
    
    while not rospy.is_shutdown():
        for topic, pub in publishers.items():
            # Request and publish the ARCL commands return values.
            run_command(topic, topics_to_pub[topic][0], topics_to_pub[topic][1], pub)
            pass

        rate.sleep()


if __name__ == '__main__':
    try:
        pub_topics()
    except rospy.ROSInterruptException:
        pass
