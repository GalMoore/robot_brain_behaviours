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
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 12 2019
@author: Gal Moore
'''
class robot_brainSM(Behavior):
	'''
	high level state machine for robot brain
	'''


	def __init__(self):
		super(robot_brainSM, self).__init__()
		self.name = 'robot_brain'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:54 y:385, x:100 y:523
		_sm_safety_monitor_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_safety_monitor_0:
			# x:289 y:57
			OperatableStateMachine.add('subscribe to safety topic 1',
										SubscriberState(topic='/chatter', blocking=True, clear=False),
										transitions={'received': 'check if topic publishes warning', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:719 y:64
			OperatableStateMachine.add('fine continue log',
										LogState(text="continue log", severity=Logger.REPORT_HINT),
										transitions={'done': 'subscribe to safety topic 1'},
										autonomy={'done': Autonomy.Off})

			# x:690 y:202
			OperatableStateMachine.add('check if topic publishes warning',
										CheckConditionState(predicate=lambda message: message.data == "1"),
										transitions={'true': 'fine continue log', 'false': 'stop now log'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:451 y:481
			OperatableStateMachine.add('stop now log',
										LogState(text="stopping - message receieved", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		# x:30 y:456, x:130 y:456
		_sm_normal_activity_1 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_normal_activity_1:
			# x:338 y:227
			OperatableStateMachine.add('normalactivity',
										LogState(text="normal activity", severity=Logger.REPORT_HINT),
										transitions={'done': 'wait1'},
										autonomy={'done': Autonomy.Off})

			# x:618 y:312
			OperatableStateMachine.add('wait1',
										WaitState(wait_time=1),
										transitions={'done': 'normalactivity'},
										autonomy={'done': Autonomy.Off})


		# x:113 y:364, x:465 y:451, x:737 y:425, x:254 y:385, x:221 y:448
		_sm_container_2 = ConcurrencyContainer(outcomes=['finished', 'failed'], conditions=[
										('failed', [('normal_activity', 'failed'), ('safety_monitor', 'failed')]),
										('finished', [('normal_activity', 'finished')]),
										('finished', [('safety_monitor', 'finished')])
										])

		with _sm_container_2:
			# x:149 y:54
			OperatableStateMachine.add('normal_activity',
										_sm_normal_activity_1,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:676 y:54
			OperatableStateMachine.add('safety_monitor',
										_sm_safety_monitor_0,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})



		with _state_machine:
			# x:317 y:100
			OperatableStateMachine.add('Container',
										_sm_container_2,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
