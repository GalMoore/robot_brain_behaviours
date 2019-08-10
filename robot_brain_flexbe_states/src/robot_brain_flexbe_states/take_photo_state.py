#!/usr/bin/env python
import rospy
import datetime
from flexbe_core import EventState, Logger
import cv2

from os.path import expanduser
home = expanduser("~") + "/"

class TakePhotoState(EventState):
	'''
	takes a photo of user! 

	-- target_time 	float 	Time which needs to have passed since the behavior started.

	<= continue 			Given time has passed.
	<= failed 				Example for a failure outcome.

	'''

	def __init__(self):
		# Declare outcomes, input_keys, and output_keys by calling the super constructor with the corresponding arguments.
		super(TakePhotoState, self).__init__(outcomes = ['continue', 'failed'])
		print("in init now")


	def execute(self, userdata):
		Logger.loginfo(datetime.datetime.now().time())
		cam = cv2.VideoCapture(0)
		cv2.namedWindow("test")
		img_counter = 0

		while True:
		    ret, frame = cam.read()
		    cv2.imshow("test", frame)
		    if not ret:
		        break
		    k = cv2.waitKey(1)

		    if k%256 == 27:
		        # ESC pressed
		        print("Escape hit, closing...")
		        break
		    elif k%256 == 32:
		        # SPACE pressed
		        img_name = "{}Desktop/opencv_frame_{}.png".format(home,img_counter)
		        cv2.imwrite(img_name, frame)
		        print("{} written!".format(img_name))
		        img_counter += 1

		cam.release()

		cv2.destroyAllWindows()
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
		
