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
from robot_brain_flexbe_states.launch_obj_detect_and_track import LaunchObjDetectAndTrack
from robot_brain_flexbe_states.stop_camera_stream import StopObjectDetectAndTrack as robot_brain_flexbe_states__StopObjectDetectAndTrack
from robot_brain_flexbe_states.launch_video_stream_state import LaunchVideoStream
from robot_brain_flexbe_states.stop_camera_stream import StopCameraStream
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 22 2019
@author: Gal Moore
'''
class objectandpeopletrackingSM(Behavior):
	'''
	detect and track people (object) than detect and track faces.
	'''


	def __init__(self):
		super(objectandpeopletrackingSM, self).__init__()
		self.name = 'object and people tracking'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:949 y:748, x:437 y:452
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:192 y:105
			OperatableStateMachine.add('wait a sec',
										WaitState(wait_time=3),
										transitions={'done': 'start_video_stream_State'},
										autonomy={'done': Autonomy.Off})

			# x:835 y:33
			OperatableStateMachine.add('wait number TWO',
										WaitState(wait_time=10),
										transitions={'done': 'stop detect and track'},
										autonomy={'done': Autonomy.Off})

			# x:633 y:37
			OperatableStateMachine.add('start detect and track',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'wait number TWO', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:821 y:142
			OperatableStateMachine.add('stop detect and track',
										robot_brain_flexbe_states__StopObjectDetectAndTrack(),
										transitions={'continue': 'stop video stream', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:415 y:39
			OperatableStateMachine.add('start_video_stream_State',
										LaunchVideoStream(),
										transitions={'continue': 'start detect and track', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:822 y:253
			OperatableStateMachine.add('stop video stream',
										StopCameraStream(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
