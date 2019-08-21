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
from robot_brain_flexbe_states.launch_face_server import LaunchFaceServer
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.stop_camera_stream import StopCameraStream
from flexbe_states.subscriber_state import SubscriberState
from flexbe_states.check_condition_state import CheckConditionState
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.facial_expression_state import FacialExpressionState
from robot_brain_flexbe_states.listening_state import ListeningState
from robot_brain_flexbe_states.gender_check_state import AgeGenderCheckingState
from robot_brain_flexbe_states.check_what_to_stay_State import AgeGenderCheckSpeechState
from robot_brain_flexbe_states.sound_calibration_state import SoundCalibState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Sun May 26 2019
@author: Gal
'''
class CuriosityLabDemoSM(Behavior):
	'''
	demo of basic abilities for TAU Curiosity Lab
	'''


	def __init__(self):
		super(CuriosityLabDemoSM, self).__init__()
		self.name = 'Curiosity Lab Demo'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:154 y:236, x:130 y:410
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:77 y:297, x:130 y:392
		_sm_got_permission_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_got_permission_0:
			# x:100 y:65
			OperatableStateMachine.add('go ahead',
										TalkState(sentence_number=3),
										transitions={'continue': 'wait till robot  finish talking', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:519 y:139
			OperatableStateMachine.add('smile',
										FacialExpressionState(expression_num=1),
										transitions={'continue': 'sub', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:368 y:43
			OperatableStateMachine.add('wait till robot  finish talking',
										WaitState(wait_time=5),
										transitions={'done': 'smile'},
										autonomy={'done': Autonomy.Off})

			# x:819 y:114
			OperatableStateMachine.add('sub',
										SubscriberState(topic='/ros_openvino_toolkit/age_genders_Recognition', blocking=True, clear=False),
										transitions={'received': 'check age gender', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:901 y:198
			OperatableStateMachine.add('check age gender',
										AgeGenderCheckingState(),
										transitions={'found': 'check what to say', 'not_found': 'check what to say'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message', 'age': 'age', 'gender': 'gender'})

			# x:853 y:391
			OperatableStateMachine.add('check what to say',
										AgeGenderCheckSpeechState(),
										transitions={'found': 'wait', 'not_found': 'wait'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'age': 'age', 'gender': 'gender'})

			# x:904 y:506
			OperatableStateMachine.add('wait',
										WaitState(wait_time=2),
										transitions={'done': 'was I right or'},
										autonomy={'done': Autonomy.Off})

			# x:715 y:514
			OperatableStateMachine.add('was I right or',
										TalkState(sentence_number=14),
										transitions={'continue': 'graucho', 'failed': 'graucho'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:518 y:611
			OperatableStateMachine.add('graucho',
										FacialExpressionState(expression_num=3),
										transitions={'continue': 'good bye', 'failed': 'good bye'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:475 y:465
			OperatableStateMachine.add('good bye',
										TalkState(sentence_number=12),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:343 y:584, x:501 y:192
		_sm_guess_age_interaction_1 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_guess_age_interaction_1:
			# x:27 y:84
			OperatableStateMachine.add('smile',
										FacialExpressionState(expression_num=1),
										transitions={'continue': 'wait2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:210 y:70
			OperatableStateMachine.add('wait2',
										WaitState(wait_time=2),
										transitions={'done': 'blink'},
										autonomy={'done': Autonomy.Off})

			# x:329 y:43
			OperatableStateMachine.add('blink',
										FacialExpressionState(expression_num=2),
										transitions={'continue': 'welcome whats your name', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:498 y:19
			OperatableStateMachine.add('welcome whats your name',
										TalkState(sentence_number=1),
										transitions={'continue': 'calib1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1089 y:151
			OperatableStateMachine.add('welcome',
										TalkState(sentence_number=2),
										transitions={'continue': 'wait till finished talking', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1035 y:254
			OperatableStateMachine.add('user input please take photo',
										ListeningState(),
										transitions={'continue': 'wait 1 second', 'failed': 'wait 1 second'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:1286 y:154
			OperatableStateMachine.add('wait till finished talking',
										WaitState(wait_time=1),
										transitions={'done': 'user input please take photo'},
										autonomy={'done': Autonomy.Off})

			# x:958 y:424
			OperatableStateMachine.add('wait 1 second',
										WaitState(wait_time=1),
										transitions={'done': 'SUBTORESPONSE'},
										autonomy={'done': Autonomy.Off})

			# x:1053 y:586
			OperatableStateMachine.add('got permission',
										_sm_got_permission_0,
										transitions={'finished': 'finished', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1153 y:431
			OperatableStateMachine.add('SUBTORESPONSE',
										SubscriberState(topic='/is_robot_listening', blocking=True, clear=False),
										transitions={'received': 'CHKCOND', 'unavailable': 'CHKCOND'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:1365 y:430
			OperatableStateMachine.add('CHKCOND',
										CheckConditionState(predicate=lambda message: message.data == "not listening"),
										transitions={'true': 'log', 'false': 'SUBTORESPONSE'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:1351 y:558
			OperatableStateMachine.add('log',
										LogState(text="got input from user", severity=Logger.REPORT_HINT),
										transitions={'done': 'got permission'},
										autonomy={'done': Autonomy.Off})

			# x:1095 y:14
			OperatableStateMachine.add('listenuserinput',
										ListeningState(),
										transitions={'continue': 'waitwait', 'failed': 'waitwait'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:1296 y:12
			OperatableStateMachine.add('waitwait',
										WaitState(wait_time=1),
										transitions={'done': 'substate'},
										autonomy={'done': Autonomy.Off})

			# x:1401 y:16
			OperatableStateMachine.add('substate',
										SubscriberState(topic='/is_robot_listening', blocking=True, clear=False),
										transitions={'received': 'chekcont', 'unavailable': 'chekcont'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message_listen'})

			# x:839 y:94
			OperatableStateMachine.add('chekcont',
										CheckConditionState(predicate=lambda message: message.data == "not listening"),
										transitions={'true': 'welcome', 'false': 'substate'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message_listen'})

			# x:716 y:13
			OperatableStateMachine.add('calib1',
										SoundCalibState(length_of_calibration=60),
										transitions={'continue': 'sub5', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:921 y:13
			OperatableStateMachine.add('sub5',
										SubscriberState(topic='/avg_ambience_vol', blocking=True, clear=False),
										transitions={'received': 'listenuserinput', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})


		# x:555 y:314, x:343 y:251
		_sm_start_face__2 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_start_face__2:
			# x:90 y:59
			OperatableStateMachine.add('say face found',
										TalkState(sentence_number=100),
										transitions={'continue': 'start face', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:391 y:73
			OperatableStateMachine.add('start face',
										FaceDetTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:582 y:410, x:130 y:365
		_sm_check_face_nearby_3 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_check_face_nearby_3:
			# x:335 y:73
			OperatableStateMachine.add('sub face nearby',
										SubscriberState(topic='/is_person_nearby', blocking=True, clear=False),
										transitions={'received': 'face condition', 'unavailable': 'failed'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:517 y:113
			OperatableStateMachine.add('face condition',
										CheckConditionState(predicate=lambda message: message.data == "yes"),
										transitions={'true': 'finished', 'false': 'log'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:367 y:223
			OperatableStateMachine.add('log',
										LogState(text="no face yet", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub face nearby'},
										autonomy={'done': Autonomy.Off})


		# x:159 y:294, x:262 y:532
		_sm_stop_video_detects_and_tracks_4 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_stop_video_detects_and_tracks_4:
			# x:347 y:146
			OperatableStateMachine.add('stop obj',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'stop face', 'failed': 'stop face'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:621 y:167
			OperatableStateMachine.add('stop face',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'stop video', 'failed': 'stop video'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:439 y:323
			OperatableStateMachine.add('stop video',
										StopCameraStream(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:375 y:332, x:227 y:202
		_sm_launch_video_stream_and_object_detector_5 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_launch_video_stream_and_object_detector_5:
			# x:120 y:76
			OperatableStateMachine.add('video stream',
										LaunchVideoStream(vid_input_num=1),
										transitions={'continue': 'say launch obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:405 y:63
			OperatableStateMachine.add('say launch obj',
										TalkState(sentence_number=99),
										transitions={'continue': 'launch obj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:647 y:168
			OperatableStateMachine.add('launch obj',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'launch face server', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:649 y:298
			OperatableStateMachine.add('launch face server',
										LaunchFaceServer(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})



		with _state_machine:
			# x:46 y:63
			OperatableStateMachine.add('launch video stream and object detector',
										_sm_launch_video_stream_and_object_detector_5,
										transitions={'finished': 'wait5', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:372 y:534
			OperatableStateMachine.add('stop video detects and tracks',
										_sm_stop_video_detects_and_tracks_4,
										transitions={'finished': 'launch video stream and object detector', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:540 y:64
			OperatableStateMachine.add('check face nearby',
										_sm_check_face_nearby_3,
										transitions={'finished': 'stop obj', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:815 y:53
			OperatableStateMachine.add('stop obj',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'start face ', 'failed': 'stop video detects and tracks'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:906 y:199
			OperatableStateMachine.add('start face ',
										_sm_start_face__2,
										transitions={'finished': 'wait3', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:390 y:36
			OperatableStateMachine.add('wait5',
										WaitState(wait_time=5),
										transitions={'done': 'check face nearby'},
										autonomy={'done': Autonomy.Off})

			# x:954 y:322
			OperatableStateMachine.add('wait3',
										WaitState(wait_time=2),
										transitions={'done': 'guess age interaction'},
										autonomy={'done': Autonomy.Off})

			# x:878 y:457
			OperatableStateMachine.add('guess age interaction',
										_sm_guess_age_interaction_1,
										transitions={'finished': 'stop video detects and tracks', 'failed': 'stop video detects and tracks'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
