#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy		
class LaunchVideoStream(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(LaunchVideoStream, self).__init__(outcomes = ['continue', 'failed'])
		self._start_time = None

	def execute(self, userdata):
		print("executing")
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		Logger.loginfo('entered state launch video stream')
		os.system("roslaunch video_stream_opencv camera.launch &")
		Logger.loginfo('launched video stream (topic publishing video)')

	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.
		Logger.loginfo('leaving and logging')
		pass # Nothing to do in this example.

	def on_start(self):
		pass

	def on_stop(self):
		pass # Nothing to do in this example.
		
