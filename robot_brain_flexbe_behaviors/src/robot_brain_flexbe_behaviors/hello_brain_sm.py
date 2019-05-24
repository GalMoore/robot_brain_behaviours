#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.wait_state import WaitState
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.example_state import ExampleState
from robot_brain_flexbe_states.take_photo_state import TakePhotoState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 12 2019
@author: Me
'''
class Hello_BrainSM(Behavior):
	'''
	Brain description
	'''


	def __init__(self):
		super(Hello_BrainSM, self).__init__()
		self.name = 'Hello_Brain'

		# parameters of this behavior
		self.add_parameter('waiting_time', 0)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		hello = "Hello World"
		# x:30 y:365, x:332 y:473
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:131 y:60
			OperatableStateMachine.add('waiter',
										WaitState(wait_time=self.waiting_time),
										transitions={'done': 'example_State'},
										autonomy={'done': Autonomy.Off})

			# x:633 y:55
			OperatableStateMachine.add('printer',
										LogState(text=hello, severity=Logger.REPORT_HINT),
										transitions={'done': 'phototaker'},
										autonomy={'done': Autonomy.Off})

			# x:348 y:60
			OperatableStateMachine.add('example_State',
										ExampleState(target_time=3),
										transitions={'continue': 'printer', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:401 y:249
			OperatableStateMachine.add('phototaker',
										TakePhotoState(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
