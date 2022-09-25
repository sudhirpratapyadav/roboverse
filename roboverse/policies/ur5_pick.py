import numpy as np
import roboverse.bullet as bullet

from roboverse.assets.shapenet_object_lists import GRASP_OFFSETS


class UR5Pick:

    def __init__(self, env, pick_height_thresh=-0.30, xyz_action_scale=5.0,
                 pick_point_noise=0.00, pick_point_z=-0.31):
        self.env = env
        self.pick_height_thresh = pick_height_thresh
        self.xyz_action_scale = xyz_action_scale
        self.pick_point_noise = pick_point_noise
        self.pick_point_z = pick_point_z
        self.reset()

    def reset(self):
        # self.dist_thresh = 0.06 + np.random.normal(scale=0.01)
        self.object_to_target = self.env.object_names[
            np.random.randint(self.env.num_objects)]

        self.pick_point = bullet.get_object_position(
            self.env.objects[self.object_to_target])[0]

        print("Pick Point object:", self.pick_point)

        if self.object_to_target in GRASP_OFFSETS.keys():
            self.pick_point += np.asarray(GRASP_OFFSETS[self.object_to_target])
        self.pick_point += np.random.normal(scale=self.pick_point_noise, size=(3,))
        # self.pick_point[2] = self.pick_point_z + np.random.normal(scale=0.01)

        print("Pick Point:", self.pick_point)
        print("\n\n")

    def get_action(self):
        
        ee_pos, _ = bullet.get_link_state(
            self.env.robot_id, self.env.end_effector_index)

        object_pos, _ = bullet.get_object_position(
            self.env.objects[self.object_to_target])
        
        object_lifted = object_pos[2] > self.pick_height_thresh
        gripper_pickpoint_dist = np.linalg.norm(self.pick_point - ee_pos)

        np.set_printoptions(precision=3)
        print("\n\n----------------")
        # print("self.env.end_effector_index",self.env.end_effector_index)
        print("ee_pos:\t\t\t", ee_pos)
        print("object_pos:\t\t", object_pos)
        print("pick_point:\t\t", self.pick_point)
        print(f"obj_pos>pick_thresh: {object_pos[2]}>{self.pick_height_thresh}={object_lifted}")
        print("object_lifted:", object_lifted)
        print("gripper_pickpoint_dist:\t",gripper_pickpoint_dist)
        print("griper open:", self.env.is_gripper_open)
        

        done = False
        neutral_action = [0.]

        if gripper_pickpoint_dist > 0.05 and self.env.is_gripper_open:
            # move near the object
            action_xyz = (self.pick_point - ee_pos) * self.xyz_action_scale
            print('(self.pick_point - ee_pos)', (self.pick_point - ee_pos))
            print('self.xyz_action_scale', self.xyz_action_scale)
            print('action_xyz', action_xyz)
            xy_diff = np.linalg.norm(action_xyz[:2] / self.xyz_action_scale)
            if xy_diff > 0.08:
                action_xyz[2] = 0.0
            action_angles = [0., 0., 0.]
            action_gripper = [0.]  
            print("Coming Closer")
            print('xy_diff', xy_diff)
        elif self.env.is_gripper_open:
            # near the object enough, performs grasping action
            action_xyz = (self.pick_point - ee_pos) * self.xyz_action_scale
            action_angles = [0., 0., 0.]
            action_gripper = [-1.0]
            print("Grasping")
        elif not object_lifted:
            # lifting objects above the height threshold for picking
            action_xyz = (self.env.ee_pos_init - ee_pos) * self.xyz_action_scale
            action_angles = [0., 0., 0.]
            action_gripper = [0.]
            print("Lifiting")
        else:
            # Hold
            action_xyz = (0., 0., 0.)
            action_angles = [0., 0., 0.]
            action_gripper = [0.]
            print("Hold")
        # print("*******************\n\n")
        agent_info = dict(done=done)
        action = np.concatenate(
            (action_xyz, action_angles, action_gripper, neutral_action))
        print('policy-action:\t\t', action)
        return action, agent_info