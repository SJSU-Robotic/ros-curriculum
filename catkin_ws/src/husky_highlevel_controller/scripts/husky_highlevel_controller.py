#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

# execise 3 calls for a P controller
def p_control(k_p, feedback, setpoint = 0):
    """
    inputs
        k_p: proportional factor
        feedback: control feedback (this is the sensor input)
        setpoint: control setpoint (this is the target value)
    output
        output = k_p * (feedback - setpoint)
    """
    return k_p * (feedback - setpoint)

def callback(data):
    smallest_dist_msmt = data.range_min
    rospy.loginfo("smallest distance measurement: %s", smallest_dist_msmt)

def listener(scan_topic, queue_size):
    rospy.Subscriber(scan_topic, LaserScan, callback, queue_size=queue_size)
    rospy.spin()

if __name__ == '__main__':
    # init-ing in main allows us to work with rospy API for name/node info right away
    # for more, see: http://wiki.ros.org/rospy/Overview/Names%20and%20Node%20Information
    rospy.init_node('husky_highlevel_controller')

    # get values from the ROS Parameter Server
    scan_topic = rospy.get_param(rospy.get_name() + "/scan_topic")
    queue_size = rospy.get_param(rospy.get_name() + "/queue_size")

    # we can also set a default value for these parameters, 
    #   but we want to error out if the key for some reason isn't present
    # scan_topic = rospy.get_param(rospy.get_name() + "/scan_topic", "scan")
    # queue_size = rospy.get_param(rospy.get_name() + "/queue_size", "1")
    
    listener(scan_topic, queue_size)