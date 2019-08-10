#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger


class SoundCalibState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(SoundCalibState, self).__init__(outcomes = ['continue', 'failed'])

	def execute(self, userdata):
		# This method is called periodically while the state is active.
		# Main purpose is to check state conditions and trigger a corresponding outcome.
		# If no outcome is returned, the state will stay active.
		# publish to listening topic that we are listening so the state machine 
		
		# can wait till finished listening to move to next state
		# WE DO THIS WITH A SUBSCRIBER STATE AND CHECK CONDITION
		# os.system("rostopic pub /is_robot_listening std_msgs/String \"data: 'listening'\" &" )
		# if rospy.Time.now() - self._start_time > self._target_time:

		# rosrun a ROS node that records for 3 seconds and gets average background volume
		# os.system("rosrun robot_ears speech_to_text.py &")

		return 'continue' # One of the outcomes declared above.


	def on_enter(self, userdata):
		# This method is called when the state becomes active, i.e. a transition from another state to this one is taken.
		# It is primarily used to start actions which are associated with this state.

		# The following code is just for illustrating how the behavior logger works.
		# Text logged by the behavior logger is sent to the operator and displayed in the GUI.

		# time_to_wait = (self._target_time - (rospy.Time.now() - self._start_time)).to_sec()

		# if time_to_wait > 0:
		# Logger.loginfo('setting ambience threshold as %.1f seconds.' % self._ambience_threshold)
		# Logger.loginfo("(not actually connected to ambience threshold input - to do)")
		pass




	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.
		Logger.loginfo('leaving listening state')
		pass # Nothing to do in this example.


	def on_start(self):
		pass
		# This method is called when the behavior is started.
		# If possible, it is generally better to initialize used resources in the constructor
		# because if anything failed, the behavior would not even be started.

		# In this example, we use this event to set the correct start time.
		# self._start_time = rospy.Time.now()


	def on_stop(self):
		# This method is called whenever the behavior stops execution, also if it is cancelled.
		# Use this event to clean up things like claimed resources.

		pass # Nothing to do in this example.
		
