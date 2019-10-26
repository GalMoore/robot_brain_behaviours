#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger


class FacialGesturesFaceDetState(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(FacialGesturesFaceDetState, self).__init__(outcomes = ['continue', 'failed'])

	def execute(self, userdata):
		#os.system("rosrun robot_ears pu_one_msg_stt.py &" )
		Logger.loginfo("running some facial gestures whilst tracking without eye turn for face det trk ")
		# Logger.loginfo(userdata.input_value)
		# Logger.loginfo(userdata.input_value)
		os.system("python3 /home/intel/catkin_ws/src/robot_face/src/only_lip_etc_eyes_steady.py &")
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		pass


	def on_exit(self, userdata):
		Logger.loginfo('leaving facial gestures state')
		pass # Nothing to do in this example.

	def on_start(self):
		pass

	def on_stop(self):
		os.system("pgrep -f /home/intel/catkin_ws/src/robot_face/src/only_lip_etc_eyes_steady.py")
		os.system("pkill -9 -f /home/intel/catkin_ws/src/robot_face/src/only_lip_etc_eyes_steady.py")
		pass # Nothing to do in this example.
		
