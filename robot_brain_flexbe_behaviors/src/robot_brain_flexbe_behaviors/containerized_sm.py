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
from robot_brain_flexbe_states.talk_state import TalkState
from robot_brain_flexbe_states.launch_obj_detect_and_track import LaunchObjDetectAndTrack
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.check_condition_state import CheckConditionState
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.stop_camera_stream import StopCameraStream
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from robot_brain_flexbe_states.facial_expression_state import FacialExpressionState
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.listening_state import ListeningState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 26 2019
@author: Gal
'''
class containerizedSM(Behavior):
	'''
	full inteaction in containers
	'''


	def __init__(self):
		super(containerizedSM, self).__init__()
		self.name = 'containerized'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:456 y:478, x:347 y:237
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:365, x:487 y:245
		_sm_guess_age_interaction_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_guess_age_interaction_0:
			# x:153 y:68
			OperatableStateMachine.add('smile',
										FacialExpressionState(expression_num=1),
										transitions={'continue': 'wait 1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:378 y:48
			OperatableStateMachine.add('wait 1',
										WaitState(wait_time=1),
										transitions={'done': 'blink'},
										autonomy={'done': Autonomy.Off})

			# x:605 y:69
			OperatableStateMachine.add('blink',
										FacialExpressionState(expression_num=2),
										transitions={'continue': 'introduction', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:817 y:120
			OperatableStateMachine.add('introduction',
										TalkState(sentence_number=1),
										transitions={'continue': 'listen for name', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:919 y:202
			OperatableStateMachine.add('listen for name',
										ListeningState(),
										transitions={'continue': 'welcome to', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1004 y:291
			OperatableStateMachine.add('welcome to',
										TalkState(sentence_number=2),
										transitions={'continue': 'sub please take my photo', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1027 y:401
			OperatableStateMachine.add('sub please take my photo',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'cond please take my photo', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:1025 y:515
			OperatableStateMachine.add('cond please take my photo',
										CheckConditionState(predicate=lambda message:message.data =="please take my photo"),
										transitions={'true': 'cool go ahead', 'false': 'not heard take photo'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:823 y:458
			OperatableStateMachine.add('not heard take photo',
										LogState(text=not yet heard "please take my photo", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub please take my photo'},
										autonomy={'done': Autonomy.Off})

			# x:938 y:641
			OperatableStateMachine.add('cool go ahead',
										TalkState(sentence_number=3),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:161 y:371, x:268 y:170
		_sm_start_face_det_and_trk_1 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_start_face_det_and_trk_1:
			# x:149 y:36
			OperatableStateMachine.add('say face found',
										TalkState(sentence_number=100),
										transitions={'continue': 'face det trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:519 y:73
			OperatableStateMachine.add('face det trk',
										FaceDetTrack(),
										transitions={'continue': 'say start face det trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:563 y:328
			OperatableStateMachine.add('say start face det trk',
										TalkState(sentence_number=101),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:128 y:223, x:130 y:365
		_sm_stop_video_detects_and_tracks_2 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_stop_video_detects_and_tracks_2:
			# x:135 y:64
			OperatableStateMachine.add('stop obj det trk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'stop face det  trk', 'failed': 'stop face det  trk'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:410 y:78
			OperatableStateMachine.add('stop face det  trk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'stop video stream', 'failed': 'stop video stream'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:466 y:250
			OperatableStateMachine.add('stop video stream',
										StopCameraStream(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:438 y:355, x:121 y:296
		_sm_check_face_nearby_3 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_check_face_nearby_3:
			# x:237 y:77
			OperatableStateMachine.add('subscr face found topic',
										SubscriberState(topic='/is_person_nearby', blocking=True, clear=False),
										transitions={'received': 'face condition', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:521 y:63
			OperatableStateMachine.add('face condition',
										CheckConditionState(predicate=lambda message:message.data == "yes"),
										transitions={'true': 'finished', 'false': 'no face found yet'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:297 y:218
			OperatableStateMachine.add('no face found yet',
										LogState(text="no face found yet", severity=Logger.REPORT_HINT),
										transitions={'done': 'subscr face found topic'},
										autonomy={'done': Autonomy.Off})


		# x:30 y:365, x:132 y:205
		_sm_launch_stream_and_object_detector_4 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_launch_stream_and_object_detector_4:
			# x:126 y:42
			OperatableStateMachine.add('launch video stream',
										LaunchVideoStream(),
										transitions={'continue': 'say launching video', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:389 y:56
			OperatableStateMachine.add('say launching video',
										TalkState(sentence_number=99),
										transitions={'continue': 'launch obj det trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:483 y:152
			OperatableStateMachine.add('launch obj det trk',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})



		with _state_machine:
			# x:135 y:38
			OperatableStateMachine.add('launch stream and object detector',
										_sm_launch_stream_and_object_detector_4,
										transitions={'finished': 'check face nearby', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:469 y:33
			OperatableStateMachine.add('check face nearby',
										_sm_check_face_nearby_3,
										transitions={'finished': 'stop obj det trk', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:546 y:220
			OperatableStateMachine.add('stop video detects and tracks',
										_sm_stop_video_detects_and_tracks_2,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:701 y:69
			OperatableStateMachine.add('stop obj det trk',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'start face det and trk', 'failed': 'stop video detects and tracks'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:892 y:135
			OperatableStateMachine.add('start face det and trk',
										_sm_start_face_det_and_trk_1,
										transitions={'finished': 'guess age interaction', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:887 y:356
			OperatableStateMachine.add('guess age interaction',
										_sm_guess_age_interaction_0,
										transitions={'finished': 'finished', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
