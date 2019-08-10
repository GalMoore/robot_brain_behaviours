#!/usr/bin/env python
import rospy
import subprocess

from flexbe_core import EventState, Logger
import time
from os.path import expanduser
home = expanduser("~") + "/"

class MoveRobotLipsState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self, target_time):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(MoveRobotLipsState, self).__init__(outcomes = ['continue', 'failed'])
		self._target_time = rospy.Duration(target_time)
		self._start_time = None

	def execute(self, userdata):		
		if rospy.Time.now() - self._start_time > self._target_time:
			return 'continue' # One of the outcomes declared above.
		
	def on_enter(self, userdata):
			# #  OPEN LIPS!
        python_bin3 = "/usr/bin/python3"
        subprocess.Popen([python_bin3, "{}toibot_ws/src/ToiBot1/src/toi_bot_speakers/src/move_lips_temp.py".format(home)]).wait()

	def on_exit(self, userdata):
		# #  OPEN LIPS!
        python_bin3 = "/usr/bin/python3"
        subprocess.Popen([python_bin3, "{}toibot_ws/src/ToiBot1/src/toi_bot_speakers/src/close_lips_temp.py".format(home)]).wait()

		Logger.loginfo('leaving and loggin')
		pass # Nothing to do in this example.

	def on_start(self):
		self._start_time = rospy.Time.now()

	def on_stop(self):
		pass # Nothing to do in this example.
		
