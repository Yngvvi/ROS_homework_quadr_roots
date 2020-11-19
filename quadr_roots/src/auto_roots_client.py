#!/usr/bin/env python

from __future__ import print_function

import rospy
from quadr_roots.srv import *
import random


def quadr_roots_client(a, b, c):
    rospy.wait_for_service('quadr_roots')
    try:
        quadr_roots = rospy.ServiceProxy('quadr_roots', GetRoots)
        resp1 = quadr_roots(a, b, c)
        return resp1.message
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)


if __name__ == "__main__":
    rospy.init_node('quadr_roots_client', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        a = round(random.random()*100 - 50, 2)
        b = round(random.random()*100 - 50, 2)
        c = round(random.random()*100 - 50, 2)
        print('Input coefficients: a = {}, b = {}, c = {}'.format(a, b, c))
        print(quadr_roots_client(a, b, c))
        rate.sleep()
