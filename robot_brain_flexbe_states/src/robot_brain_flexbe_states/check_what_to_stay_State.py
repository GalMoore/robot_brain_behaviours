#!/usr/bin/env python

import rospy
from flexbe_core import EventState, Logger
import os
'''
Created on 02/24/2015

@author: Philipp Schillinger
'''

class AgeGenderCheckSpeechState(EventState):
	'''
	Checks if the given condition is true and returns the corresponding outcome.
	This state can be used if the further control flow of the behavior depends on a simple condition.
	
	-- predicate    function	The condition whose truth value will be evaluated.
								Has to expect one parameter which will be set to input_value and return a boolean.

	># input_value	object		Input to the predicate function.

	<= true 					Returned if the condition evaluates to True
	<= false 					Returned if the condition evaluates to False
	
	'''


	def __init__(self):
		'''Constructor'''
		super(AgeGenderCheckSpeechState, self).__init__(outcomes=['found', 'not_found'],
													input_keys=['age','gender'])
		# self._key_word = key_word
		# self._message_location = message_location
		self._outcome = 'not_found'
		# self._age = userdata.age
		# self._gender = gender
		
	def execute(self, userdata):
		'''Execute this state'''


		print("age: " +str(userdata.age))
		print("gender: " +str(userdata.gender))
		Logger.logwarn("age: " +str(userdata.age))
		Logger.logwarn("gender: " +str(userdata.gender))

		print("talking now")

		if(userdata.age>40 and userdata.gender=="Male"):
			os.system("python3 /home/gal/catkin_ws/src/robot_voice/src/ohbot_say_function.py %s" %(str(7)))
		if(userdata.age<40 and userdata.gender=="Male"):
			os.system("python3 /home/gal/catkin_ws/src/robot_voice/src/ohbot_say_function.py %s" %(str(8)))
		if(userdata.gender=="Female"):
			os.system("python3 /home/gal/catkin_ws/src/robot_voice/src/ohbot_say_function.py %s" %(str(9)))

		return self._outcome
		
	
	def on_enter(self, userdata):
		# print("age: " +str(self._age))
		# print("gender: " +str(self._gender))
		# Logger.logwarn("age: " +str(self._age))
		# Logger.logwarn("gender: " +str(self._gender))
		pass
		# print(" ")
		# Logger.logwarn("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].gender))
		# print("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].gender))
		# Logger.logwarn("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].age))
		# print("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].age))
		# try:
		# 	# self._outcome = 'found' if self._predicate(userdata.input_value) else 'not found'
		# 	self._outcome = 'found' if self._key_word in userdata.input_value.objects[0].gender else 'not_found'
		# 	if self._key_word in userdata.input_value:

		# 		print("found the word " + self._key_word)
		# 		Logger.logwarn("found the word " + self._key_word)
		# 	else:
		# 		print("did not find the word " + self._key_word)
		# 		Logger.logwarn("didn't find the word " + self._key_word)

		# except Exception as e:
		# 	Logger.logwarn('Failed to execute condition function!\n%s' % str(e))
