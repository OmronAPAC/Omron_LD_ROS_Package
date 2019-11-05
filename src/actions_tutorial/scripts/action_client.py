#! /usr/bin/env python

import rospy
import actionlib
from actions_tutorial.msg import WashTheDishesAction, WashTheDishesGoal

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server():

    client = actionlib.SimpleActionClient('wash_dishes_as', WashTheDishesAction)

    client.wait_for_server()

    goal = WashTheDishesGoal()
    goal.number_of_minutes = 7

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':

    try:
        rospy.init_node('action_client')
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
