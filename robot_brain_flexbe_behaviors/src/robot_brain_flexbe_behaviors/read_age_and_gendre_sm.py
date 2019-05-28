#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from robot_brain_flexbe_states.launch_video_stream_state import LaunchVideoStream
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from flexbe_states.wait_state import WaitState
from flexbe_states.subscriber_state import SubscriberState
from robot_brain_flexbe_states.stop_camera_stream import StopCameraStream
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.gender_check_state import AgeGenderCheckingState
from robot_brain_flexbe_states.check_what_to_stay_State import AgeGenderCheckSpeechState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 26 2019
@author: gal
'''
class readageandgendreSM(Behavior):
	'''
	read age and gendre
	'''


	def __init__(self):
		super(readageandgendreSM, self).__init__()
		self.name = 'read age and gendre'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:518 y:618, x:130 y:365
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:77 y:44
			OperatableStateMachine.add('1',
										LaunchVideoStream(),
										transitions={'continue': '2', 'failed': '5'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:280 y:40
			OperatableStateMachine.add('2',
										FaceDetTrack(),
										transitions={'continue': '3', 'failed': '6'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:482 y:25
			OperatableStateMachine.add('3',
										WaitState(wait_time=5),
										transitions={'done': 'sub to age and gendre'},
										autonomy={'done': Autonomy.Off})

			# x:647 y:100
			OperatableStateMachine.add('sub to age and gendre',
										SubscriberState(topic='/ros_openvino_toolkit/age_genders_Recognition', blocking=True, clear=False),
										transitions={'received': '7', 'unavailable': '6'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:283 y:347
			OperatableStateMachine.add('5',
										StopCameraStream(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:493 y:401
			OperatableStateMachine.add('6',
										StopFaceDetectAndTrack(),
										transitions={'continue': '5', 'failed': '5'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:820 y:229
			OperatableStateMachine.add('7',
										AgeGenderCheckingState(),
										transitions={'found': 'what to say', 'not_found': 'what to say'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message', 'age': 'age', 'gender': 'gender'})

			# x:780 y:427
			OperatableStateMachine.add('what to say',
										AgeGenderCheckSpeechState(),
										transitions={'found': '6', 'not_found': '6'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'age': 'age', 'gender': 'gender'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
