#!/usr/bin/env python

import rospy
from flexbe_core import EventState, Logger

'''
Created on 02/24/2015

@author: Philipp Schillinger
'''

class AgeGenderCheckingState(EventState):
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
		super(AgeGenderCheckingState, self).__init__(outcomes=['found', 'not_found'],
													input_keys=['input_value'],output_keys=['age','gender'])
		
		# self._key_word = key_word
		# self._message_location = message_location
		self._outcome = 'not_found'
		
		
	def execute(self, userdata):
		'''Execute this state'''
		userdata.age = userdata.input_value.objects[0].age
		userdata.gender = userdata.input_value.objects[0].gender
		return self._outcome
		
	
	def on_enter(self, userdata):
		print(" ")
		Logger.logwarn("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].gender))
		print("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].gender))
		Logger.logwarn("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].age))
		print("userdata.input_value.objects[0].gender is: " + str(userdata.input_value.objects[0].age))
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
