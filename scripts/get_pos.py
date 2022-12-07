#!usr/bin/env python
import rospy
import math

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def get_pose():
        t= Twist()
        o =Odometry()
        o.header.frame_id = 'odom'
        o.child_frame_id= 'base_link'
        init_pos_x = o.pose.pose.position.x
        init_pos_y = o.pose.pose.position.y
        print("initial positions: ",init_pos_x, init_pos_y)
        rospy.init_node('Robot_pose', anonymous=True)
        pub_twist = rospy.Publisher('/vehicle_assembly/cmd_vel', Twist, queue_size=10)
        
        rate = rospy.Rate(10) # 10hz
        
        Kp=0.2
        goal1_x_pos = -5.0
        goal1_y_pos = -5.0
        i=0
        j=0
        if(goal1_y_pos<0):
            y_vel = -1
        else:
            y_vel = 1
        if(goal1_x_pos<0):
            x_vel = -1
        else:
            x_vel = 1

        y1_dis= goal1_y_pos-init_pos_y
        x1_dis= goal1_x_pos-init_pos_x
        while(i!=(y1_dis+y_vel)):
            print('\nupdated i:', i)
            t.linear.y = y_vel
            pub_twist.publish(t)
            i=i+y_vel
            print("Odometry: values\n", o.pose.pose.position)
            rospy.sleep(1) 
        
        t.linear.y = 0
        pub_twist.publish(t)

        while(j!=(x1_dis)):
            print('\nupdated j:', j)
            t.linear.x = x_vel
            pub_twist.publish(t)
            j=j+x_vel
            rospy.sleep(1)

        t.linear.x=0
        pub_twist.publish(t)

   
if __name__ == '__main__':
       try:
           get_pose()
       except rospy.ROSInterruptException:
           pass
