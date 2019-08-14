#!/usr/bin/env python

import rospy
from flexbe_core import EventState, Logger

'''
Created on 02/24/2015

@author: Philipp Schillinger
'''

class WordCheckingStringState(EventState):
	'''
	Checks if the given condition is true and returns the corresponding outcome.
	This state can be used if the further control flow of the behavior depends on a simple condition.
	
	-- predicate    function	The condition whose truth value will be evaluated.
								Has to expect one parameter which will be set to input_value and return a boolean.

	># input_value	object		Input to the predicate function.

	<= true 					Returned if the condition evaluates to True
	<= false 					Returned if the condition evaluates to False
	
	'''

	def __init__(self,key_word):
		'''Constructor'''
		super(WordCheckingStringState, self).__init__(outcomes=['found', 'not_found'],
													input_keys=['input_value'])
		
		self._key_word = key_word
		# self._message_location = message_location
		self._outcome = 'not_found'
		
	def execute(self, userdata):
		'''Execute this state'''
		Logger.logwarn("execute")
		Logger.logwarn(self._key_word)
		Logger.logwarn(userdata.input_value.data)
		Logger.logwarn("are they the same?")
		Logger.logwarn(userdata.input_value.data==self._key_word)
		self._outcome = 'found' if self._key_word in userdata.input_value.data else 'not_found'
		return self._outcome
		
	def on_enter(self, userdata):
		# print("yo yo yo")
		# print(self._key_word)
		# Logger.logwarn("yo yo yo ")

		pass
		# print(userdata.input_value)
		# try:				
		# 	# self._outcome = 'found' if self._predicate(userdata.input_value) else 'not found'
		# 	Logger.logwarn("input message from subscriber: " + userdata.input_value)
		# 	Logger.logwarn("im looking through last phrase for the word: " + self._key_word)
		# 	self._outcome = 'found' if self._key_word in userdata.input_value else 'not_found'
		# 	if self._key_word in userdata.input_value:

		# 		print("found the word " + self._key_word)
		# 		Logger.logwarn("found the word " + self._key_word)
		# 	else:
		# 		print("did not find the word " + self._key_word)
		# 		Logger.logwarn("didn't find the word " + self._key_word + " only got this: " + userdata.input_value)

		# except Exception as e:
		# 	Logger.logwarn('Failed to execute condition function!\n%s' % str(e))


			
