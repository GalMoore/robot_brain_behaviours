#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy		
from os.path import expanduser
home = expanduser("~") + "/"

class LaunchFaceServer(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(LaunchFaceServer, self).__init__(outcomes = ['continue', 'failed'])
		self._start_time = None

	def execute(self, userdata):
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		# JUST IN CASE ALREADY RUNNING - KILL SCRIPT FIRST
		os.system("pgrep -f face_motor_server.py")
		os.system("pkill -9 -f face_motor_server.py")
		os.system("python3 {}catkin_ws/src/robot_face/src/face_motor_server.py &".format(home))
		Logger.loginfo('starting face motor server')

	def on_exit(self, userdata):
		pass # Nothing to do in this example.

	def on_start(self):
		pass

	def on_stop(self):
		pass # Nothing to do in this example.
		
