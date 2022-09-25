import numpy as np
import time
import argparse

import roboverse
import roboverse.bullet as bullet

ACTION_SCALE = 0.5

KEY_TO_ACTION_MAPPING = {
    bullet.p.B3G_LEFT_ARROW: np.array([ACTION_SCALE, 0, 0, 0, 0, 0, 0, 0]),
    bullet.p.B3G_RIGHT_ARROW: np.array([-ACTION_SCALE, 0, 0, 0, 0, 0, 0, 0]),
    bullet.p.B3G_UP_ARROW: np.array([0, -ACTION_SCALE, 0, 0, 0, 0, 0, 0]),
    bullet.p.B3G_DOWN_ARROW: np.array([0, ACTION_SCALE, 0, 0, 0, 0, 0, 0]),
    ord('j'): np.array([0, 0, ACTION_SCALE, 0, 0, 0, 0, 0]),
    ord('k'): np.array([0, 0, -ACTION_SCALE, 0, 0, 0, 0, 0]),
    ord('h'): np.array([0, 0, 0, 0, 0, 0, -1.0, 0]),
    ord('l'): np.array([0, 0, 0, 0, 0, 0, 1.0, 0]),
    # ord('f'): np.array([0, 0, 0, 0, 0, 0, 1.0, 0])
    # ord('g'): np.array([0, 0, 0, 0, 0, 0, 1.0, 0])
}

ENV_COMMANDS = {
    ord('r'): lambda env: env.reset(),
    ord('p'): lambda env: env.save_state_disk(),
}


def keyboard_control(args):
    env = roboverse.make(args.env_name, gui=True)
    env.reset()

    while True:
        take_action = False
        action = np.array([0, 0, 0, 0, 0, 0, 0, 0], dtype='float32')
        keys = bullet.p.getKeyboardEvents()
        for qKey in keys:
            if qKey in KEY_TO_ACTION_MAPPING.keys():
                action += KEY_TO_ACTION_MAPPING[qKey]
                take_action = True
            elif qKey in ENV_COMMANDS.keys():
                ENV_COMMANDS[qKey](env)
                take_action = False

        if take_action:
            obs, rew, done, info = env.step(action)
            print("reward:",rew)
        time.sleep(0.1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--env-name", type=str,
                        default='UR5GraspEasy-v0')
    args = parser.parse_args()
    keyboard_control(args)
