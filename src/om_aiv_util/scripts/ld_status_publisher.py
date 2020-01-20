#!/usr/bin/env python
## publishes std_msgs messages to the 6 ld_status topics
from colorama import init
init()
from colorama import Fore, Back, Style
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from geometry_msgs.msg import Point
from om_aiv_util.msg import Location
import socket
import threading
import time
import re
import sys
from om_aiv_util.srv import ArclApi, ArclApiRequest, ArclApiResponse

# TODO: Do better than this!!
def split_args(input):
    out = input.splitlines()
    f_out = []

    for idx, elem in enumerate(out):
        if "Location:" in elem or "Status:" in elem or "StateOfCharge:" in elem or "LocalizationScore:" in elem or "Temperature:" in elem or "ExtendedStatusForHumans:":
            f_out.append(elem[(elem.find(":")+2):])
    
    return (f_out[0], f_out[1], f_out[2], f_out[3], f_out[4], f_out[5])

def req_status():
    rospy.wait_for_service("arcl_api_service")
    get_status = rospy.ServiceProxy("arcl_api_service", ArclApi)
    request = ArclApiRequest("Status", "Temperature:")
    # TODO: Do a try except here.
    resp = get_status(request)
    return resp.response

def pub_status():
    # TODO: Combine all status values as one Status msg type in ROS
    ext_status_pub = rospy.Publisher("ldarcl_extended_human_status", String, queue_size=10)
    status_pub = rospy.Publisher("ldarcl_status", String, queue_size=10)
    battery_pub = rospy.Publisher("ldarcl_batteryvoltage", String, queue_size=10)
    loc_pub = rospy.Publisher("ldarcl_location", Location, queue_size=10)
    locscore_pub = rospy.Publisher("ldarcl_localizationscore", String, queue_size=10)
    temp_pub = rospy.Publisher("ldarcl_temperature", String, queue_size=10)
    rospy.init_node("ld_status_publisher", anonymous=True)
    rate = rospy.Rate(1)
    loc_msg = Location()
    while not rospy.is_shutdown():
        try:
            resp = req_status()
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
        else:
            (ext_status, status, batt, loc, locscore, temp) = split_args(resp)
            ext_status_pub.publish(ext_status)
            status_pub.publish(status)
            battery_pub.publish(batt)
            loc_msg.x = float(loc.split()[0])
            loc_msg.y = float(loc.split()[1])
            loc_msg.theta = float(loc.split()[2])
            loc_pub.publish(loc_msg)
            locscore_pub.publish(locscore)
            temp_pub.publish(temp)
        finally:
            rate.sleep()



if __name__ == '__main__':
    try:
        pub_status()
            
    except rospy.ROSInterruptException:
        pass
