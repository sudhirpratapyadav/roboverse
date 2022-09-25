import numpy as np
import time
import os
import os.path as osp
import roboverse
from roboverse.policies import policies
import argparse

from roboverse.utils import get_timestamp
import sys
import pathlib

EPSILON = 0.1

BASE_PATH =  pathlib.Path(__file__).parent
SAVE_PATH = (BASE_PATH / '../../../results_data_collection/').resolve()

if not os.path.exists(SAVE_PATH):
	os.makedirs(SAVE_PATH)

PRINT_FILE_PATH = os.path.join(SAVE_PATH , 'log.txt')

def sec_to_str(sec):
	sec = int(sec)
	s = sec%60
	h = int(sec//3600)
	m = int((sec - h*3600)//60)
	s = int(sec - h*3600 -m*60)
	return f"{h:02d}h:{m:02d}m:{s:02d}s"

def add_transition(traj, observation, action, reward, info, agent_info, done,
				   next_observation, img_dim):
	observation["image"] = np.reshape(np.uint8(observation["image"] * 255.),
									  (img_dim, img_dim, 3))
	traj["observations"].append(observation)
	next_observation["image"] = np.reshape(
		np.uint8(next_observation["image"] * 255.), (img_dim, img_dim, 3))
	traj["next_observations"].append(next_observation)
	traj["actions"].append(action)
	traj["rewards"].append(reward)
	traj["terminals"].append(done)
	traj["agent_infos"].append(agent_info)
	traj["env_infos"].append(info)
	return traj


def collect_one_traj(env, policy, num_timesteps, noise,
					 accept_trajectory_key):
	num_steps = -1
	rewards = []
	success = False
	img_dim = env.observation_img_dim
	env.reset()
	policy.reset()
	time.sleep(1)
	traj = dict(
		observations=[],
		actions=[],
		rewards=[],
		next_observations=[],
		terminals=[],
		agent_infos=[],
		env_infos=[],
	)
	for j in range(num_timesteps):

		print(f"\nstep: {j+1}/{num_timesteps}")

		action, agent_info = policy.get_action()

		# In case we need to pad actions by 1 for easier realNVP modelling
		env_action_dim = env.action_space.shape[0]
		if env_action_dim - action.shape[0] == 1:
			action = np.append(action, 0)
		action += np.random.normal(scale=noise, size=(env_action_dim,))
		# print('noised_action:\t', action)
		action = np.clip(action, -1 + EPSILON, 1 - EPSILON)
		observation = env.get_observation()
		next_observation, reward, done, info = env.step(action)
		add_transition(traj, observation,  action, reward, info, agent_info,
					   done, next_observation, img_dim)

		if info[accept_trajectory_key] and num_steps < 0:
			num_steps = j

		rewards.append(reward)
		if done or agent_info['done']:
			break
	# print(accept_trajectory_key)
	# print('success: ', info[accept_trajectory_key])
	if info[accept_trajectory_key]:
		success = True

	return traj, success, num_steps


def main(args):

	timestamp = get_timestamp()
	data_save_path = osp.join(__file__, "../..", "data", args.save_directory)
	data_save_path = osp.abspath(data_save_path)
	if not osp.exists(data_save_path):
		os.makedirs(data_save_path)

	env = roboverse.make(args.env_name,
						 gui=args.gui,
						 transpose_image=False)

	data = []
	# print(args.policy_name)
	print(type(policies))
	print("Policies: ", policies.keys())
	print("Env:", env.get_info().keys())
	assert args.policy_name in policies.keys(), f"The policy name must be one of: {policies.keys()}"
	assert args.accept_trajectory_key in env.get_info().keys(), \
		"The accept trajectory key must be one of: {env.get_info().keys()}"
	policy_class = policies[args.policy_name]
	policy = policy_class(env)
	num_success = 0
	num_saved = 0
	num_attempts = 0
	accept_trajectory_key = args.accept_trajectory_key

	# progress_bar = tqdm(total=args.num_trajectories)
	eta = None
	episode_time = None
	previous_episode_time = None
	start_time = time.time()

	while num_saved < args.num_trajectories:
		num_attempts += 1
		traj, success, num_steps = collect_one_traj(
			env, policy, args.num_timesteps, args.noise,
			accept_trajectory_key)

		if success:
			data.append(traj)
			num_success += 1
			num_saved += 1

			t = time.time()
			if episode_time is None:
				episode_time = t - start_time
			else:
				episode_time = t - previous_episode_time
			eta = episode_time*(args.num_trajectories-num_saved)
			elapsed_time = t - start_time
			total_time = elapsed_time + eta
			previous_episode_time = t

			# print(f"episodes completed: {num_saved}/{args.num_trajectories} episode_time:{episode_time:.1f}s \telapsed/total:({sec_to_str(elapsed_time)}/{sec_to_str(total_time)}) \tETA:{sec_to_str(eta)}")
			# print("success rate: {}".format(num_success/(num_attempts)))

			# with open(PRINT_FILE_PATH, 'a') as f:
			# 	print(f"episodes completed: {num_saved}/{args.num_trajectories} episode_time:{episode_time:.1f}s \telapsed/total:({sec_to_str(elapsed_time)}/{sec_to_str(total_time)}) \tETA:{sec_to_str(eta)}", file=f)
			# 	print("success rate: {}".format(num_success/(num_attempts)), file=f)

		elif args.save_all:
			data.append(traj)
			num_saved += 1

			t = time.time()
			if episode_time is None:
				episode_time = t - start_time
			else:
				episode_time = t - previous_episode_time
			eta = episode_time*(args.num_trajectories-num_saved)
			elapsed_time = t - start_time
			total_time = elapsed_time + eta
			previous_episode_time = t

			print(f"episodes completed: {num_saved}/{args.num_trajectories} episode_time:{episode_time:.1f}s \telapsed/total:({sec_to_str(elapsed_time)}/{sec_to_str(total_time)}) \tETA:{sec_to_str(eta)}")
			print("success rate: {}".format(num_success/(num_attempts)))

			with open(PRINT_FILE_PATH, 'a') as f:
				print(f"Thread:{args.save_id}, episodes completed: {num_saved}/{args.num_trajectories} episode_time:{episode_time:.1f}s \telapsed/total:({sec_to_str(elapsed_time)}/{sec_to_str(total_time)}) \tETA:{sec_to_str(eta)}", file=f)
				print("success rate: {}".format(num_success/(num_attempts)), file=f)

				

		print('\n------')
		print(f'episodes completed: {num_saved}/{args.num_trajectories}')
		print("num_timesteps: ", num_steps)
		print('reward:', np.sum(traj['rewards']))
		print("success rate: {}".format(num_success/(num_attempts)))
		print('------\n')			

	print("\n\nOver-all success rate: {}".format(num_success / (num_attempts)))
	path = osp.join(data_save_path, "scripted_{}_{}_{}_{}.npy".format(
		args.env_name, timestamp, args.noise, args.save_id))
	print(path)
	np.save(path, data)


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--env-name", type=str, required=True)
	parser.add_argument("-pl", "--policy-name", type=str, required=True)
	parser.add_argument("-a", "--accept-trajectory-key", type=str, required=True)
	parser.add_argument("-n", "--num-trajectories", type=int, required=True)
	parser.add_argument("-t", "--num-timesteps", type=int, required=True)
	parser.add_argument("--save-all", action='store_true', default=False)
	parser.add_argument("--gui", action='store_true', default=False)
	parser.add_argument("-o", "--target-object", type=str)
	parser.add_argument("-d", "--save-directory", type=str, default="")
	parser.add_argument("--noise", type=float, default=0.05)
	parser.add_argument("-s", "--save_id", type=str, default="0")
	args = parser.parse_args()

	main(args)
