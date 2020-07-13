#! /usr/bin/env python

from __future__ import print_function
import rospy
import actionlib
from om_aiv_navigation.msg import ActionAction, ActionGoal, ActionResult

def goto_client():
    # Creates the SimpleActionClient, passing the type of the action
    # (FibonacciAction) to the constructor.
    client = actionlib.SimpleActionClient('action_servers', ActionAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = ActionGoal("goto Goal3", ["Arrived at Goal3"])


    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  

if __name__ == '__main__':
    try:
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('goto_goal3_action_py')
        result = goto_client()
        # rospy.INFO("Result:")
        print("Result:", result)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)