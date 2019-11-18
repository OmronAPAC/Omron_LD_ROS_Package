#! /usr/bin/env python

import rospy
import actionlib
from om_aiv_navigation.msg import QueueDropoffAction, QueueDropoffGoal

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server():

    client = actionlib.SimpleActionClient('queueDropoff', QueueDropoffAction)

    client.wait_for_server()

    goal = QueueDropoffGoal()
    goal.goal_queueDropoff = "goal1"

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':

    try:
        rospy.init_node('queueDropoff_action_client')
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
