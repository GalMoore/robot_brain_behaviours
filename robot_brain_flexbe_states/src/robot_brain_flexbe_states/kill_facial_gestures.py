#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger


class KillFacialGesturesState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(KillFacialGesturesState, self).__init__(outcomes = ['continue', 'failed'])

	def execute(self, userdata):
		#os.system("rosrun robot_ears pu_one_msg_stt.py &" )
		Logger.loginfo("killing facial gestures ")
		# Logger.loginfo(userdata.input_value)
		# Logger.loginfo(userdata.input_value)
		# os.system("python /home/intel/catkin_ws/src/robot_face/src/only_lips_and_eyes_waiting_faces.py &")
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		os.system("pgrep -f /home/intel/catkin_ws/src/robot_face/src/only_lips_and_eyes_waiting_faces.py")
		os.system("pkill -9 -f /home/intel/catkin_ws/src/robot_face/src/only_lips_and_eyes_waiting_faces.py")
		pass


	def on_exit(self, userdata):
		# Logger.loginfo('leaving facial gestures state')
		pass # Nothing to do in this example.

	def on_start(self):
		pass

	def on_stop(self):
		pass # Nothing to do in this example.
		
