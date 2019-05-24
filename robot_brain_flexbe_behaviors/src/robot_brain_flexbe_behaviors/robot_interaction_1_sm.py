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


		with _state_machine:
			# x:222 y:60
			OperatableStateMachine.add('launch video',
										LaunchVideoStream(),
										transitions={'continue': 'detect and track', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:435 y:60
			OperatableStateMachine.add('detect and track',
										LaunchObjDetectAndTrack(),
										transitions={'continue': 'subscriber_is_nearby_face_State', 'failed': 'detect and track'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:693 y:41
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

			# x:590 y:161
			OperatableStateMachine.add('logger',
										LogState(text="false", severity=Logger.REPORT_HINT),
										transitions={'done': 'subscriber_is_nearby_face_State'},
										autonomy={'done': Autonomy.Off})

			# x:935 y:201
			OperatableStateMachine.add('stop obj detect state',
										StopObjectDetectAndTrack(),
										transitions={'continue': 'face identified', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1127 y:263
			OperatableStateMachine.add('launch face detect and track',
										FaceDetTrack(),
										transitions={'continue': 'wait to show face trk', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:1091 y:385
			OperatableStateMachine.add('wait to show face trk',
										WaitState(wait_time=5),
										transitions={'done': 'talk hello'},
										autonomy={'done': Autonomy.Off})

			# x:1089 y:547
			OperatableStateMachine.add('talk hello',
										TalkState(sentence_number=2),
										transitions={'continue': 'stop face detect', 'failed': 'stop face detect'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off})

			# x:624 y:472
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


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
