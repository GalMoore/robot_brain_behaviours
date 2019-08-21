#!/usr/bin/env python
import rospy
import subprocess

from flexbe_core import EventState, Logger
import time
import os
from os.path import expanduser
home = expanduser("~") + "/"

class TalkState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self, sentence_number):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(TalkState, self).__init__(outcomes = ['continue', 'failed'])
		self._sentence = sentence_number
		self._start_time = None

	def execute(self, userdata):
		return 'continue' # One of the outcomes declared above.
		
	def on_enter(self, userdata):
		print("talking now")
		os.system("python3 {}catkin_ws/src/robot_voice/src/ohbot_say_function.py {}".format(home,str(self._sentence)))
		time.sleep(0.2)

	def on_exit(self, userdata):
		Logger.loginfo('finished talking')
		pass # Nothing to do in this example.

	def on_start(self):
		# In this example, we use this event to set the correct start time.
		self._start_time = rospy.Time.now()

	def on_stop(self):
		pass # Nothing to do in this example.
		
