#!/usr/bin/env python

import sys
import time
import rospy
from std_msgs.msg import UInt32
from msg_types import *
import baxter_interface
from baxter_interface import Gripper, Head, Limb
from std_msgs.msg import String

class Baxter_Deli(object):
	
	def __init__(self):
		
		self.rightg = Gripper('right')
		self.rightg.set_holding_force(100)
		self.leftg = Gripper('left')
		self.right = Limb('right')
		self.left = Limb('left')
		self.head = Head()

		self.angles= list()

		
		rospy.Subscriber("command", String, self.command)
		rospy.spin()

	def command(self, comm):
		if comm.data == "left":
			self.angles.append(self.left.joint_angles())
		elif comm.data == "right":
			self.angles.append(self.right.joint_angles())
		elif comm.data == "done":
			print self.angles







if __name__ == '__main__':

	rospy.init_node("baxter_deli")

	try:

		client = Baxter_Deli()
		
	except rospy.ROSInterruptException: pass