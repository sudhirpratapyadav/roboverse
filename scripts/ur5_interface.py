import roboverse
import time
import numpy as np

# env = roboverse.make('Widow250PickTray-v0', gui=True)
### make function is in envs.registration
print("Creating env")
env = roboverse.make('UR5GraspEasy-v0', gui=True)
print("Resset env")
env.reset()

print("action_space:", env.action_space)

# time.sleep(2)
print("\n\n\n######################  STARTING SIMULATION  #################\n")
for i_step in range(100):

    action = env.action_space.sample()
    action = np.zeros(8)
    action = np.zeros(8)
    if(i_step<50):
        action[0] = 0.5
        action[1] = 0.0
        action[2] = 0.0
    else:
        action[0] = -0.5
        action[1] = 0.0
        action[2] = 0.0
    

    # if (i_step%2):
    #     action[6] = -1
    # else:
    #     action[6] = 1

    # print(f"action: {type(action)}, {action}")
    # xyz_action = action[:3]  # ee position actions
    # abc_action = action[3:6]  # ee orientation actions
    # gripper_action = action[6]
    # neutral_action = action[7]
    # print(f"action: {action}, xyz:{xyz_action}, abc{abc_action}")
    # print(f"Step:{i_step}")
    env.step(action)
    time.sleep(0.1)
print("\n######################  STOPPING SIMULATION  #################\n\n")