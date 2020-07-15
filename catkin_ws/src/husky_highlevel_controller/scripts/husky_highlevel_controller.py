#!/usr/bin/env python
import rospy
from math import sin, cos
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

# global refs for callback()
k_p       = None # set this via rospy.get_param() after node init
twist_pub = None # initialize this after node init

# execise 3 calls for a P controller
def p_control(feedback, setpoint = 0):
    global k_p
    """
    inputs
        k_p: proportional factor
        feedback: control feedback (this is the sensor input)
        setpoint: control setpoint (this is the target value)
    output
        output = k_p * (feedback - setpoint)
    """
    return k_p * (feedback - setpoint)

def get_min_index(a_list):
    return [index for index in range(0, len(a_list)) if a_list[index] == min(a_list)][0]

def get_angle(ranges_index, angle_min, angle_increment):
    return angle_min + ranges_index * angle_increment

def callback(data):
    global twist_pub
    # don't use data.range_min with the intention of scan data this is a meta-parameter defining 
    #     the LIDAR's lower-bound detectability
    # instead, use ranges, and extract the minimum value
    dist  = min(data.ranges)
    angle = get_angle(get_min_index(data.ranges), data.angle_min, data.angle_increment)
    # find angle at which smallest_dist was found
    rospy.loginfo("dist: %s, angle: %s" % (dist, angle))

    # prop/attitude control
    #   if we are perpendicular to target, then set v_x to zero and rotate in place
    #   else if we are straight on target, maximize v_x and assert zero yaw
    #   gradations in between these are well defined by cos() and sin()
    # here we want to get as close as we can get, which is the LIDAR's lower bound range_min
    v_x = p_control(dist, data.range_min) * cos(angle)
    # we want to be on target, so setpoint is 0. note LIDAR frame is flipped 180 deg from base frame
    #   so we should negate our angle. Instead of negating angle at the input of both p_control()
    #   and sin(), we can just negate at the output of sin()
    # w_z = p_control(-angle, 0) * sin(-angle)
    w_z = p_control(angle, 0) * -sin(angle)
    twist_msg = Twist()
    twist_msg.linear.x = v_x
    twist_msg.angular.z = w_z
    twist_pub.publish(twist_msg) 



def listener(scan_topic, queue_size):
    rospy.Subscriber(scan_topic, LaserScan, callback, queue_size=queue_size)
    rospy.spin()

if __name__ == '__main__':
    # init-ing in main allows us to work with rospy API for name/node info right away
    # for more, see: http://wiki.ros.org/rospy/Overview/Names%20and%20Node%20Information
    rospy.init_node('husky_highlevel_controller')

    # get values from the ROS Parameter Server
    k_p  = rospy.get_param(rospy.get_name() + "/k_p", 0.5)
    scan_topic  = rospy.get_param(rospy.get_name() + "/scan_topic")
    queue_size  = rospy.get_param(rospy.get_name() + "/queue_size")
    twist_topic = rospy.get_param(rospy.get_name() + "/twist_topic", "/cmd_vel")

    # we can also set a default value for these parameters, 
    #   but we want to error out if the key for some reason isn't present
    # scan_topic = rospy.get_param(rospy.get_name() + "/scan_topic", "scan")
    # queue_size = rospy.get_param(rospy.get_name() + "/queue_size", "1")
    
    twist_pub = rospy.Publisher(twist_topic, Twist)
    listener(scan_topic, queue_size)