#!/usr/bin/env python
import rospy
from om_aiv_util.srv import ArclApi, ArclApiRequest
def getMacros_client():
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
            ARCL server = "End of routes"
            line_identifier = "of routes" (unique substring is OK) OR "End of routes"
    
            Incorrect, will NOT return correct response:
            ARCL server = "End of routes"
            line_identifier = "End routes"
            OR
            "End" => does not uniquely identify, there are other commands that returns messages 
            with "End of something" similar syntax. 
    """
    req_msg = ArclApiRequest()
    req_msg.command = "getMacros"
    req_msg.line_identifier = "End of macros"
    
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
        getMacros_client()
    except rospy.ROSInterruptException:
        rospy.signal_shutdown("Shutting down getMacros client")
