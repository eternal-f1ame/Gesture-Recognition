#!/usr/bin/env python
# license removed for brevity


import rospy
from geometry_msgs.msg import Pose
from nav_msgs.msg import Odometry

def callback(msg):
    print(msg.pose)

rospy.init_node('check_odometry')
odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()


