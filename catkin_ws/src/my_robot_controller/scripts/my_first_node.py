#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node('test_node')
    rospy.loginfo("Test node has been started.")
    #rospy Rate is a class that is used to define frequency for a loop
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        rospy.loginfo("Hello ROS!")
        #rate.sleep() will make sure that loop runs at 10Hz
        rate.sleep()
    
    