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
from robot_brain_flexbe_states.launch_face_server import LaunchFaceServer
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.launch_obj_detect_and_track import LaunchObjDetectAndTrack
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.stop_face_server import StopFaceServer
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Aug 09 2019
@author: Gal Moore
'''
class check_new_face_ServerSM(Behavior):
	'''
	new face server
	'''


	def __init__(self):
		super(check_new_face_ServerSM, self).__init__()
		self.name = 'check_new_face_Server'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:526 y:310
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:91 y:42
			OperatableStateMachine.add('video',
										LaunchVideoStream(),
										transitions={'continue': 'w', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:423 y:65
			OperatableStateMachine.add('motor_face server',
										LaunchFaceServer(),
										transitions={'continue': 'w2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:286 y:75
			OperatableStateMachine.add('w',
										WaitState(wait_time=5),
										transitions={'done': 'motor_face server'},
										autonomy={'done': Autonomy.Off})

			# x:590 y:183
			OperatableStateMachine.add('w2',
										WaitState(wait_time=5),
										transitions={'done': 'objtrk'},
										autonomy={'done': Autonomy.Off})

			# x:767 y:180
			OperatableStateMachine.add('objtrk',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'w4', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:805 y:282
			OperatableStateMachine.add('w4',
										WaitState(wait_time=20),
										transitions={'done': 'stop objtrk'},
										autonomy={'done': Autonomy.Off})

			# x:753 y:378
			OperatableStateMachine.add('stop objtrk',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'start face trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:527 y:396
			OperatableStateMachine.add('start face trk',
										FaceDetTrack(),
										transitions={'continue': 'w6', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:215 y:426
			OperatableStateMachine.add('stop face',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'stop face server', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:418 y:496
			OperatableStateMachine.add('w6',
										WaitState(wait_time=20),
										transitions={'done': 'stop face'},
										autonomy={'done': Autonomy.Off})

			# x:173 y:264
			OperatableStateMachine.add('stop face server',
										StopFaceServer(),
										transitions={'continue': 'w', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
