#!/usr/bin/env python

from quadr_roots.srv import GetRoots, GetRootsResponse
import rospy

def handle_quadr_roots(req):
    rospy.loginfo('Input coefficients: a = %0.2f b = %0.2f c = %0.2f',
                  req.a, req.b, req.c)
    if req.a == 0 and req.b == 0:
        rospy.logerr('Wrong coefficients')
        message = 'Please enter not null values'
    elif req.a == 0:
        rospy.logwarn('You get a linear equation')
        x = -req.c/req.b
        message = 'x = {:.2f}'.format(x)
        rospy.loginfo('Solution: x = %0.2f', x)
    else:
        D = req.b*req.b-4*req.a*req.c
        if D < 0:
            message = 'No roots'
            rospy.loginfo("Can't get solution")
        elif D == 0:
            x = -req.b/(2*req.a)
            message = 'x1 = x2 = {:.2f}'.format(x)
            rospy.loginfo('Solution: x = %0.2f', x)
        else:
            x1 = (-req.b+D**0.5)/(2*req.a)
            x2 = (-req.b-D**0.5)/(2*req.a)
            message = 'x1 = {:.2f}, x2 = {:.2f}'.format(x1, x2)
            rospy.loginfo('Solution: x1 = %0.2f, x2 = %0.2f', x1, x2)
    return GetRootsResponse(message)

def quadr_roots_server():
    rospy.init_node('quadr_roots_server')
    s = rospy.Service('quadr_roots', GetRoots, handle_quadr_roots)
    rospy.loginfo('Server ready')
    rospy.spin()

if __name__ == "__main__":
    quadr_roots_server()
