#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy		
class IdentifyState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(IdentifyState, self).__init__(outcomes = ['continue', 'failed'])

		# self._start_time = None

	def execute(self, userdata):
		os.system("rosrun robot_identify identify_node.py &")
		Logger.loginfo('looking for familiar faces to identify')
		Logger.loginfo('publishing found face names to /identified_people_string_name')
		# print("executing")
		# if rospy.Time.now() - self._start_time > self._target_time:
		return 'continue' # One of the outcomes declared above.
		
	def on_enter(self, userdata):
		pass
		# os.system("rosrun robot_tracking face_tracking_from_vino.py &")
		# Logger.loginfo("start tracking")

	# def on_exit(self, userdata):
	# 	pass # Nothing to do in this example.

	# def on_start(self):
	# 	self._start_time = rospy.Time.now()

	def on_stop(self):
		os.system("rosnode kill /robot_identify")
		pass # Nothing to do in this example.
		
