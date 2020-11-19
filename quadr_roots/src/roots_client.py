#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from quadr_roots.srv import *

def quadr_roots_client(a, b, c):
    rospy.wait_for_service('quadr_roots')
    try:
        quadr_roots = rospy.ServiceProxy('quadr_roots', GetRoots)
        resp1 = quadr_roots(a, b, c)
        return resp1.message
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s a b c"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        c = float(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print(quadr_roots_client(a, b, c))
