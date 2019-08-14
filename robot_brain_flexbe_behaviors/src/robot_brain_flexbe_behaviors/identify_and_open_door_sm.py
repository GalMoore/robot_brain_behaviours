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
from robot_brain_flexbe_states.listening_state import ListeningState
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.check_condition_state import CheckConditionState
from robot_brain_flexbe_states.word_check_state import WordCheckingState
from robot_brain_flexbe_states.talk_state import TalkState
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

		# O 870 377 
		# word check checks for the word "identification"



	def create(self):
		# x:30 y:344, x:202 y:205
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:53 y:52
			OperatableStateMachine.add('launch vid',
										LaunchVideoStream(vid_input_num=1),
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
										transitions={'continue': '4', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:746 y:16
			OperatableStateMachine.add('4',
										WaitState(wait_time=2),
										transitions={'done': 'how help'},
										autonomy={'done': Autonomy.Off})

			# x:679 y:650
			OperatableStateMachine.add('8',
										WaitState(wait_time=1),
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

			# x:825 y:624
			OperatableStateMachine.add('identify',
										IdentifyState(),
										transitions={'continue': 'hat', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:965 y:121
			OperatableStateMachine.add('listen',
										ListeningState(),
										transitions={'continue': 'wait1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1204 y:117
			OperatableStateMachine.add('wait1',
										WaitState(wait_time=1),
										transitions={'done': 'sub'},
										autonomy={'done': Autonomy.Off})

			# x:1128 y:229
			OperatableStateMachine.add('sub',
										SubscriberState(topic='/is_robot_listening', blocking=True, clear=False),
										transitions={'received': 'chk', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:1114 y:326
			OperatableStateMachine.add('chk',
										CheckConditionState(predicate=lambda message: message.data == "not listening"),
										transitions={'true': '2', 'false': 'sub'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:1123 y:501
			OperatableStateMachine.add('what was said',
										SubscriberState(topic="/stt_topic", blocking=True, clear=False),
										transitions={'received': '3', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message_said'})

			# x:1123 y:408
			OperatableStateMachine.add('2',
										WaitState(wait_time=2),
										transitions={'done': 'what was said'},
										autonomy={'done': Autonomy.Off})

			# x:872 y:409
			OperatableStateMachine.add('word chk',
										WordCheckingState(key_word="identification"),
										transitions={'found': 'commence', 'not_found': 'unknown cmd'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_said'})

			# x:1002 y:584
			OperatableStateMachine.add('3',
										WaitState(wait_time=2),
										transitions={'done': 'word chk'},
										autonomy={'done': Autonomy.Off})

			# x:953 y:15
			OperatableStateMachine.add('how help',
										TalkState(sentence_number=15),
										transitions={'continue': '6', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1180 y:10
			OperatableStateMachine.add('6',
										WaitState(wait_time=1),
										transitions={'done': 'listen'},
										autonomy={'done': Autonomy.Off})

			# x:673 y:283
			OperatableStateMachine.add('unknown cmd',
										TalkState(sentence_number=16),
										transitions={'continue': 'stopfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:775 y:520
			OperatableStateMachine.add('commence',
										TalkState(sentence_number=17),
										transitions={'continue': 'identify', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:538 y:604
			OperatableStateMachine.add('subnamestring',
										SubscriberState(topic='/identified_people_string_name', blocking=True, clear=False),
										transitions={'received': 'one', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message_name'})

			# x:390 y:632
			OperatableStateMachine.add('one',
										WaitState(wait_time=1),
										transitions={'done': 'chkstrng'},
										autonomy={'done': Autonomy.Off})

			# x:204 y:657
			OperatableStateMachine.add('chkstrng',
										WordCheckingStringState(key_word="Gal Moore"),
										transitions={'found': 'yes', 'not_found': 'no'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:11 y:649
			OperatableStateMachine.add('yes',
										TalkState(sentence_number=18),
										transitions={'continue': 'stopfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:304 y:516
			OperatableStateMachine.add('no',
										TalkState(sentence_number=19),
										transitions={'continue': 'stopfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:578 y:486
			OperatableStateMachine.add('hat',
										TalkState(sentence_number=20),
										transitions={'continue': '8', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
