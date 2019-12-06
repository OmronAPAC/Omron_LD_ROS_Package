#!/usr/bin/env python
import sys
import rospy
import actionlib
from om_aiv_navigation.msg import ActionAction, ActionGoal
from om_aiv_util.srv import *
def say_client(array):
    rospy.wait_for_service('say')
    try:
        service = rospy.ServiceProxy('say', OmAivService)
        resp1 = service(array)
        return resp1.device
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def feedback_cb(msg):
 print 'Feedback received:', msg

def call_server(goal_name,command):

    client = actionlib.SimpleActionClient(command, ActionAction)

    client.wait_for_server()

    goal = ActionGoal()
    # goal.goal_goal = "Goal1"
    goal.goal_goal = goal_name


    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result



if __name__ == '__main__':
    text_str = "going to first goal"
    array = [text_str]
    print "running command"
    print say_client(array)
    try:
        rospy.init_node('goTo_action_client')
        result = call_server("goal5", "goTo")
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
    text_str = "going to second goal"
    array = [text_str]
    print "running command"
    print say_client(array)
    try:
        rospy.init_node('goTo_action_client')
        result = call_server("goal6", "goTo")
        print 'The result is:', result
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
