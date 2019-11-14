#! /usr/bin/env python

import rospy
import actionlib
from ld_actions.msg import GoToAction, GoToGoal

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server():

    client = actionlib.SimpleActionClient('goTo', GoToAction)

    client.wait_for_server()

    goal = GoToGoal()
    goal.goal_goto = "Goal3"
    # goalname = rospy.get_param("goal")
    # goal.goal_goto = goalname

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':

    try:
        rospy.init_node('goTo_action_client')
        result = call_server()
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
