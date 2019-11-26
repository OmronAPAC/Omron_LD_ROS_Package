#!/usr/bin/env python

from om_aiv_util.srv import AddTwoInts,AddTwoIntsResponse
import rospy

def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)
def handle_minus_two_ints(req):
    print "Returning [%s - %s = %s]"%(req.a, req.b, (req.a - req.b))
    return AddTwoIntsResponse(req.a - req.b)

def operation_two_ints_server(op):
    # rospy.init_node('add_two_ints_server')
    print op
    if op == "plus":
        s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
        print "Ready to add two ints."
    elif op == "minus":
        s2 = rospy.Service('minus_two_ints', AddTwoInts, handle_minus_two_ints)
        print "Ready to subtract two ints."


if __name__ == "__main__":
    rospy.init_node('operations_server')
    operation_two_ints_server("plus")
    operation_two_ints_server("minus")
    rospy.spin()
