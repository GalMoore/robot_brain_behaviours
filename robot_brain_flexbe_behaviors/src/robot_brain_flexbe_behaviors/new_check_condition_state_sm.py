#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.subscriber_state import SubscriberState
from robot_brain_flexbe_states.word_check_state import WordCheckingState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 26 2019
@author: Gal
'''
class new_check_condition_stateSM(Behavior):
	'''
	new check condition state
	'''


	def __init__(self):
		super(new_check_condition_stateSM, self).__init__()
		self.name = 'new_check_condition_state'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:187 y:238
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:136 y:65
			OperatableStateMachine.add('subscriber',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'word check', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:483 y:91
			OperatableStateMachine.add('word check',
										WordCheckingState(key_word="party"),
										transitions={'found': 'finished', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
