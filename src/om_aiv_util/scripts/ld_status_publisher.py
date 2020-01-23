#!/usr/bin/env python
## publishes std_msgs messages to the 6 ld_status topics
import rospy
from om_aiv_util.srv import ArclApi, ArclApiRequest, ArclApiResponse
from om_aiv_util.srv import ArclListen, ArclListenRequest, ArclListenResponse
from om_aiv_util.msg import Status, Location

headers = ["Location", "Status", "StateOfCharge", "LocalizationScore", "Temperature", "ExtendedStatusForHumans"]
responses = {}

def req_status():
    responses.clear()

    # Request for the responses we are interested in, specified in the headers list.
    for i in range(0, len(headers)):
        resp_header = headers[i]
        
        rospy.wait_for_service("arcl_listen_service")
        get_status = rospy.ServiceProxy("arcl_listen_service", ArclListen)
        request = ArclListenRequest(resp_header)
        resp = get_status(request)
        
        if len(resp.resp_text) == 0:
            rospy.logdebug("No \"%s\" header from ARCL outgoing commands", resp_header)
            responses[resp_header] = ""
        else:
            responses[resp_header] = resp.resp_text

def pub_status():
    # TODO: Combine all status values as one Status msg type in ROS
    rospy.init_node("ld_status_publisher", anonymous=True)
    status_pub = rospy.Publisher("ldarcl_status", Status, queue_size=10)
    rate = rospy.Rate(10)

    status_msg = Status()
    loc_msg = Location()
    
    while not rospy.is_shutdown():
        try:
            req_status()
        except rospy.ServiceException, e:
            print "Service call failed: %s"%e
        else:
            # The order specified in the headers list must be followed here.
            values = responses[headers[0]].split()
            if len(values) is 3:
                try:
                    loc_msg.x = float(values[0])
                    loc_msg.y = float(values[1])
                    loc_msg.theta = float(values[2])
                except ValueError:
                    loc_msg.x = 0
                    loc_msg.y = 0
                    loc_msg.theta = 0
                    pass
                else:
                    status_msg.location = loc_msg 

            status_msg.status = responses[headers[1]]
            status_msg.extended_status = responses[headers[5]]

            try:
                status_msg.state_of_charge = float(responses[headers[2]])
            except ValueError:
                status_msg.state_of_charge = 0

            try:
                status_msg.localization_score = float(responses[headers[3]])
            except ValueError:
                status_msg.localization_score = 0

            try:
                status_msg.temperature = float(responses[headers[4]])
            except ValueError:
                status_msg.temperature = 0

            status_pub.publish(status_msg)
            
        finally:
            rate.sleep()



if __name__ == '__main__':
    try:
        pub_status()
            
    except rospy.ROSInterruptException:
        pass
