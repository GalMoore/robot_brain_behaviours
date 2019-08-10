#!/usr/bin/env python
import rospy
import datetime
from flexbe_core import EventState, Logger
import cv2

class TrackingState(EventState):
	'''
	takes a photo of user! 

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(TrackingState, self).__init__(outcomes = ['continue', 'stop_tracking','failed'])
		rospy.Subscriber('chat_strings', String, callback)

	def execute(self, userdata):
		Logger.loginfo("in execute loop")
		return 'continue'
		
	def on_enter(self, userdata):
		Logger.loginfo('logging on_enter photo')

	def on_exit(self, userdata):
		Logger.loginfo('leaving and loggin photo')
		pass # Nothing to do in this example.

	def on_start(self):
		print("doing nothing on start")

	def on_stop(self):
		pass # Nothing to do in this example.
		
