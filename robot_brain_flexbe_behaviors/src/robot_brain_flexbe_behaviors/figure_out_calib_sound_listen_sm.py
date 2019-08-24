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
from robot_brain_flexbe_states.launch_arduino_led import LaunchArduinoLed
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
			# x:47 y:27
			OperatableStateMachine.add('arduino led',
										LaunchArduinoLed(),
										transitions={'continue': 'calib', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:331 y:18
			OperatableStateMachine.add('sub1',
										SubscriberState(topic='/avg_ambience_vol', blocking=True, clear=False),
										transitions={'received': 'log', 'unavailable': 'unavailable'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'vol'})

			# x:722 y:23
			OperatableStateMachine.add('listen',
										ListeningState(),
										transitions={'continue': 'text', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:885 y:357
			OperatableStateMachine.add('calib2',
										SoundCalibState(length_of_calibration=20),
										transitions={'continue': 'sub2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1091 y:395
			OperatableStateMachine.add('sub2',
										SubscriberState(topic='/avg_ambience_vol', blocking=True, clear=False),
										transitions={'received': 'listen2', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'vol'})

			# x:1091 y:237
			OperatableStateMachine.add('listen2',
										ListeningState(),
										transitions={'continue': 'again sub?', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:962 y:41
			OperatableStateMachine.add('text',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'check text', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:701 y:245
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

			# x:958 y:136
			OperatableStateMachine.add('again sub?',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'check text', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:154 y:89
			OperatableStateMachine.add('calib',
										SoundCalibState(length_of_calibration=20),
										transitions={'continue': 'sub1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
