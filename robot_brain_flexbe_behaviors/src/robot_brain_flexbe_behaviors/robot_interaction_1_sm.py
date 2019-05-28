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
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.check_condition_state import CheckConditionState
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.talk_state import TalkState
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.listening_state import ListeningState
from robot_brain_flexbe_states.facial_expression_state import FacialExpressionState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Fri May 24 2019
@author: G
'''
class robot_interaction_1SM(Behavior):
	'''
	interaction with start video, start obj detect, start track, and close all.
	'''


	def __init__(self):
		super(robot_interaction_1SM, self).__init__()
		self.name = 'robot_interaction_1'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:284 y:484, x:47 y:223
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:454, x:130 y:454
		_sm_take_photo_container_(guess_age)_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_take_photo_container_(guess_age)_0:
			# x:124 y:43
			OperatableStateMachine.add('ok if you are ready show me a big smile',
										TalkState(sentence_number=3),
										transitions={'continue': 'smile', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:699 y:57
			OperatableStateMachine.add('wait as if take photo',
										WaitState(wait_time=3),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:481 y:41
			OperatableStateMachine.add('smile',
										FacialExpressionState(expression_num=1),
										transitions={'continue': 'wait as if take photo', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})



		with _state_machine:
			# x:109 y:52
			OperatableStateMachine.add('launch video',
										LaunchVideoStream(),
										transitions={'continue': 'starting object track talk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:514 y:19
			OperatableStateMachine.add('detect and track',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'subscriber_is_nearby_face_State', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:734 y:20
			OperatableStateMachine.add('subscriber_is_nearby_face_State',
										SubscriberState(topic='/is_person_nearby', blocking=True, clear=False),
										transitions={'received': 'check_if_nearby', 'unavailable': 'stop obj detect state'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:732 y:157
			OperatableStateMachine.add('check_if_nearby',
										CheckConditionState(predicate=lambda message:message.data == "yes"),
										transitions={'true': 'stop obj detect state', 'false': 'logger'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:588 y:115
			OperatableStateMachine.add('logger',
										LogState(text="false", severity=Logger.REPORT_HINT),
										transitions={'done': 'subscriber_is_nearby_face_State'},
										autonomy={'done': Autonomy.Off})

			# x:935 y:201
			OperatableStateMachine.add('stop obj detect state',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'face identified', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:960 y:281
			OperatableStateMachine.add('launch face detect and track',
										FaceDetTrack(),
										transitions={'continue': 'wait to show face trk', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1178 y:285
			OperatableStateMachine.add('wait to show face trk',
										WaitState(wait_time=5),
										transitions={'done': 'talk hello'},
										autonomy={'done': Autonomy.Off})

			# x:1165 y:361
			OperatableStateMachine.add('talk hello',
										TalkState(sentence_number=2),
										transitions={'continue': 'listen_for_input_state', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:342 y:308
			OperatableStateMachine.add('stop face detect',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:967 y:38
			OperatableStateMachine.add('face identified',
										TalkState(sentence_number=100),
										transitions={'continue': 'start face track', 'failed': 'stop obj detect state'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1171 y:33
			OperatableStateMachine.add('start face track',
										TalkState(sentence_number=101),
										transitions={'continue': 'launch face detect and track', 'failed': 'stop obj detect state'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:273 y:126
			OperatableStateMachine.add('starting object track talk',
										TalkState(sentence_number=99),
										transitions={'continue': 'detect and track', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1164 y:441
			OperatableStateMachine.add('listen_for_input_state',
										ListeningState(),
										transitions={'continue': 'subscribe to user input1', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1160 y:516
			OperatableStateMachine.add('subscribe to user input1',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'check user input1', 'unavailable': 'stop face detect'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message_stt'})

			# x:1180 y:590
			OperatableStateMachine.add('check user input1',
										CheckConditionState(predicate=lambda message: message.query =="please take my photo"),
										transitions={'true': 'yes take photo', 'false': 'no take photo not received'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message_stt'})

			# x:1005 y:585
			OperatableStateMachine.add('yes take photo',
										LogState(text="yes take photo recieved", severity=Logger.REPORT_HINT),
										transitions={'done': 'take photo container (guess age)'},
										autonomy={'done': Autonomy.Off})

			# x:1367 y:517
			OperatableStateMachine.add('no take photo not received',
										LogState(text="no not recieved take photo", severity=Logger.REPORT_HINT),
										transitions={'done': 'listen_for_input_state'},
										autonomy={'done': Autonomy.Off})

			# x:727 y:532
			OperatableStateMachine.add('take photo container (guess age)',
										_sm_take_photo_container_(guess_age)_0,
										transitions={'finished': 'left container', 'failed': 'stop face detect'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:585 y:606
			OperatableStateMachine.add('left container',
										LogState(text="left container - now back on main", severity=Logger.REPORT_HINT),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
