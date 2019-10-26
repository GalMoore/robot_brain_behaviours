#!/usr/bin/env python
import rospy
import subprocess
import random

from flexbe_core import EventState, Logger
import time
import os
from os.path import expanduser
home = expanduser("~") + "/"

class DecideTalkState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(DecideTalkState, self).__init__(outcomes = ['continue1', 'continue2','continue3'])
		# self._sentence = sentence_number
		# self._start_time = None

	def execute(self, userdata):
		selection = random.randint(1,3)
		if selection==1:
			Logger.loginfo('selecting random sentence 1')
			return 'continue1'
		elif selection==2:
			Logger.loginfo('selecting random sentence 2')
			return 'continue2' # One of the outcomes declared above.
		elif selection==3:
			Logger.loginfo('selecting random sentence 3')
			return 'continue3'

		
	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		
		pass # Nothing to do in this example.

	def on_start(self):
		# In this example, we use this event to set the correct start time.
		# self._start_time = rospy.Time.now()
		pass

	def on_stop(self):
		pass # Nothing to do in this example.
		
