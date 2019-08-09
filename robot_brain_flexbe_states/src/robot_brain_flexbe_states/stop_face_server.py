#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy		
from os.path import expanduser
home = expanduser("~") + "/"

class StopFaceServer(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(StopFaceServer, self).__init__(outcomes = ['continue', 'failed'])

		# The constructor is called when building the state machine, not when actually starting the behavior.
		# Thus, we cannot save the starting time now and will do so later.
		self._start_time = None


	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.

		# if rospy.Time.now() - self._start_time > self._target_time:
		return 'continue' # One of the outcomes declared above.
		

	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.
		os.system("pgrep -f face_motor_server.py")
		os.system("pkill -9 -f face_motor_server.py")

		# The following code is just for illustrating how the behavior logger works.
		# Text logged by the behavior logger is sent to the operator and displayed in the GUI.
		Logger.loginfo('stopping the face motor server')



	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.
		# Logger.loginfo('leaving and logging')
		# os.system("python /home/gal/Desktop/stop_object_detection.py")
		# os.system("python /home/gal/Desktop/stop_object_tracking.py")
		pass # Nothing to do in this example.


	def on_start(self):
		pass

	def on_stop(self):
		pass # Nothing to do in this example.
		
