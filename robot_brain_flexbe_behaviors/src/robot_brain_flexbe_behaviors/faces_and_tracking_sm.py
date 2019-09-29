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
from robot_brain_flexbe_states.launch_face_server import LaunchFaceServer
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.facial_gestures_state import FacialGesturesState
from robot_brain_flexbe_states.kill_facial_gestures import KillFacialGesturesState
from robot_brain_flexbe_states.stop_face_server import StopFaceServer
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri Sep 20 2019
@author: gal
'''
class faces_and_trackingSM(Behavior):
	'''
	faces_and_Tracking
	'''


	def __init__(self):
		super(faces_and_trackingSM, self).__init__()
		self.name = 'faces_and_tracking'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:365, x:416 y:272
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:117 y:105
			OperatableStateMachine.add('launch vid',
										LaunchVideoStream(vid_input_num=0),
										transitions={'continue': 'facesrv', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:595 y:89
			OperatableStateMachine.add('onjtrk',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'facial_gestures', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:378 y:33
			OperatableStateMachine.add('facesrv',
										LaunchFaceServer(),
										transitions={'continue': 'onjtrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:746 y:432
			OperatableStateMachine.add('w1',
										WaitState(wait_time=20),
										transitions={'done': 'kill faces'},
										autonomy={'done': Autonomy.Off})

			# x:717 y:230
			OperatableStateMachine.add('facial_gestures',
										FacialGesturesState(),
										transitions={'continue': 'w1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:503 y:479
			OperatableStateMachine.add('kill faces',
										KillFacialGesturesState(),
										transitions={'continue': 'stop face serv', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:300 y:445
			OperatableStateMachine.add('stop face serv',
										StopFaceServer(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
