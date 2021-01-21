#!/usr/bin/env python
import rospy
import numpy as np
from open_manipulator_msgs.srv import *
from open_manipulator_msgs.msg import *
from time import sleep
import math

class ArmController:
    def __init__(self,movetime=.5):
        rospy.wait_for_service('goal_joint_space_path')
        rospy.wait_for_service('goal_tool_control')
        rospy.init_node('si475_arm_control',anonymous=True)
        rospy.Subscriber('/gripper/kinematics_pose',KinematicsPose,self.__storepose)
        self.count=0
        self.movetime=movetime
        self.close_tool()
    def __storepose(self,data):
        self.tool_pose=data.pose
    def set_joints(self,joint_angles):
        jp=JointPosition()
        jp.joint_name=['joint1','joint2','joint3','joint4']
        jp.position=np.array([0,0,0,0],dtype=np.float64)
        sjp=rospy.ServiceProxy('goal_joint_space_path',SetJointPosition)
        jp.position=np.array(joint_angles,dtype=np.float64)
        sjp('motion'+str(self.count),jp,self.movetime)
        self.count+=1
        sleep(self.movetime)
    def close_tool(self):
        jp=JointPosition()
        jp.joint_name=['gripper']
        jp.position=np.array([-.01],dtype=np.float64)
        sjp=rospy.ServiceProxy('goal_tool_control',SetJointPosition)
        thing=sjp('motion'+str(self.count),jp,self.movetime)
        self.count+=1
        sleep(self.movetime)
    def open_tool(self):
        jp=JointPosition()
        jp.joint_name=['gripper']
        jp.position=np.array([.01],dtype=np.float64)
        sjp=rospy.ServiceProxy('goal_tool_control',SetJointPosition)
        thing=sjp('motion'+str(self.count),jp,self.movetime)
        self.count+=1
        sleep(self.movetime)
    def get_pose(self):
        position=np.array([self.tool_pose.position.x,
                self.tool_pose.position.y,
                self.tool_pose.position.z])
        (x,y,z,w)=(self.tool_pose.orientation.x,
                self.tool_pose.orientation.y,
                self.tool_pose.orientation.z,
                self.tool_pose.orientation.w)
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

        orientation=np.array([roll_x, pitch_y, yaw_z])
        return {'position':position,'orientation':orientation}
