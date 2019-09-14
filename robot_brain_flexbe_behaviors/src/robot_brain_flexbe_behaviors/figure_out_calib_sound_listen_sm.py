#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robot_brain_flexbe_states.launch_arduino_led import LaunchArduinoLed
from robot_brain_flexbe_states.listening_state import ListeningState
from robot_brain_flexbe_states.sound_calibration_state import SoundCalibState
from robot_brain_flexbe_states.word_check_state import WordCheckingState
from robot_brain_flexbe_states.read_txt_and_msg_out import ReadTxtState
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

			# x:550 y:45
			OperatableStateMachine.add('listen',
										ListeningState(),
										transitions={'continue': 'read2txtstring', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'my_amb'})

			# x:591 y:446
			OperatableStateMachine.add('calib2',
										SoundCalibState(length_of_calibration=20),
										transitions={'continue': 'read2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:814 y:411
			OperatableStateMachine.add('listen2',
										ListeningState(),
										transitions={'continue': 'read5', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:585 y:257
			OperatableStateMachine.add('check text',
										WordCheckingState(key_word="again"),
										transitions={'found': 'calib2', 'not_found': 'failed'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:150 y:122
			OperatableStateMachine.add('calib',
										SoundCalibState(length_of_calibration=20),
										transitions={'continue': 'read', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:343 y:141
			OperatableStateMachine.add('read',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/volume_calib.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'listen'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'my_amb'})

			# x:778 y:50
			OperatableStateMachine.add('read2txtstring',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/query.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'check text'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'message'})

			# x:804 y:513
			OperatableStateMachine.add('read2',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/volume_calib.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'listen2'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'vol'})

			# x:822 y:276
			OperatableStateMachine.add('read5',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/query.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'check text'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'message'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
