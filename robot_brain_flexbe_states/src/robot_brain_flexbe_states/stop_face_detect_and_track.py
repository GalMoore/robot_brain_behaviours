#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy		
class StopFaceDetectAndTrack(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(StopFaceDetectAndTrack, self).__init__(outcomes = ['continue', 'failed'])

		# Store state parameter for later use.
		# self._target_time = rospy.Duration(target_time)

		# The constructor is called when building the state machine, not when actually starting the behavior.
		# Thus, we cannot save the starting time now and will do so later.
		self._start_time = None

	def execute(self, userdata):
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		os.system("rosnode kill pipeline_with_params")
		Logger.loginfo('stopping object detection')
		os.system("rosnode kill robot_face_tracking_from_vino")
		Logger.loginfo("stop tracking")

	def on_exit(self, userdata):
		pass # Nothing to do in this example.

	def on_start(self):
		self._start_time = rospy.Time.now()

	def on_stop(self):
		pass # Nothing to do in this example.
		
