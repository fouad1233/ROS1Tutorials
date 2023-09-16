#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
def main():
        # Initialize the node with rospy.init_node()
    rospy.init_node('draw_circle')
    # Print loginfo to screen
    rospy.loginfo("Draw circle node has been started.")
    
    
    # Create a publisher with rospy.Publisher(<topic_name>, <message_type>, queue_size=<queue_size>)
    # The queue_size argument is optional and it determines how many messages can be stored in the queue before messages are dropped.
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    
    rate = rospy.Rate(2)
    
    while not rospy.is_shutdown():
        # Create a new Twist message
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        
        #publish cmd vel
        pub.publish(msg)
        rate.sleep()
if __name__ == '__main__':
    main()

        