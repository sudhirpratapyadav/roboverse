import gym
import numpy as np
import time

from roboverse.bullet.serializable import Serializable
import roboverse.bullet as bullet
from roboverse.envs import objects
from roboverse.bullet import object_utils

import os.path as osp

### Parameters
END_EFFECTOR_INDEX = 7

RESET_JOINT_INDICES = [1, 2, 3, 4, 5, 6, 9, 11]

RESET_JOINT_VALUES = [0.0, -1.32, 1.57, 1.32, 1.57, 1.57] + [-0.055, 0.055]

RESET_JOINT_VALUES_GRIPPER_CLOSED = [0.0, -1.32, 1.57, 1.32, 1.57, 1.57] + [-0.0, 0.0]

JOINT_LIMIT_LOWER = [-3.14, -3.14, -3.14, -3.14, -3.14, -3.14]+[-0.055, 0.0]
JOINT_LIMIT_UPPER = [3.14, 3.14, 3.14, 3.14, 3.14, 3.14]+[0.0, 0.055]

JOINT_RANGE = []
for upper, lower in zip(JOINT_LIMIT_LOWER, JOINT_LIMIT_UPPER):
	JOINT_RANGE.append(upper - lower)

ACTION_DIM = 8

GRIPPER_CONFIG= {
					'name':'wsg',
					'movable_joints_num': 2,
					'joint_values_open': (-0.055, 0.055),
					'joint_values_close': (-0.00, 0.00),
					}

