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
from robot_brain_flexbe_states.launch_obj_detect_and_track import LaunchObjDetectAndTrack
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from robot_brain_flexbe_states.launch_face_server import LaunchFaceServer
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Aug 08 2019
@author: Gal Moore
'''
class TRACKING_DEBUGSM(Behavior):
	'''
	perfect tracking for object and face
	'''


	def __init__(self):
		super(TRACKING_DEBUGSM, self).__init__()
		self.name = 'TRACKING_DEBUG'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:233 y:490, x:599 y:231
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:95 y:72
			OperatableStateMachine.add('launch video stream',
										LaunchVideoStream(),
										transitions={'continue': 'launch face serer', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:628 y:85
			OperatableStateMachine.add('launch obj det trk',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'wait 60sec', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:706 y:444
			OperatableStateMachine.add('stop obj trk',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'start fac e trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:493 y:530
			OperatableStateMachine.add('wait60 sec',
										WaitState(wait_time=60),
										transitions={'done': 'stop face det trk'},
										autonomy={'done': Autonomy.Off})

			# x:324 y:390
			OperatableStateMachine.add('stop face det trk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'launch obj det trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:805 y:258
			OperatableStateMachine.add('wait 60sec',
										WaitState(wait_time=60),
										transitions={'done': 'stop obj trk'},
										autonomy={'done': Autonomy.Off})

			# x:726 y:557
			OperatableStateMachine.add('start fac e trk',
										FaceDetTrack(),
										transitions={'continue': 'wait60 sec', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:347 y:52
			OperatableStateMachine.add('launch face serer',
										LaunchFaceServer(),
										transitions={'continue': 'launch obj det trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
