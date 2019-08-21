#!/usr/bin/env python

import rospy
from flexbe_core import EventState, Logger

'''
Created on 02/24/2015

@author: Philipp Schillinger
'''

class LogTopicMessage(EventState):


	def __init__(self):
		'''Constructor'''
		super(LogTopicMessage, self).__init__(outcomes=['continue', 'failed'],
													input_keys=['input_value'])
		# self.calib_level = calib_level
		# self._key_word = key_word
		# self._message_location = message_location
		# self._outcome = 'not_found'
		
	def execute(self, userdata):
		Logger.logwarn("LOGGING THE MESSAGE I GOT FROM SUBSCRIBER: " + str(userdata.input_value.data))
		# userdata.message = userdata.input_value.data
		'''Execute this state'''

		return 'continue'
		


	def on_enter(self, userdata):
		pass
		# try:	
		# 	self._key_word = self._key_word.lower()
			

		# 	# self._outcome = 'found' if self._predicate(userdata.input_value) else 'not found'
		# 	Logger.logwarn("input message from subscriber: " + userdata.input_value.query.lower())
		# 	Logger.logwarn("im looking through last phrase for the word: " + self._key_word)
		# 	self._outcome = 'found' if self._key_word in userdata.input_value.query.lower() else 'not_found'
		# 	if self._key_word in userdata.input_value.query.lower():

		# 		print("found the word " + self._key_word)
		# 		Logger.logwarn("found the word " + self._key_word)
		# 	else:
		# 		print("did not find the word " + self._key_word)
		# 		Logger.logwarn("didn't find the word " + self._key_word + " only got this: " + userdata.input_value.query.lower())

		# except Exception as e:
		# 	Logger.logwarn('Failed to execute condition function!\n%s' % str(e))
