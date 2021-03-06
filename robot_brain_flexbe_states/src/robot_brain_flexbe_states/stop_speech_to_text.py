#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy	


class StopSpeechToText(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(StopSpeechToText, self).__init__(outcomes = ['continue', 'failed'])
		self._start_time = None


	def execute(self, userdata):
		print("executing")
		return 'continue' # One of the outcomes declared above.
		

	def on_enter(self, userdata):
		os.system("rosnode kill robot_ears_node")
		Logger.loginfo("stop video stream")

	def on_exit(self, userdata):
		pass # Nothing to do in this example.


	def on_start(self):
		pass 
		
	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		


