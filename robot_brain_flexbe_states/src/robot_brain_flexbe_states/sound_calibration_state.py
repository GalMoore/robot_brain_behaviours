#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
from std_msgs.msg import String, Int16
import rospy


class SoundCalibState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self,length_of_calibration):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(SoundCalibState, self).__init__(outcomes = ['continue', 'failed'])
		self.length = length_of_calibration
	
	# def get_avg_callback(self, data):
	# 		Logger.loginfo(data)

	def execute(self, userdata):
		os.system("rostopic pub /avg_ambience_vol std_msgs/Int16 \"data: 0\" &") # does this help get the topic started?
		os.system("rosrun robot_ears sound_calibration_node.py {}".format(self.length))
		Logger.loginfo("rosrun robot_ears sound_calibration_node.py {}".format(self.length))
		Logger.loginfo("finished calib")

		# rospy.Subscriber('/avg_ambience_vol', self.get_avg_callback)



		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		pass

	def on_exit(self, userdata):
		# This method is called when an outcome is returned and another state gets active.
		# It can be used to stop possibly running processes started by on_enter.
		Logger.loginfo('leaving listening state')
		pass # Nothing to do in this example.




