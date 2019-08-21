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
from robot_brain_flexbe_states.talk_state import TalkState
from robot_brain_flexbe_states.launch_obj_detect_and_track import LaunchObjDetectAndTrack
from flexbe_states.check_condition_state import CheckConditionState
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from flexbe_states.subscriber_state import SubscriberState
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from robot_brain_flexbe_states.facial_expression_state import FacialExpressionState
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.listening_state import ListeningState
from robot_brain_flexbe_states.word_check_state import WordCheckingState
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.sound_calibration_state import SoundCalibState
from robot_brain_flexbe_states.gender_check_state import AgeGenderCheckingState
from robot_brain_flexbe_states.check_what_to_stay_State import AgeGenderCheckSpeechState
from robot_brain_flexbe_states.identify_state import IdentifyState
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.check_simple_string import WordCheckingStringState
from robot_brain_flexbe_states.stop_identify import StopIdentifyState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Aug 15 2019
@author: Gal Moore
'''
class toilabinteractionSM(Behavior):
	'''
	full toilab interaction August 2019
	'''


	def __init__(self):
		super(toilabinteractionSM, self).__init__()
		self.name = 'toilab interaction'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:174 y:518, x:535 y:33
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:408, x:370 y:201
		_sm_what_do_next_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_what_do_next_0:
			# x:30 y:40
			OperatableStateMachine.add('t29',
										TalkState(sentence_number=29),
										transitions={'continue': 't30', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:30 y:132
			OperatableStateMachine.add('t30',
										TalkState(sentence_number=30),
										transitions={'continue': '31', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:30 y:224
			OperatableStateMachine.add('31',
										TalkState(sentence_number=31),
										transitions={'continue': '32', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:30 y:316
			OperatableStateMachine.add('32',
										TalkState(sentence_number=32),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:256 y:317, x:458 y:279
		_sm_interaction_1 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_interaction_1:
			# x:166 y:76
			OperatableStateMachine.add('start face det trk',
										FaceDetTrack(),
										transitions={'continue': 't17', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:382 y:59
			OperatableStateMachine.add('t17',
										TalkState(sentence_number=17),
										transitions={'continue': 'identify', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:567 y:60
			OperatableStateMachine.add('identify',
										IdentifyState(),
										transitions={'continue': 't20', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:796 y:59
			OperatableStateMachine.add('t20',
										TalkState(sentence_number=20),
										transitions={'continue': 'w6', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1019 y:66
			OperatableStateMachine.add('w6',
										WaitState(wait_time=6),
										transitions={'done': 'subbb'},
										autonomy={'done': Autonomy.Off})

			# x:606 y:165
			OperatableStateMachine.add('subbb',
										SubscriberState(topic='/identified_people_string_name', blocking=True, clear=False),
										transitions={'received': 'w1', 'unavailable': 'log no sub'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message_name'})

			# x:811 y:167
			OperatableStateMachine.add('w1',
										WaitState(wait_time=1),
										transitions={'done': 'cchker'},
										autonomy={'done': Autonomy.Off})

			# x:940 y:173
			OperatableStateMachine.add('cchker',
										WordCheckingStringState(key_word="Gal Moore"),
										transitions={'found': 'f18', 'not_found': '19'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:784 y:365
			OperatableStateMachine.add('f18',
										TalkState(sentence_number=18),
										transitions={'continue': 'stpfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1020 y:362
			OperatableStateMachine.add('19',
										TalkState(sentence_number=19),
										transitions={'continue': 'stpfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:509 y:504
			OperatableStateMachine.add('stpfacetrk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'stop identify', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:608 y:272
			OperatableStateMachine.add('log no sub',
										LogState(text="no available lkog log", severity=Logger.REPORT_HINT),
										transitions={'done': 'subbb'},
										autonomy={'done': Autonomy.Off})

			# x:270 y:471
			OperatableStateMachine.add('stop identify',
										StopIdentifyState(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:30 y:365, x:172 y:294
		_sm_game_2 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_game_2:
			# x:40 y:41
			OperatableStateMachine.add('face trk',
										FaceDetTrack(),
										transitions={'continue': 't36', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:240 y:43
			OperatableStateMachine.add('t37',
										TalkState(sentence_number=37),
										transitions={'continue': 't38', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:460 y:41
			OperatableStateMachine.add('t38',
										TalkState(sentence_number=38),
										transitions={'continue': 'sub vino age gendre', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:699 y:70
			OperatableStateMachine.add('sub vino age gendre',
										SubscriberState(topic='/ros_openvino_toolkit/age_genders_Recognition', blocking=True, clear=False),
										transitions={'received': 'agegendchek', 'unavailable': 'log'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:626 y:228
			OperatableStateMachine.add('agegendchek',
										AgeGenderCheckingState(),
										transitions={'found': 'chkspch', 'not_found': 'chkspch'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message', 'age': 'age', 'gender': 'gender'})

			# x:672 y:384
			OperatableStateMachine.add('chkspch',
										AgeGenderCheckSpeechState(),
										transitions={'found': 'stopface trk', 'not_found': 'stopface trk'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'age': 'age', 'gender': 'gender'})

			# x:58 y:174
			OperatableStateMachine.add('t36',
										TalkState(sentence_number=36),
										transitions={'continue': 't37', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:392 y:462
			OperatableStateMachine.add('stopface trk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:870 y:59
			OperatableStateMachine.add('log',
										LogState(text="log", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub vino age gendre'},
										autonomy={'done': Autonomy.Off})


		# x:30 y:365, x:130 y:365
		_sm_do_nothing_3 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_do_nothing_3:
			# x:118 y:83
			OperatableStateMachine.add('stopdettrkface',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'tlk33', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:570 y:190
			OperatableStateMachine.add('tlk33',
										TalkState(sentence_number=33),
										transitions={'continue': '34', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:408 y:283
			OperatableStateMachine.add('34',
										TalkState(sentence_number=34),
										transitions={'continue': '35', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:418 y:455
			OperatableStateMachine.add('35',
										TalkState(sentence_number=35),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:1214 y:584, x:130 y:368, x:849 y:566, x:938 y:579, x:602 y:556
		_sm_user_input_speech_4 = OperatableStateMachine(outcomes=['finished', 'failed', 'identification', 'game', 'nothing'])

		with _sm_user_input_speech_4:
			# x:71 y:57
			OperatableStateMachine.add('stopfacedettrk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'calib', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:453 y:35
			OperatableStateMachine.add('sub for vol',
										SubscriberState(topic='/avg_ambience_vol', blocking=True, clear=False),
										transitions={'received': 'listen1', 'unavailable': 'log'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'vol'})

			# x:638 y:51
			OperatableStateMachine.add('listen1',
										ListeningState(),
										transitions={'continue': 'sub_stt', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'vol'})

			# x:897 y:126
			OperatableStateMachine.add('sub_stt',
										SubscriberState(topic='/stt_topic', blocking=True, clear=False),
										transitions={'received': 'word chk "do nothing"', 'unavailable': 'logg'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'message'})

			# x:666 y:184
			OperatableStateMachine.add('word chk "do nothing"',
										WordCheckingState(key_word="nothing"),
										transitions={'found': 'nothing', 'not_found': 'wrd chk "identification"'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:802 y:282
			OperatableStateMachine.add('wrd chk "identification"',
										WordCheckingState(key_word="identification"),
										transitions={'found': 'identification', 'not_found': 'wrd chk "game"'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:1015 y:316
			OperatableStateMachine.add('wrd chk "game"',
										WordCheckingState(key_word="game"),
										transitions={'found': 'game', 'not_found': '39'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:319 y:140
			OperatableStateMachine.add('log',
										LogState(text="log", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub for vol'},
										autonomy={'done': Autonomy.Off})

			# x:1085 y:120
			OperatableStateMachine.add('logg',
										LogState(text="logging", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub_stt'},
										autonomy={'done': Autonomy.Off})

			# x:138 y:152
			OperatableStateMachine.add('calib',
										SoundCalibState(length_of_calibration=20),
										transitions={'continue': 'sub for vol', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1123 y:431
			OperatableStateMachine.add('39',
										TalkState(sentence_number=39),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:195 y:308, x:402 y:431
		_sm_face_det_and_start_interaction_ask_user_what_next_5 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_face_det_and_start_interaction_ask_user_what_next_5:
			# x:64 y:61
			OperatableStateMachine.add('face det trk',
										FaceDetTrack(),
										transitions={'continue': 'tlk3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:814 y:163
			OperatableStateMachine.add('tlk2',
										TalkState(sentence_number=2),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:312 y:35
			OperatableStateMachine.add('tlk3',
										TalkState(sentence_number=27),
										transitions={'continue': 'talk4', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:543 y:43
			OperatableStateMachine.add('talk4',
										TalkState(sentence_number=28),
										transitions={'continue': 'graucho', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:797 y:64
			OperatableStateMachine.add('graucho',
										FacialExpressionState(expression_num=3),
										transitions={'continue': 'welcome', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:555 y:165
			OperatableStateMachine.add('welcome',
										TalkState(sentence_number=1),
										transitions={'continue': 'tlk2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:30 y:338, x:339 y:254
		_sm_object_detection_till_face_nearby_6 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_object_detection_till_face_nearby_6:
			# x:167 y:58
			OperatableStateMachine.add('obj det trk',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'strtdobj', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:661 y:188
			OperatableStateMachine.add('chk person',
										CheckConditionState(predicate=lambda person_message: person_message.data == "yes"),
										transitions={'true': 'found face ', 'false': 'sub person'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'person_message'})

			# x:308 y:364
			OperatableStateMachine.add('stop obj trk',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:495 y:37
			OperatableStateMachine.add('strtdobj',
										TalkState(sentence_number=25),
										transitions={'continue': 'sub person', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:697 y:303
			OperatableStateMachine.add('found face ',
										TalkState(sentence_number=24),
										transitions={'continue': 'stop obj trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:775 y:45
			OperatableStateMachine.add('sub person',
										SubscriberState(topic='/is_person_nearby', blocking=True, clear=False),
										transitions={'received': 'chk person', 'unavailable': 'chk person'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'person_message'})


		# x:370 y:484, x:130 y:365
		_sm_startup_vid_motors_srvr_7 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_startup_vid_motors_srvr_7:
			# x:112 y:64
			OperatableStateMachine.add('video stream',
										LaunchVideoStream(vid_input_num=1),
										transitions={'continue': 'face motor server', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:337 y:45
			OperatableStateMachine.add('face motor server',
										LaunchFaceServer(),
										transitions={'continue': '23', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:658 y:202
			OperatableStateMachine.add('23',
										TalkState(sentence_number=23),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})



		with _state_machine:
			# x:127 y:84
			OperatableStateMachine.add('startup vid motors srvr',
										_sm_startup_vid_motors_srvr_7,
										transitions={'finished': 'what do next', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:956 y:166
			OperatableStateMachine.add('object detection till face nearby',
										_sm_object_detection_till_face_nearby_6,
										transitions={'finished': 'face det and start interaction ask user what next', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:701 y:41
			OperatableStateMachine.add('face det and start interaction ask user what next',
										_sm_face_det_and_start_interaction_ask_user_what_next_5,
										transitions={'finished': 'what do next', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:359 y:340
			OperatableStateMachine.add('user input speech',
										_sm_user_input_speech_4,
										transitions={'finished': 'finished', 'failed': 'failed', 'identification': 'interaction', 'game': 'game', 'nothing': 'do_nothing'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'identification': Autonomy.Inherit, 'game': Autonomy.Inherit, 'nothing': Autonomy.Inherit})

			# x:711 y:223
			OperatableStateMachine.add('do_nothing',
										_sm_do_nothing_3,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:710 y:307
			OperatableStateMachine.add('game',
										_sm_game_2,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:698 y:393
			OperatableStateMachine.add('interaction',
										_sm_interaction_1,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:358 y:169
			OperatableStateMachine.add('what do next',
										_sm_what_do_next_0,
										transitions={'finished': 'user input speech', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
