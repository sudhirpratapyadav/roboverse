import numpy as np
import roboverse.bullet as bullet

from roboverse.assets.shapenet_object_lists import GRASP_OFFSETS


class UR5Place:

    def __init__(self, env, xyz_action_scale=20.0, drop_point_noise=0.00):
        self.env = env
        self.xyz_action_scale = xyz_action_scale
        self.drop_point_noise = drop_point_noise
        self.reset()

    def reset(self):
        # self.dist_thresh = 0.06 + np.random.normal(scale=0.01)
        self.object_to_target = self.env.object_names[
            np.random.randint(self.env.num_objects)]
        self.drop_point = self.env.container_position
        self.drop_point[2] = -0.2
        self.place_attempted = False

    def get_action(self):
        ee_pos, _ = bullet.get_link_state(
            self.env.robot_id, self.env.end_effector_index)
        object_pos, _ = bullet.get_object_position(
            self.env.objects[self.object_to_target])
        gripper_droppoint_dist = np.linalg.norm(self.drop_point - ee_pos)
        done = False

        if gripper_droppoint_dist > 0.02:
            # lifted, now need to move towards the container
            action_xyz = (self.drop_point - ee_pos) * self.xyz_action_scale
            action_angles = [0., 0., 0.]
            action_gripper = [0]
            # print("Coming Closer")
        else:
            # already moved above the container; drop object
            action_xyz = (0., 0., 0.)
            action_angles = [0., 0., 0.]
            action_gripper = [1.0]
            self.place_attempted = True
            # print("Droping")

        agent_info = dict(place_attempted=self.place_attempted, done=done)
        neutral_action = [0.]
        action = np.concatenate(
            (action_xyz, action_angles, action_gripper, neutral_action))
        return action, agent_info
