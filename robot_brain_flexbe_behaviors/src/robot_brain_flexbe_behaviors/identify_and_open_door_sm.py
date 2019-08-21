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
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.stop_face_server import StopFaceServer
from robot_brain_flexbe_states.stop_camera_stream import StopCameraStream
from robot_brain_flexbe_states.identify_state import IdentifyState
from robot_brain_flexbe_states.talk_state import TalkState
from flexbe_states.subscriber_state import SubscriberState
from robot_brain_flexbe_states.check_simple_string import WordCheckingStringState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Aug 14 2019
@author: Gal Moore
'''
class Identify_and_open_doorSM(Behavior):
	'''
	open day through face recognition
	'''


	def __init__(self):
		super(Identify_and_open_doorSM, self).__init__()
		self.name = 'Identify_and_open_door'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:344, x:202 y:205
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:53 y:52
			OperatableStateMachine.add('launch vid',
										LaunchVideoStream(vid_input_num=0),
										transitions={'continue': 'launch faceserv', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:305 y:35
			OperatableStateMachine.add('launch faceserv',
										LaunchFaceServer(),
										transitions={'continue': 'facetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:508 y:38
			OperatableStateMachine.add('facetrk',
										FaceDetTrack(),
										transitions={'continue': 'commence', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1085 y:460
			OperatableStateMachine.add('8',
										WaitState(wait_time=6),
										transitions={'done': 'subnamestring'},
										autonomy={'done': Autonomy.Off})

			# x:124 y:526
			OperatableStateMachine.add('stopfacetrk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'stopfacesrv', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:125 y:422
			OperatableStateMachine.add('stopfacesrv',
										StopFaceServer(),
										transitions={'continue': 'stopvid', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:134 y:283
			OperatableStateMachine.add('stopvid',
										StopCameraStream(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1041 y:215
			OperatableStateMachine.add('identify',
										IdentifyState(),
										transitions={'continue': 'hat', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:837 y:91
			OperatableStateMachine.add('commence',
										TalkState(sentence_number=17),
										transitions={'continue': 'identify', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:916 y:471
			OperatableStateMachine.add('subnamestring',
										SubscriberState(topic='/identified_people_string_name', blocking=True, clear=False),
										transitions={'received': 'one', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message_name'})

			# x:766 y:474
			OperatableStateMachine.add('one',
										WaitState(wait_time=1),
										transitions={'done': 'chkstrng'},
										autonomy={'done': Autonomy.Off})

			# x:577 y:490
			OperatableStateMachine.add('chkstrng',
										WordCheckingStringState(key_word="Gal Moore"),
										transitions={'found': 'yes', 'not_found': 'no'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:381 y:586
			OperatableStateMachine.add('yes',
										TalkState(sentence_number=18),
										transitions={'continue': 'stopfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:404 y:396
			OperatableStateMachine.add('no',
										TalkState(sentence_number=19),
										transitions={'continue': 'stopfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1055 y:323
			OperatableStateMachine.add('hat',
										TalkState(sentence_number=20),
										transitions={'continue': '8', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
