import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import pathlib
import random
import roboverse
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--env-name", type=str, required=True)
parser.add_argument("-d", "--dataset_name", type=str, required=True)
args = parser.parse_args()

BASE_PATH =  '/home/sudhir/robotics/datasets/'

DATASET_NAME = args.dataset_name

# DATASET_NAME = 'UR5PlaceTray-v0_15K_save_all_noise_0.03_2022-04-24T17-51-55_5000_less'
DATA_PATH = BASE_PATH + DATASET_NAME + '.npy'
data = np.load(DATA_PATH, allow_pickle=True)

print("Creating env")
env_id = args.env_name
env = roboverse.make(env_id, gui=True)
print("action_space:", env.action_space)

print("Resset env")
env.reset()

env.add_display_trajectories(data)





# time.sleep(2)
print("\n\n\n######################  STARTING SIMULATION  #################\n")
for i_step in range(100):

	action = env.action_space.sample()
	action = np.zeros(8)
	action = np.zeros(8)
	# if(i_step<50):
	#     action[0] = 0.5
	#     action[1] = 0.0
	#     action[2] = 0.0
	# else:
	#     action[0] = -0.5
	#     action[1] = 0.0
	#     action[2] = 0.0

	print(f'step: {i_step}')
	# print(f"action: {type(action)}, {action}")
	# xyz_action = action[:3]  # ee position actions
	# abc_action = action[3:6]  # ee orientation actions
	# gripper_action = action[6]
	# neutral_action = action[7]
	# print(f"action: {action}, xyz:{xyz_action}, abc{abc_action}")
	# print(f"Step:{i_step}")
	env.step(action)
	time.sleep(1)
print("\n######################  STOPPING SIMULATION  #################\n\n")