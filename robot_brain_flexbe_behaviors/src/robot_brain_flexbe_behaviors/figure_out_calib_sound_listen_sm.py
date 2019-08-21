#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robot_brain_flexbe_states.sound_calibration_state import SoundCalibState
from flexbe_states.subscriber_state import SubscriberState
from robot_brain_flexbe_states.listening_state import ListeningState
from robot_brain_flexbe_states.word_check_state import WordCheckingState
from robot_brain_flexbe_states.log_input_data import LogTopicMessage
from flexbe_states.log_state import LogState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Aug 15 2019
@author: gal moore
'''
class figure_out_calib_sound_listenSM(Behavior):
	'''
	sound
	'''


	def __init__(self):
		super(figure_out_calib_sound_listenSM, self).__init__()
		self.name = 'figure_out_calib_sound_listen'

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


		with _state_machine:
			# x:95 y:50
			OperatableStateMachine.add('calib',
										SoundCalibState(length_of_calibration=60),
										transitions={'continue': 'sub1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:331 y:18
			OperatableStateMachine.add('sub1',
										SubscriberState(topic='/avg_ambience_vol', blocking=True, clear=False),
										transitions={'received': 'log', 'unavailable': 'unavailable'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'vol'})

			# x:561 y:199
			OperatableStateMachine.add('listen',
										ListeningState(),
										transitions={'continue': 'text', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:708 y:107
			OperatableStateMachine.add('calib2',
										SoundCalibState(length_of_calibration=120),
										transitions={'continue': 'sub2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:963 y:137
			OperatableStateMachine.add('sub2',
										SubscriberState(topic='/avg_ambience_vol', blocking=True, clear=False),
										transitions={'received': 'listen2', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'vol'})

			# x:843 y:295
			OperatableStateMachine.add('listen2',
										ListeningState(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:609 y:386
			OperatableStateMachine.add('text',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'check text', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:744 y:514
			OperatableStateMachine.add('check text',
										WordCheckingState(key_word="again"),
										transitions={'found': 'calib2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:515 y:26
			OperatableStateMachine.add('log',
										LogTopicMessage(),
										transitions={'continue': 'listen', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:234 y:171
			OperatableStateMachine.add('unavailable',
										LogState(text="Sub1 NAVAILABLE", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub1'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
