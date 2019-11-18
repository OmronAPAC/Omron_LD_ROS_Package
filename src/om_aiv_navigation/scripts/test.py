#!/usr/bin/env python
import sys
import rospy
import actionlib
from om_aiv_navigation.msg import QueueDropoffAction, QueueDropoffGoal
from std_msgs.msg import Float32
from std_msgs.msg import String

# rospy.init_node('queueDropoff_action_client')
# battery_level = rospy.wait_for_message('/ldarcl_status_state_of_charge', Float32)
# print battery_level
# battery_level = str(battery_level)
# battery_level = battery_level.strip("data:")
# battery_level = float(battery_level)
# if battery_level <= 50:
#         print "battery less than 50%"
#         exit(0)

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

def call_server2():

    client = actionlib.SimpleActionClient('queueDropoff', QueueDropoffAction)

    client.wait_for_server()

    goal = QueueDropoffGoal()
    goal.goal_queueDropoff = "goal4"

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':

    try:
        rospy.init_node('queueDropoff_action_client')
        result = call_server()
        print 'The result is:', result
        result2 = call_server2()
        print 'The result is:', result2
    except rospy.ROSInterruptException as e:
        print 'Something went wrong:', e
