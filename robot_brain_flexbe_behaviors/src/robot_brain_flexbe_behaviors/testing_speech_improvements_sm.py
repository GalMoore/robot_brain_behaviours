#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from flexbe_states.log_state import LogState
from flexbe_states.wait_state import WaitState
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.check_condition_state import CheckConditionState
from robot_brain_flexbe_states.listening_state import ListeningState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Jul 31 2019
@author: Gal Moore
'''
class testing_speech_improvementsSM(Behavior):
	'''
	testing speech improvements
	'''


	def __init__(self):
		super(testing_speech_improvementsSM, self).__init__()
		self.name = 'testing_speech_improvements'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:242 y:161
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:241 y:23
			OperatableStateMachine.add('log',
										LogState(text="logged to get started :-) ", severity=Logger.REPORT_HINT),
										transitions={'done': 'listennow'},
										autonomy={'done': Autonomy.Off})

			# x:936 y:282
			OperatableStateMachine.add('wait4',
										WaitState(wait_time=3),
										transitions={'done': 'subto'},
										autonomy={'done': Autonomy.Off})

			# x:913 y:34
			OperatableStateMachine.add('is_listening',
										SubscriberState(topic='/is_robot_listening', blocking=True, clear=False),
										transitions={'received': 'check listen or not', 'unavailable': 'check listen or not'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:1122 y:153
			OperatableStateMachine.add('check listen or not',
										CheckConditionState(predicate=lambda message: message.data == "not listening"),
										transitions={'true': 'listen2', 'false': 'is_listening'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:709 y:49
			OperatableStateMachine.add('wait2',
										WaitState(wait_time=1),
										transitions={'done': 'is_listening'},
										autonomy={'done': Autonomy.Off})

			# x:522 y:205
			OperatableStateMachine.add('chk',
										CheckConditionState(predicate=lambda message: message.data == "not listening"),
										transitions={'true': 'fin', 'false': 'subto'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:328 y:237
			OperatableStateMachine.add('fin',
										LogState(text="finished interaction", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:460 y:24
			OperatableStateMachine.add('listennow',
										ListeningState(),
										transitions={'continue': 'wait2', 'failed': 'wait2'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1048 y:421
			OperatableStateMachine.add('listen2',
										ListeningState(),
										transitions={'continue': 'wait4', 'failed': 'wait4'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:730 y:302
			OperatableStateMachine.add('subto',
										SubscriberState(topic='/is_robot_listening', blocking=True, clear=False),
										transitions={'received': 'chk', 'unavailable': 'chk'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
