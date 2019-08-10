#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger


class ListeningState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(ListeningState, self).__init__(outcomes = ['continue', 'failed'])

	def execute(self, userdata):
		os.system("rostopic pub /is_robot_listening std_msgs/String \"data: 'listening'\" &" )
		os.system("rosrun robot_ears speech_to_text.py &")
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		Logger.loginfo("(not actually connected to ambience threshold input - to do)")
		pass

	def on_exit(self, userdata):
		Logger.loginfo('leaving listening state')
		pass # Nothing to do in this example.

	def on_start(self):
		pass

	def on_stop(self):
		pass # Nothing to do in this example.
		
