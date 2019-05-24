#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robot_brain_flexbe_states.talk_last_response import Talk_Last_Response
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.take_photo_state import TakePhotoState
from robot_brain_flexbe_states.move_robot_State import MoveRobotLipsState
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.check_condition_state import CheckConditionState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 12 2019
@author: galgush
'''
class trackandnotrackSM(Behavior):
	'''
	track and no track
	'''


	def __init__(self):
		super(trackandnotrackSM, self).__init__()
		self.name = 'track and no track'

		# parameters of this behavior
		self.add_parameter('wait_time', 0)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:150 y:452
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:283 y:40
			OperatableStateMachine.add('say',
										Talk_Last_Response(target_time=1),
										transitions={'continue': 'sub', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:457 y:297
			OperatableStateMachine.add('logfalse',
										LogState(text="false", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub'},
										autonomy={'done': Autonomy.Off})

			# x:391 y:168
			OperatableStateMachine.add('unavailable_topic_string_log',
										LogState(text="the topic is not available so finishing", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:973 y:355
			OperatableStateMachine.add('takephoto',
										TakePhotoState(),
										transitions={'continue': 'move_lips', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:975 y:444
			OperatableStateMachine.add('move_lips',
										MoveRobotLipsState(target_time=0),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:776 y:71
			OperatableStateMachine.add('sub',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'chyeck', 'unavailable': 'unavailable_topic_string_log'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:778 y:303
			OperatableStateMachine.add('chyeck',
										CheckConditionState(predicate=lambda message: message.query == "take photo"),
										transitions={'true': 'takephoto', 'false': 'logfalse'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
