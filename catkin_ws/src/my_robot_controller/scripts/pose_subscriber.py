#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback(msg:Pose):
    rospy.loginfo("("+str(msg.x)+", "+str(msg.y)+")")
    
    

if __name__ == '__main__':
    
    rospy.init_node('turtle_pose_subscriber')
    #make a rospy subscriber object
    sub = rospy.Subscriber('/turtle1/pose', Pose, callback= pose_callback)
    
    rospy.loginfo("Node has been started")
    #spin() simply keeps python from exiting until this node is stopped and callbacks will continue to be called
    rospy.spin()