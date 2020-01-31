#! /usr/bin/env python

import rospy
import actionlib
from om_aiv_navigation.msg import ActionAction, ActionFeedback, ActionResult
from om_aiv_util.socket_taskmaster import *

class ActionServer(object):
    _feedback = ActionFeedback()
    _result = ActionResult()

    def __init__(self, name, socket_taskmaster):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, ActionAction, self.exec_cb, auto_start=False)
        self._as.start()
        self.socket_taskmaster = socket_taskmaster

    def exec_cb(self, goal):
        r = rospy.Rate(10)

        self.socket_taskmaster.push_command(goal.command, True, goal.identifier)

        while True:
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                break

            (is_done, result, feedback) = self.socket_taskmaster.wait_command()
            if is_done:
                self._feedback.feed_msg = feedback
                self._as.publish_feedback(self._feedback)
                self._result.res_msg = result
                self._as.set_succeeded(self._result)
                break
            else:
                self._feedback.feed_msg = feedback
                self._as.publish_feedback(self._feedback)

            r.sleep()
        
if __name__ == "__main__":
    ip_address = rospy.get_param("ip_address")
    port = rospy.get_param("port")
    passwd = rospy.get_param("def_arcl_passwd")
    
    socket_taskmaster = SocketTaskmaster()
    # TODO: Add retrying of connection
    socket_taskmaster.connect(str(ip_address), int(port))
    req_id = socket_taskmaster.login(passwd)

    rospy.init_node("action_server")
    server = ActionServer(rospy.get_name(), socket_taskmaster)
    rospy.spin()
