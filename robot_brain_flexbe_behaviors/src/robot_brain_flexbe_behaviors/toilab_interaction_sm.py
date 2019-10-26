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
from robot_brain_flexbe_states.launch_arduino_led import LaunchArduinoLed
from robot_brain_flexbe_states.talk_state import TalkState
from robot_brain_flexbe_states.launch_face_det_track_state import FaceDetTrack
from robot_brain_flexbe_states.facial_expression_state import FacialExpressionState
from robot_brain_flexbe_states.kill_facial_gestures import KillFacialGesturesState
from robot_brain_flexbe_states.facial_gestures_for_face_Det import FacialGesturesFaceDetState
from robot_brain_flexbe_states.sound_calibration_state import SoundCalibState
from robot_brain_flexbe_states.word_check_state import WordCheckingState
from robot_brain_flexbe_states.read_txt_and_msg_out import ReadTxtState
from robot_brain_flexbe_states.stop_face_detect_and_track import StopFaceDetectAndTrack
from robot_brain_flexbe_states.listening_state import ListeningState
from robot_brain_flexbe_states.decide_talk_state import DecideTalkState
from flexbe_states.subscriber_state import SubscriberState
from robot_brain_flexbe_states.gender_check_state import AgeGenderCheckingState
from robot_brain_flexbe_states.check_what_to_stay_State import AgeGenderCheckSpeechState
from flexbe_states.log_state import LogState
from robot_brain_flexbe_states.identify_state import IdentifyState
from flexbe_states.wait_state import WaitState
from robot_brain_flexbe_states.check_simple_string import WordCheckingStringState
from robot_brain_flexbe_states.stop_identify import StopIdentifyState
from flexbe_states.check_condition_state import CheckConditionState
from robot_brain_flexbe_states.stop_object_detect_and_track import StopObjectDetectAndTrack
from robot_brain_flexbe_states.facial_gestures_state import FacialGesturesState
from robot_brain_flexbe_states.launch_obj_detect_and_track import LaunchObjDetectAndTrack
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

		# O 637 168 /user input speech
		# this must be done at some point cause we arrive here often after obj tracking turned face trk



	def create(self):
		# x:174 y:518, x:535 y:33
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]

		# x:30 y:372, x:130 y:372
		_sm_joke_0 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_joke_0:
			# x:83 y:58
			OperatableStateMachine.add('startfacedettrk2',
										FaceDetTrack(),
										transitions={'continue': 'great', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:465 y:94
			OperatableStateMachine.add('44',
										TalkState(sentence_number=44),
										transitions={'continue': 'readcalib', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:696 y:130
			OperatableStateMachine.add('listenn',
										ListeningState(),
										transitions={'continue': 'readquery', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'calib_vol'})

			# x:695 y:30
			OperatableStateMachine.add('readcalib',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/volume_calib.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'listenn'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'calib_vol'})

			# x:708 y:235
			OperatableStateMachine.add('readquery',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/query.txt"),
										transitions={'unavailable': 'failed', 'got_message': '43'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'message'})

			# x:712 y:329
			OperatableStateMachine.add('43',
										TalkState(sentence_number=43),
										transitions={'continue': 'lllisten', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:713 y:433
			OperatableStateMachine.add('lllisten',
										ListeningState(),
										transitions={'continue': 'ttlk45', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'calib_vol'})

			# x:487 y:468
			OperatableStateMachine.add('ttlk45',
										TalkState(sentence_number=45),
										transitions={'continue': '46', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:275 y:461
			OperatableStateMachine.add('46',
										TalkState(sentence_number=46),
										transitions={'continue': 'stopffcedettrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:83 y:558
			OperatableStateMachine.add('stopffcedettrk',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:270 y:113
			OperatableStateMachine.add('great',
										TalkState(sentence_number=42),
										transitions={'continue': '44', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:372 y:465, x:183 y:214
		_sm_waking_up_1 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_waking_up_1:
			# x:181 y:75
			OperatableStateMachine.add('facial gestures eyes mouth only',
										FacialGesturesState(),
										transitions={'continue': 'decide_talk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:612 y:466
			OperatableStateMachine.add('3',
										WaitState(wait_time=2),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off})

			# x:719 y:238
			OperatableStateMachine.add('40',
										TalkState(sentence_number=40),
										transitions={'continue': '41', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:712 y:335
			OperatableStateMachine.add('41',
										TalkState(sentence_number=41),
										transitions={'continue': '3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:527 y:239
			OperatableStateMachine.add('51',
										TalkState(sentence_number=51),
										transitions={'continue': '52', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:528 y:333
			OperatableStateMachine.add('52',
										TalkState(sentence_number=52),
										transitions={'continue': '3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:556 y:35
			OperatableStateMachine.add('decide_talk',
										DecideTalkState(),
										transitions={'continue1': '51', 'continue2': '40', 'continue3': '53'},
										autonomy={'continue1': Autonomy.Off, 'continue2': Autonomy.Off, 'continue3': Autonomy.Off})

			# x:371 y:153
			OperatableStateMachine.add('53',
										TalkState(sentence_number=53),
										transitions={'continue': '54', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:376 y:338
			OperatableStateMachine.add('54',
										TalkState(sentence_number=54),
										transitions={'continue': '3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:30 y:338, x:364 y:249
		_sm_object_detection_till_face_nearby_2 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_object_detection_till_face_nearby_2:
			# x:47 y:244
			OperatableStateMachine.add('killfacegesture1',
										KillFacialGesturesState(),
										transitions={'continue': 'obj det trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:798 y:215
			OperatableStateMachine.add('chk person',
										CheckConditionState(predicate=lambda person_message: person_message.data == "yes"),
										transitions={'true': 'decidetalk56', 'false': 'sub person'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'input_value': 'person_message'})

			# x:308 y:364
			OperatableStateMachine.add('stop obj trk',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:503 y:74
			OperatableStateMachine.add('strtdobj',
										TalkState(sentence_number=25),
										transitions={'continue': 'sub person', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:592 y:305
			OperatableStateMachine.add('found face ',
										TalkState(sentence_number=24),
										transitions={'continue': 'stop obj trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:908 y:45
			OperatableStateMachine.add('sub person',
										SubscriberState(topic='/is_person_nearby', blocking=True, clear=False),
										transitions={'received': 'chk person', 'unavailable': 'chk person'},
										autonomy={'received': Autonomy.Off, 'unavailable': Autonomy.Off},
										remapping={'message': 'person_message'})

			# x:288 y:30
			OperatableStateMachine.add('decidetalk5',
										DecideTalkState(),
										transitions={'continue1': 'strtdobj', 'continue2': '61', 'continue3': '62'},
										autonomy={'continue1': Autonomy.Off, 'continue2': Autonomy.Off, 'continue3': Autonomy.Off})

			# x:503 y:148
			OperatableStateMachine.add('61',
										TalkState(sentence_number=61),
										transitions={'continue': 'sub person', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:506 y:213
			OperatableStateMachine.add('62',
										TalkState(sentence_number=62),
										transitions={'continue': 'sub person', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:792 y:381
			OperatableStateMachine.add('decidetalk56',
										DecideTalkState(),
										transitions={'continue1': 'found face ', 'continue2': '63t', 'continue3': '64t'},
										autonomy={'continue1': Autonomy.Off, 'continue2': Autonomy.Off, 'continue3': Autonomy.Off})

			# x:593 y:371
			OperatableStateMachine.add('63t',
										TalkState(sentence_number=63),
										transitions={'continue': 'stop obj trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:585 y:442
			OperatableStateMachine.add('64t',
										TalkState(sentence_number=64),
										transitions={'continue': 'stop obj trk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:102 y:77
			OperatableStateMachine.add('startfacialgestures',
										FacialGesturesState(),
										transitions={'continue': 'decidetalk5', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:95 y:156
			OperatableStateMachine.add('obj det trk',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'startfacialgestures', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:30 y:408, x:370 y:201
		_sm_what_do_next_3 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_what_do_next_3:
			# x:322 y:25
			OperatableStateMachine.add('decidetllk2',
										DecideTalkState(),
										transitions={'continue1': 't29', 'continue2': '57', 'continue3': '60'},
										autonomy={'continue1': Autonomy.Off, 'continue2': Autonomy.Off, 'continue3': Autonomy.Off})

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

			# x:582 y:225
			OperatableStateMachine.add('57',
										TalkState(sentence_number=57),
										transitions={'continue': '59', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:99 y:34
			OperatableStateMachine.add('59',
										TalkState(sentence_number=59),
										transitions={'continue': 't30', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:554 y:324
			OperatableStateMachine.add('60',
										TalkState(sentence_number=60),
										transitions={'continue': '59', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:584 y:151
			OperatableStateMachine.add('t29',
										TalkState(sentence_number=29),
										transitions={'continue': '59', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:256 y:317, x:458 y:279
		_sm_identify_4 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_identify_4:
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

			# x:587 y:33
			OperatableStateMachine.add('identify',
										IdentifyState(),
										transitions={'continue': 't20', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:807 y:28
			OperatableStateMachine.add('t20',
										TalkState(sentence_number=20),
										transitions={'continue': 'w6', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1045 y:34
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

			# x:832 y:144
			OperatableStateMachine.add('w1',
										WaitState(wait_time=1),
										transitions={'done': 'cchker gal'},
										autonomy={'done': Autonomy.Off})

			# x:1050 y:142
			OperatableStateMachine.add('cchker gal',
										WordCheckingStringState(key_word="Gal Moore"),
										transitions={'found': 'f18', 'not_found': 'chk2 coral'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:842 y:225
			OperatableStateMachine.add('f18',
										TalkState(sentence_number=18),
										transitions={'continue': '50 auth coplete', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1042 y:737
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

			# x:1051 y:236
			OperatableStateMachine.add('chk2 coral',
										WordCheckingStringState(key_word="coral"),
										transitions={'found': '47 coral', 'not_found': 'chek3 yona'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:1049 y:338
			OperatableStateMachine.add('chek3 yona',
										WordCheckingStringState(key_word="yona"),
										transitions={'found': '48 yona', 'not_found': 'check4 yaeli'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:1061 y:445
			OperatableStateMachine.add('check4 yaeli',
										WordCheckingStringState(key_word="yaeli"),
										transitions={'found': '49', 'not_found': 'chk zeev'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:645 y:373
			OperatableStateMachine.add('50 auth coplete',
										TalkState(sentence_number=50),
										transitions={'continue': 'stpfacetrk', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:843 y:283
			OperatableStateMachine.add('47 coral',
										TalkState(sentence_number=47),
										transitions={'continue': '50 auth coplete', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:841 y:356
			OperatableStateMachine.add('48 yona',
										TalkState(sentence_number=48),
										transitions={'continue': '50 auth coplete', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:837 y:430
			OperatableStateMachine.add('49',
										TalkState(sentence_number=49),
										transitions={'continue': '50 auth coplete', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1047 y:555
			OperatableStateMachine.add('chk zeev',
										WordCheckingStringState(key_word="zeev"),
										transitions={'found': 'zeev65', 'not_found': '19'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message_name'})

			# x:841 y:519
			OperatableStateMachine.add('zeev65',
										TalkState(sentence_number=65),
										transitions={'continue': '50 auth coplete', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:30 y:365, x:172 y:294
		_sm_game_5 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_game_5:
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

			# x:874 y:21
			OperatableStateMachine.add('log',
										LogState(text="log", severity=Logger.REPORT_HINT),
										transitions={'done': 'sub vino age gendre'},
										autonomy={'done': Autonomy.Off})


		# x:202 y:510, x:130 y:365
		_sm_tracking_6 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_tracking_6:
			# x:118 y:83
			OperatableStateMachine.add('stopdettrkface',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'decide_what_sy', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:439 y:266
			OperatableStateMachine.add('35',
										TalkState(sentence_number=35),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:475 y:80
			OperatableStateMachine.add('decide_what_sy',
										DecideTalkState(),
										transitions={'continue1': '35', 'continue2': 'talk55', 'continue3': 'talk56'},
										autonomy={'continue1': Autonomy.Off, 'continue2': Autonomy.Off, 'continue3': Autonomy.Off})

			# x:651 y:272
			OperatableStateMachine.add('talk55',
										TalkState(sentence_number=55),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:260 y:221
			OperatableStateMachine.add('talk56',
										TalkState(sentence_number=56),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:1214 y:584, x:130 y:368, x:849 y:566, x:938 y:579, x:793 y:382, x:1024 y:542
		_sm_user_input_speech_7 = OperatableStateMachine(outcomes=['finished', 'failed', 'identification', 'game', 'tracking', 'joke'])

		with _sm_user_input_speech_7:
			# x:105 y:65
			OperatableStateMachine.add('calib',
										SoundCalibState(length_of_calibration=5),
										transitions={'continue': 'read1', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:477 y:315
			OperatableStateMachine.add('word chk "tracking"',
										WordCheckingState(key_word="tracking"),
										transitions={'found': 'tracking', 'not_found': 'wrd chk "identification"'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:701 y:294
			OperatableStateMachine.add('wrd chk "identification"',
										WordCheckingState(key_word="identification"),
										transitions={'found': 'identification', 'not_found': 'wrd chk "game"'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:873 y:293
			OperatableStateMachine.add('wrd chk "game"',
										WordCheckingState(key_word="game"),
										transitions={'found': 'game', 'not_found': 'wrd chek "joke"'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})

			# x:1209 y:475
			OperatableStateMachine.add('39',
										TalkState(sentence_number=39),
										transitions={'continue': 'tracking', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:417 y:112
			OperatableStateMachine.add('read1',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/volume_calib.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'listen1'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'calib1'})

			# x:818 y:68
			OperatableStateMachine.add('read2',
										ReadTxtState(txt_path="/home/intel/catkin_ws/src/robot_ears/text_files/query.txt"),
										transitions={'unavailable': 'failed', 'got_message': 'stopfacedettrk22'},
										autonomy={'unavailable': Autonomy.Off, 'got_message': Autonomy.Off},
										remapping={'message': 'message'})

			# x:637 y:209
			OperatableStateMachine.add('stopfacedettrk22',
										StopFaceDetectAndTrack(),
										transitions={'continue': 'word chk "tracking"', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:607 y:31
			OperatableStateMachine.add('listen1',
										ListeningState(),
										transitions={'continue': 'read2', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'input_value': 'calib1'})

			# x:1132 y:279
			OperatableStateMachine.add('wrd chek "joke"',
										WordCheckingState(key_word="joke"),
										transitions={'found': 'joke', 'not_found': '39'},
										autonomy={'found': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'input_value': 'message'})


		# x:195 y:308, x:402 y:431
		_sm_face_det_and_start_interaction_ask_user_what_next_8 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_face_det_and_start_interaction_ask_user_what_next_8:
			# x:52 y:220
			OperatableStateMachine.add('face det trk',
										FaceDetTrack(),
										transitions={'continue': 'killfacialgestures', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:814 y:163
			OperatableStateMachine.add('tlk2',
										TalkState(sentence_number=2),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:326 y:31
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

			# x:58 y:112
			OperatableStateMachine.add('killfacialgestures',
										KillFacialGesturesState(),
										transitions={'continue': 'gesturesfacedet', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:145 y:36
			OperatableStateMachine.add('gesturesfacedet',
										FacialGesturesFaceDetState(),
										transitions={'continue': 'tlk3', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})


		# x:30 y:365, x:237 y:222
		_sm_face_server_video_and_arduino_init_9 = OperatableStateMachine(outcomes=['finished', 'failed'])

		with _sm_face_server_video_and_arduino_init_9:
			# x:54 y:82
			OperatableStateMachine.add('launch video',
										LaunchVideoStream(vid_input_num=0),
										transitions={'continue': 'init face server', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:308 y:86
			OperatableStateMachine.add('init face server',
										LaunchFaceServer(),
										transitions={'continue': 'init arduino', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:493 y:204
			OperatableStateMachine.add('init arduino',
										LaunchArduinoLed(),
										transitions={'continue': '23', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:466 y:484
			OperatableStateMachine.add('23',
										TalkState(sentence_number=23),
										transitions={'continue': 'finished', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})



		with _state_machine:
			# x:30 y:40
			OperatableStateMachine.add('face server video and arduino init',
										_sm_face_server_video_and_arduino_init_9,
										transitions={'finished': 'waking up', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:796 y:38
			OperatableStateMachine.add('face det and start interaction ask user what next',
										_sm_face_det_and_start_interaction_ask_user_what_next_8,
										transitions={'finished': 'what do next', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:454 y:512
			OperatableStateMachine.add('user input speech',
										_sm_user_input_speech_7,
										transitions={'finished': 'finished', 'failed': 'failed', 'identification': 'identify', 'game': 'game', 'tracking': 'tracking', 'joke': 'joke'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit, 'identification': Autonomy.Inherit, 'game': Autonomy.Inherit, 'tracking': Autonomy.Inherit, 'joke': Autonomy.Inherit})

			# x:721 y:192
			OperatableStateMachine.add('tracking',
										_sm_tracking_6,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:727 y:275
			OperatableStateMachine.add('game',
										_sm_game_5,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:738 y:361
			OperatableStateMachine.add('identify',
										_sm_identify_4,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:288 y:423
			OperatableStateMachine.add('what do next',
										_sm_what_do_next_3,
										transitions={'finished': 'user input speech', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:1001 y:181
			OperatableStateMachine.add('object detection till face nearby',
										_sm_object_detection_till_face_nearby_2,
										transitions={'finished': 'face det and start interaction ask user what next', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:286 y:202
			OperatableStateMachine.add('waking up',
										_sm_waking_up_1,
										transitions={'finished': 'tracking', 'failed': 'finished'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:739 y:488
			OperatableStateMachine.add('joke',
										_sm_joke_0,
										transitions={'finished': 'object detection till face nearby', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
