#!/usr/bin/env python
import rospy
from om_aiv_util.srv import ArclApi, ArclApiRequest

def getInfo_client():
    rospy.wait_for_service('arcl_api_service')

    """
    First we create the request message.
    
    NOTE:   Unlike the command, the line_identifier IS case-sensitive.
            The line_identifier must have the correct letter case as the expected message received
            from ARCL server.
            However, the line_identifer does not have to match the complete line received from ARCL,
            it can be a substring of the ARCL line. As long as the given line_identifier will
            uniquely identify a line from ARCL. BUT IT IS STILL CASE-SENSITIVE.
    
            --- Example --- 
    
            Correct line_identifier choice, will return correct response:
            ARCL server = "Info: WirelessQuality 90%"
            line_identifier = "Info: WirelessQuality" (unique substring is OK)
    
            Incorrect, will NOT return correct response:
            ARCL server = "Info: WirelessQuality 90%"
            line_identifier = "Info: WirelessQuality 90%" => percentage can change, not reliable.
            OR
            "Info:" => does not uniquely identify, there are other commands that returns messages 
            with "Info: something" similar syntax. 
    """
    req_msg = ArclApiRequest()
    req_msg.command = "getInfo WirelessQuality"
    req_msg.line_identifier = "Info: WirelessQuality"
    
    try:
        # Request as ROS service client
        request = rospy.ServiceProxy('arcl_api_service', ArclApi)
        response = request(req_msg)
        
        # Do something awesome with the response message here.
        print response.response

    except rospy.ServiceException, error:
        print "Service call failed: %s"%error

if __name__ == "__main__":
    try:
        getInfo_client()
    except rospy.ROSInterruptException:
        rospy.signal_shutdown("Shutting down getInfo client")
    