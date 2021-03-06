#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
from os.path import expanduser
home = expanduser("~") + "/"


class FacialExpressionState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self, expression_num):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(FacialExpressionState, self).__init__(outcomes = ['continue', 'failed'])

		# Store state parameter for later use.
		self._expression_num = expression_num

		# The constructor is called when building the state machine, not when actually starting the behavior.
		# Thus, we cannot save the starting time now and will do so later.
		# self._start_time = None

	def execute(self, userdata):

		# if rospy.Time.now() - self._start_time > self._target_time:
		return 'continue' # One of the outcomes declared above.				
		
	def on_enter(self, userdata):

		Logger.loginfo("entering FacialExpressionState")
		print("making face now")
		os.system("python3 {}catkin_ws/src/robot_face/src/pick_facial_expression.py {}".format(home,str(self._expression_num)))
		pass

	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.
		Logger.loginfo('leaving FacialExpressionState and logging')
		pass # Nothing to do in this example.

	def on_start(self):
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		# In this example, we use this event to set the correct start time.
		# self._start_time = rospy.Time.now()
		pass

	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		
