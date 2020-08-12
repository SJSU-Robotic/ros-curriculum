#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    smallest_dist_msmt = data.range_min
    rospy.loginfo("smallest distance measurement: %s", smallest_dist_msmt)

def listener():
    rospy.init_node('husky_highlevel_controller')
    rospy.Subscriber('scan', LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()