from roboverse.envs.ur5 import UR5Env
from roboverse.bullet import object_utils
import roboverse.bullet as bullet
from roboverse.envs import objects
from roboverse.assets.shapenet_object_lists import CONTAINER_CONFIGS
import os.path as osp

OBJECT_IN_GRIPPER_PATH = osp.join(osp.dirname(osp.dirname(osp.realpath(__file__))),
                'assets/bullet-objects/bullet_saved_states/objects_in_gripper/')


class UR5PickPlaceEnv(UR5Env):

    def __init__(self,
                 container_name='bowl_small',
                 fixed_container_position=False,
                 start_object_in_gripper=False,
                 **kwargs
                 ):
        self.container_name = container_name

        container_config = CONTAINER_CONFIGS[self.container_name]
        self.fixed_container_position = fixed_container_position
        if self.fixed_container_position:
            self.container_position_low = container_config['container_position_default']
            self.container_position_high = container_config['container_position_default']
        else:
            self.container_position_low = container_config['container_position_low']
            self.container_position_high = container_config['container_position_high']
        self.container_position_z = container_config['container_position_z']
        self.container_orientation = container_config['container_orientation']
        self.container_scale = container_config['container_scale']
        self.min_distance_from_object = container_config['min_distance_from_object']

        self.place_success_height_threshold = container_config['place_success_height_threshold']
        self.place_success_radius_threshold = container_config['place_success_radius_threshold']

        self.start_object_in_gripper = start_object_in_gripper

        super(UR5PickPlaceEnv, self).__init__(**kwargs)

    def _load_meshes(self):
        self.table_id = objects.table()
        self.robot_id = objects.UR5()
        self.objects = {}

        """
        TODO(avi) This needs to be cleaned up, generate function should only
                  take in (x,y) positions instead.
        """
        assert self.container_position_low[2] == self.object_position_low[2]

        if self.num_objects == 2:
            self.container_position, self.original_object_positions = \
                object_utils.generate_object_positions_v2(
                    self.object_position_low, self.object_position_high,
                    self.container_position_low, self.container_position_high,
                    min_distance_small_obj=0.07,
                    min_distance_large_obj=self.min_distance_from_object,
                )
        elif self.num_objects == 1:
            self.container_position, self.original_object_positions = \
                object_utils.generate_object_positions_single(
                    self.object_position_low, self.object_position_high,
                    self.container_position_low, self.container_position_high,
                    min_distance_large_obj=self.min_distance_from_object,
                )
        else:
            raise NotImplementedError

        # TODO(avi) Need to clean up
        self.container_position[-1] = self.container_position_z
        self.container_id = object_utils.load_object(self.container_name,
                                                     self.container_position,
                                                     self.container_orientation,
                                                     self.container_scale)
        bullet.step_simulation(self.num_sim_steps_reset)
        for object_name, object_position in zip(self.object_names,
                                                self.original_object_positions):
            self.objects[object_name] = object_utils.load_object(
                object_name,
                object_position,
                object_quat=self.object_orientations[object_name],
                scale=self.object_scales[object_name])
            bullet.step_simulation(self.num_sim_steps_reset)

    def reset(self):
        super(UR5PickPlaceEnv, self).reset()
        ee_pos_init, ee_quat_init = bullet.get_link_state(
            self.robot_id, self.end_effector_index)

        if self.start_object_in_gripper:
            bullet.load_state(osp.join(OBJECT_IN_GRIPPER_PATH,
                'ur5_object_in_gripper_reset.bullet'))
            self.is_gripper_open = False

        return self.get_observation()

    def get_reward(self, info):
        if self.reward_type == 'pick_place':
            reward = float(info['place_success_target'])
        elif self.reward_type == 'grasp':
            reward = float(info['grasp_success_target'])
        else:
            raise NotImplementedError
        return reward

    def get_info(self):
        info = super(UR5PickPlaceEnv, self).get_info()

        info['place_success'] = False
        for object_name in self.object_names:
            place_success = object_utils.check_in_container(
                object_name, self.objects, self.container_position,
                self.place_success_height_threshold,
                self.place_success_radius_threshold)
            if place_success:
                info['place_success'] = place_success

        info['place_success_target'] = object_utils.check_in_container(
            self.target_object, self.objects, self.container_position,
            self.place_success_height_threshold,
            self.place_success_radius_threshold)

        return info
