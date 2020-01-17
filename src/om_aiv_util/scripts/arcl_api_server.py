#!/usr/bin/env python
import rospy
from om_aiv_util.socket_driver import *
from om_aiv_util.srv import ArclApi

# Connect and log in.
socket_driver = SocketDriver()
# TODO: Add retrying of connection
socket_driver.connect("168.3.201.123", 7171)
req_id = socket_driver.login("adept\r\n")

def custom_spin():
    """
    Customized version of rospy.spin()
    """
    rate = rospy.Rate(50)
    try:
        while not rospy.is_shutdown():
            events = socket_driver.selector.select()
            for key, mask in events:
                socket_driver.process_events(mask)
            rate.sleep()
    except KeyboardInterrupt:
        rospy.signal_shutdown('keyboard interrupt')

def req_handler(req):
    global socket_driver
    req_id = socket_driver.queue_command(req.command, True, req.line_identifier)
    while True:
        try:
            resp = socket_driver.get_response(req_id)
        except KeyError:
            pass
        else:
            return resp

def arcl_api_server():
    rospy.init_node("arcl_api_server", anonymous=True)
    service = rospy.Service("arcl_api_service", ArclApi, req_handler)
    custom_spin()

if __name__ == "__main__":
    arcl_api_server()