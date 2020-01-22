#!/usr/bin/env python
import rospy
from om_aiv_util.socket_listener import *
from om_aiv_util.srv import ArclListen, ArclListenResponse

listener = SocketListener("168.3.201.114", 7179)
listener.begin()

def custom_spin():
    """
    Customized version of rospy.spin()
    """
    rate = rospy.Rate(10)
    try:
        while not rospy.is_shutdown():
            events = listener.selector.select()
            for key, mask in events:
                listener.process_events(mask)
            rate.sleep()
    except KeyboardInterrupt:
        listener.close()
        rospy.signal_shutdown("Shutting down ARCL listening server")

def req_handler(req):
    global listener
    try:
      resp = listener.get_response(req.resp_header)
    except KeyError:
      return None
    else:
      return ArclListenResponse(" ".join(resp))
    
def arcl_listen():
  rospy.init_node("arcl_listen_server", anonymous=True)
  service = rospy.Service("arcl_listen_service", ArclListen, req_handler)
  custom_spin()

if __name__ == "__main__":
    arcl_listen()