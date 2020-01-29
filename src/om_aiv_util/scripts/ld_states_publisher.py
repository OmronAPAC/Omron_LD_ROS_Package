#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from om_aiv_util.socket_listener import *
from om_aiv_util.msg import Status, Location

"""

"""
def pub_status(status_pub, listener):
    status_msg = Status()
    loc_msg = Location()
    try:
        status_status = listener.get_response("Status")
        status_batt = listener.get_response("StateOfCharge")
        status_loc = listener.get_response("Location")
        status_loc_score = listener.get_response("LocalizationScore")
        status_temp = listener.get_response("Temperature")
        status_ext = listener.get_response("ExtendedStatusForHumans")
    except KeyError:
        pass
    else:
        status_msg.status = status_status[0]
        status_msg.extended_status = status_ext[0]
        status_msg.state_of_charge = float(status_batt[0])
        status_msg.localization_score = float(status_loc_score[0])
        status_msg.temperature = float(status_temp[0])
        # Parse location values
        values = status_loc[0].split()
        if len(values) is 3:
            try:
                loc_msg.x = float(values[0])
                loc_msg.y = float(values[1])
                loc_msg.theta = float(values[2])
            except ValueError:
                loc_msg.x = 0
                loc_msg.y = 0
                loc_msg.theta = 0
                rospy.logerr("Value error with location coordinates. Setting them to zeroes.")
                pass
            else:
                status_msg.location = loc_msg
    finally:
        status_pub.publish(status_msg)

"""

"""
def pub_laser(laser_pub, listener):
    try:
        scans = listener.get_response("RangeDeviceGetCurrent")
    except KeyError:
        pass
    else:
        laser_pub.publish(" ".join(scans))

"""

"""
def pub_goals(goals_pub, listener):
    try:
        goals = listener.get_response("Goal")
    except KeyError:
        pass
    else:
        goals_pub.publish(" ".join(goals))

def pub_odometer(odom_pub, listener):
    try:
        odom = listener.get_response("Odometer")
    except KeyError:
        pass
    else:
        odom_pub.publish(" ".join(odom))

def pub_app_fault_query(app_fault_query_pub, listener):
    try:
        query = listener.get_response("ApplicationFaultQuery")
    except KeyError:
        pass
    else:
        app_fault_query_pub.publish(" ".join(query))

def pub_faults_get(faults_get_pub, listener):
    try:
        faults = listener.get_response("FaultList")
    except KeyError:
        pass
    else:
        faults_get_pub.publish(" ".join(faults))

def pub_query_faults(query_faults_pub, listener):
    try:
        faults = listener.get_response("RobotFaultQuery")
    except KeyError:
        pass
    else:
        query_faults_pub.publish(" ".join(faults))

"""

"""
def pub_states(listener):
    rospy.init_node("ld_states_publisher", anonymous=True)
    status_pub = rospy.Publisher("ldarcl_status", Status, queue_size=10)
    laser_pub = rospy.Publisher("ldarcl_laser", String, queue_size=10)
    goals_pub = rospy.Publisher("ldarcl_all_goals", String, queue_size=10)
    odom_pub = rospy.Publisher("ldarcl_odom", String, queue_size=10)
    app_fault_query_pub = rospy.Publisher("ldarcl_application_fault_query", String, queue_size=10)
    faults_get_pub = rospy.Publisher("ldarcl_faults_get", String, queue_size=10)
    query_faults_pub = rospy.Publisher("ldarcl_query_faults", String, queue_size=10)
    rate = rospy.Rate(10)
    try:
        while not rospy.is_shutdown():
            events = listener.selector.select()
            for key, mask in events:
                listener.process_events(mask)

            pub_status(status_pub, listener)
            pub_laser(laser_pub, listener)
            pub_goals(goals_pub, listener)
            pub_odometer(odom_pub, listener)
            pub_app_fault_query(app_fault_query_pub, listener)
            pub_faults_get(faults_get_pub, listener)
            pub_query_faults(query_faults_pub, listener)

            rate.sleep()
    except (KeyboardInterrupt, rospy.ROSInterruptException):
        listener.close()
        rospy.signal_shutdown("Shutting down ARCL states publisher")
    
if __name__ == "__main__":

    listener = SocketListener("168.3.201.114", 7179)
    listener.begin()

    pub_states(listener)