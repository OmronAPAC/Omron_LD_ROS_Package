#!/usr/bin/env python
## listens to std_msgs/Strings published 
## to the 'ld_status' topics

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ' %s ', data.data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('ld_status_subscriber', anonymous=True)

    rospy.Subscriber('ldarcl_status_extended_status_for_humans', String, callback)
    rospy.Subscriber('ldarcl_status_status', String, callback)
    rospy.Subscriber('ldarcl_status_state_of_charge', String, callback)
    rospy.Subscriber('ldarcl_status_location', String, callback)
    rospy.Subscriber('ldarcl_status_localization_score', String, callback)
    rospy.Subscriber('ldarcl_status_temperature', String, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
