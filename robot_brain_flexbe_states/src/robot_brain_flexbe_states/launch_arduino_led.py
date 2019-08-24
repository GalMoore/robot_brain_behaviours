#!/usr/bin/env python
import rospy
import os
from flexbe_core import EventState, Logger
import subprocess
import time 
# import rospy		
from os.path import expanduser
home = expanduser("~") + "/"

class LaunchArduinoLed(EventState):
	'''
	Example for a state to demonstrate which functionality is available for state implementation.
	This example lets the behavior wait until the given target_time has passed since the behavior has been started.

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(LaunchArduinoLed, self).__init__(outcomes = ['continue', 'failed'])
		self._start_time = None
		# self._ttyACMport = ttyACMport

	def execute(self, userdata):
		time.sleep(0.2)
		# os.system("rostopic pub /avg_ambience_vol std_msgs/Int16 \"data: 0\" &") # does this help get the topic started?

		os.system("rostopic pub /is_robot_listening std_msgs/String \"data: 'not listening'\" &")
		return 'continue' # One of the outcomes declared above.

	def on_enter(self, userdata):
		# os.system("roslaunch video_stream_opencv camera.launch video_stream_provider:={} &".format(self._vid_input_num))

		os.system("rosrun robot_arduino PythonArduino.py &")
		Logger.loginfo('starting arduino led')

	def on_exit(self, userdata):
		pass # Nothing to do in this example.

	def on_start(self):
		pass

	def on_stop(self):
		#os.system("pgrep -f face_motor_server.py")
		#os.system("pkill -9 -f face_motor_server.py")
		Logger.loginfo('on_stop stopping the arduino led')
		pass # Nothing to do in this example.
		