class UR5Env(gym.Env, Serializable):

	def __init__(self,
				 control_mode='continuous',
				 observation_mode='pixels',
				 observation_img_dim=48,
				 transpose_image=True,

				 object_names=('beer_bottle', 'gatorade'),
				 object_scales=(0.75, 0.75),
				 object_orientations=((0, 0, 1, 0), (0, 0, 1, 0)),
				 object_position_high=(.7, .27, -.30),
				 object_position_low=(.5, .18, -.30),
				 target_object='gatorade',
				 load_tray=True,

				 num_sim_steps=10,
				 num_sim_steps_reset=50,
				 num_sim_steps_discrete_action=75,

				 reward_type='grasping',
				 grasp_success_height_threshold=-0.3,
				 grasp_success_object_gripper_threshold=0.1,

				 use_neutral_action=False,
				 neutral_gripper_open=True,

				 xyz_action_scale=1.0,
				 rpy_action_scale=20.0,

				 ee_pos_high=(0.9, 0.35, 0.0),
				 ee_pos_low=(0.45, -0.4, -.34),

				 camera_target_pos=(0.6, 0.2, -0.1),
				 camera_distance=0.5,
				 camera_roll=0.0,
				 camera_pitch=-30,
				 camera_yaw=180,

				 gui=False,
				 in_vr_replay=False,
				 ):


		self.control_mode = control_mode
		self.observation_mode = observation_mode
		self.observation_img_dim = observation_img_dim
		self.transpose_image = transpose_image

		self.num_sim_steps = num_sim_steps
		self.num_sim_steps_reset = num_sim_steps_reset
		self.num_sim_steps_discrete_action = num_sim_steps_discrete_action

		self.reward_type = reward_type
		self.grasp_success_height_threshold = grasp_success_height_threshold
		self.grasp_success_object_gripper_threshold = \
			grasp_success_object_gripper_threshold

		self.use_neutral_action = use_neutral_action
		self.neutral_gripper_open = neutral_gripper_open

		self.gui = gui

		# TODO(avi): This hard-coding should be removed
		self.fc_input_key = 'state'
		self.cnn_input_key = 'image'
		self.terminates = False
		self.scripted_traj_len = 30

		# TODO(avi): Add limits to ee orientation as well
		self.ee_pos_high = ee_pos_high
		self.ee_pos_low = ee_pos_low

		bullet.connect_headless(self.gui)

		# object stuff
		assert target_object in object_names
		assert len(object_names) == len(object_scales)
		self.load_tray = load_tray
		self.num_objects = len(object_names)
		self.object_position_high = list(object_position_high)
		self.object_position_low = list(object_position_low)
		self.object_names = object_names
		self.target_object = target_object
		self.object_scales = dict()
		self.object_orientations = dict()
		for orientation, object_scale, object_name in \
				zip(object_orientations, object_scales, self.object_names):
			self.object_orientations[object_name] = orientation
			self.object_scales[object_name] = object_scale

		self.in_vr_replay = in_vr_replay

		### LOADING MESHES
		print("\n Loading meshses")
		self._load_meshes() ## THIS WILL UPDATE ROBOT ID

		self.movable_joints = bullet.get_movable_joints(self.robot_id)
		print("movable_joints:", self.movable_joints)

		self.end_effector_index = END_EFFECTOR_INDEX
		# self.reset_joint_values = RESET_JOINT_VALUES_GRIPPER_CLOSED
		self.reset_joint_values = RESET_JOINT_VALUES
		self.reset_joint_indices = RESET_JOINT_INDICES

		self.xyz_action_scale = xyz_action_scale
		self.rpy_action_scale = rpy_action_scale

		self.camera_target_pos = camera_target_pos
		self.camera_distance = camera_distance
		self.camera_roll = camera_roll
		self.camera_pitch = camera_pitch
		self.camera_yaw = camera_yaw

		view_matrix_args = dict(target_pos=self.camera_target_pos,
								distance=self.camera_distance,
								yaw=self.camera_yaw,
								pitch=self.camera_pitch,
								roll=self.camera_roll,
								up_axis_index=2)

		self._view_matrix_obs = bullet.get_view_matrix(
			**view_matrix_args)
		self._projection_matrix_obs = bullet.get_projection_matrix(
			self.observation_img_dim, self.observation_img_dim)

		self._set_action_space()
		self._set_observation_space()

		self.is_gripper_open = True  # TODO(avi): Clean this up
		self.reset()
		self.ee_pos_init, self.ee_quat_init = bullet.get_link_state(self.robot_id, self.end_effector_index)

		# startPoint = self.ee_pos_init.tolist()
		# endPoint = (self.ee_pos_init+np.array([-0.5,0.0,0.0])).tolist()
		# self.lineID= bullet.addLine(startPoint, [1,1,1], color=[255,0,0], lineWidth=2)

	def _load_meshes(self):
		self.table_id = objects.table()
		self.robot_id = objects.UR5()

		if self.load_tray:
			self.tray_id = objects.tray()

		self.objects = {}
		if self.in_vr_replay:
			object_positions = self.original_object_positions
		else:
			object_positions = object_utils.generate_object_positions(
				self.object_position_low, self.object_position_high,
				self.num_objects,
			)
			self.original_object_positions = object_positions
		for object_name, object_position in zip(self.object_names,
												object_positions):
			self.objects[object_name] = object_utils.load_object(
				object_name,
				object_position,
				object_quat=self.object_orientations[object_name],
				scale=self.object_scales[object_name])
			bullet.step_simulation(self.num_sim_steps_reset)

	def reset(self):
		bullet.reset()
		bullet.setup_headless()
		self._load_meshes()
		bullet.reset_robot(
			self.robot_id,
			self.reset_joint_indices,
			self.reset_joint_values)
		self.is_gripper_open = True  # TODO(avi): Clean this up

		return self.get_observation()

	def save_state_disk(self):
		FILE_PATH = osp.join(osp.dirname(osp.dirname(osp.realpath(__file__))),
				'assets/bullet-objects/bullet_saved_states/objects_in_gripper/ur5_object_in_gripper_reset.bullet')
		bullet.save_state(FILE_PATH)

	def _get_gripper_poses(self, gripper_action, gripper_state, gripper_config, grip_action_open=1, grip_action_close=-1):

		GRIP_OPEN = 0
		GRIP_CLOSE = 1

		if self.control_mode == 'continuous':
			num_sim_steps = self.num_sim_steps
			target_grip_value = (gripper_action-grip_action_open)/(grip_action_close-grip_action_open)

		elif self.control_mode == 'discrete_gripper':
			if gripper_action > 0.5 and not self.is_gripper_open:
				# print("OPEN GRIPPER")
				num_sim_steps = self.num_sim_steps_discrete_action
				target_grip_value = GRIP_OPEN
				self.is_gripper_open = True

			elif gripper_action < -0.5 and self.is_gripper_open:
				# print("CLOSE GRIPPER")
				num_sim_steps = self.num_sim_steps_discrete_action
				target_grip_value = GRIP_CLOSE
				self.is_gripper_open = False
			else:
				num_sim_steps = self.num_sim_steps
				if self.is_gripper_open:
					target_grip_value = GRIP_OPEN
				else:
					target_grip_value = GRIP_CLOSE
		else:       
			raise NotImplementedError

		target_gripper_poses = []

		if(gripper_config['name']=='wsg'):
			joints =  gripper_config['movable_joints_num']
			for i in range(joints):
				joint_open = gripper_config['joint_values_open'][i]
				joint_close = gripper_config['joint_values_close'][i]
				target_pose = joint_open+ target_grip_value*(joint_close-joint_open)
				target_gripper_poses.append(target_pose)

		return target_gripper_poses, num_sim_steps

	def step(self, action):
		# np.set_printoptions(precision=3)

		# TODO Clean this up
		if np.isnan(np.sum(action)):
			print('action', action)
			raise RuntimeError('Action has NaN entries')

		action = np.clip(action, -1, +1)  # TODO Clean this up

		xyz_action = action[:3]  # ee position actions
		rpy_action = action[3:6]  # ee orientation actions
		gripper_action = action[6]
		neutral_action = action[7]

		
		joint_states, _ = bullet.get_joint_states(self.robot_id, self.movable_joints)
		gripper_state = joint_states[6]

		ee_pos, ee_quat = bullet.get_link_state(self.robot_id, self.end_effector_index)
		target_ee_pos = ee_pos + self.xyz_action_scale * xyz_action
		print()
		
		print(f'xyz-action:\t\t {xyz_action}')
		print(f'xyz-action-scale:\t\t {self.xyz_action_scale}')
		print(f'env-action:\t\t {self.xyz_action_scale * xyz_action}')
		print('ee-pos:\t\t\t', ee_pos)
		print('ee-quat:\t\t\t', ee_quat)
		print('target-pos:\t\t', target_ee_pos)

		target_ee_pos = np.clip(target_ee_pos, self.ee_pos_low, self.ee_pos_high)

		target_ee_deg = bullet.quat_to_deg(ee_quat) + self.rpy_action_scale * rpy_action
		target_ee_quat = bullet.deg_to_quat(target_ee_deg)

		
		target_gripper_poses, num_sim_steps = self._get_gripper_poses(gripper_action, gripper_state, GRIPPER_CONFIG)

		bullet.apply_action_ik(
			target_ee_pos, target_ee_quat, target_gripper_poses,
			self.robot_id,
			self.end_effector_index, self.movable_joints,
			lower_limit=JOINT_LIMIT_LOWER,
			upper_limit=JOINT_LIMIT_UPPER,
			rest_pose=RESET_JOINT_VALUES,
			joint_range=JOINT_RANGE,
			num_sim_steps=num_sim_steps)

		# print("use_neutral_action:",self.use_neutral_action)
		if self.use_neutral_action and neutral_action > 0.5:
			if self.neutral_gripper_open:
				bullet.move_to_neutral(
					self.robot_id,
					self.reset_joint_indices,
					RESET_JOINT_VALUES)
			else:
				bullet.move_to_neutral(
					self.robot_id,
					self.reset_joint_indices,
					RESET_JOINT_VALUES_GRIPPER_CLOSED)

		info = self.get_info()
		reward = self.get_reward(info)
		done = False
		return self.get_observation(), reward, done, info

	def get_observation(self):
		gripper_state = self.get_gripper_state()
		gripper_binary_state = [float(self.is_gripper_open)]
		ee_pos, ee_quat = bullet.get_link_state(
			self.robot_id, self.end_effector_index)
		object_position, object_orientation = bullet.get_object_position(
			self.objects[self.target_object])
		if self.observation_mode == 'pixels':
			image_observation = self.render_obs()
			image_observation = np.float32(image_observation.flatten()) / 255.0
			observation = {
				'object_position': object_position,
				'object_orientation': object_orientation,
				'state': np.concatenate(
					(ee_pos, ee_quat, gripper_state, gripper_binary_state)),
				'image': image_observation
			}
		else:
			raise NotImplementedError

		return observation

	def get_reward(self, info):
		if self.reward_type == 'grasping':
			reward = float(info['grasp_success_target'])
		else:
			raise NotImplementedError
		return reward

	def get_info(self):

		info = {'grasp_success': False}
		for object_name in self.object_names:
			grasp_success = object_utils.check_grasp(
				object_name, self.objects, self.robot_id,
				self.end_effector_index, self.grasp_success_height_threshold,
				self.grasp_success_object_gripper_threshold)
			if grasp_success:
				info['grasp_success'] = True

		info['grasp_success_target'] = object_utils.check_grasp(
			self.target_object, self.objects, self.robot_id,
			self.end_effector_index, self.grasp_success_height_threshold,
			self.grasp_success_object_gripper_threshold)

		return info

	def render_obs(self):
		img, depth, segmentation = bullet.render(
			self.observation_img_dim, self.observation_img_dim,
			self._view_matrix_obs, self._projection_matrix_obs, shadow=0)
		if self.transpose_image:
			img = np.transpose(img, (2, 0, 1))
		return img

	def _set_action_space(self):
		self.action_dim = ACTION_DIM
		act_bound = 1
		act_high = np.ones(self.action_dim) * act_bound
		self.action_space = gym.spaces.Box(-act_high, act_high)

	def _set_observation_space(self):
		if self.observation_mode == 'pixels':
			self.image_length = (self.observation_img_dim ** 2) * 3
			img_space = gym.spaces.Box(0, 1, (self.image_length,),
									   dtype=np.float32)
			robot_state_dim = 10  # XYZ + QUAT + GRIPPER_STATE
			obs_bound = 100
			obs_high = np.ones(robot_state_dim) * obs_bound
			state_space = gym.spaces.Box(-obs_high, obs_high)
			spaces = {'image': img_space, 'state': state_space}
			self.observation_space = gym.spaces.Dict(spaces)
		else:
			raise NotImplementedError

	def get_gripper_state(self):
		joint_states, _ = bullet.get_joint_states(self.robot_id,
												  self.movable_joints)
		gripper_state = np.asarray(joint_states[-2:])
		return gripper_state

	def close(self):
		bullet.disconnect()

	def add_display_trajectories(self, data):
		keys = ['observations',
		'terminals',
		'rewards',
		'actions',
		'next_observations',
		'agent_infos',
		'env_infos']

		observations_keys = ['image', 'object_orientation', 'object_position', 'state']

		NUM_SAMPLES = len(data)
		PATH_LENGTH = len(data[0]['observations'])

		# NUM_SAMPLES = 10

		print('PATH_LENGTH', PATH_LENGTH)

		returns = []
		a_avgs = []

		np.set_printoptions(precision=3, suppress=True)

		self.lineIDs = []

		for sample_idx in range(NUM_SAMPLES):

			rewards = data[sample_idx]['rewards']
			success = np.array(rewards).sum() > 0.0

			print('sample_idx', sample_idx, np.array(rewards).sum())


			for step in range(PATH_LENGTH):
				state = data[sample_idx]['observations'][step]['state']
				action = data[sample_idx]['actions'][step]
				reward = data[sample_idx]['rewards'][step]
				next_state = data[sample_idx]['next_observations'][step]['state']

				print(f'\nepisode {sample_idx}, step {step}')
				print(f'state {state}')
				print(f'action {action}')
				print(f'reward {reward}')
				print(f'next_state {next_state}')

				gripper_action = action[-2]

				startPoint = state[0:3].tolist()
				endPoint = next_state[0:3].tolist()
				if(success):
					# if(gripper_action > 0.5): ##open
					# 	lineID = bullet.addLine(startPoint, endPoint, color=[0,0,255], lineWidth=2)
					# elif(gripper_action < -0.5): ##close
					# 	lineID = bullet.addLine(startPoint, endPoint, color=[0,255,125], lineWidth=2)
					# else: ##no-action
					
					lineID = bullet.addLine(startPoint, endPoint, color=[0,255,0], lineWidth=1)
				else:
					# if(gripper_action > 0.5): ##open
					# 	lineID = bullet.addLine(startPoint, endPoint, color=[255,0,255], lineWidth=2)
					# elif(gripper_action < -0.5): ##close
					# 	lineID = bullet.addLine(startPoint, endPoint, color=[255,0,125], lineWidth=2)
					# else: ##no-action
					
					lineID = bullet.addLine(startPoint, endPoint, color=[255,0,0], lineWidth=1)

				
				self.lineIDs.append(lineID)



# if __name__ == "__main__":
#     env = UR5Env(gui=True)
#     import time
#
#     env.reset()
#     # import IPython; IPython.embed()
#
#     for i in range(20):
#         print(i)
#         obs, rew, done, info = env.step(
#             np.asarray([-0.05, 0., 0., 0., 0., 0.5, 0.]))
#         print("reward", rew, "info", info)
#         time.sleep(0.1)
#
#     env.reset()
#     time.sleep(1)
#     for _ in range(25):
#         env.step(np.asarray([0., 0., 0., 0., 0., 0., 0.6]))
#         time.sleep(0.1)
#
#     env.reset()
