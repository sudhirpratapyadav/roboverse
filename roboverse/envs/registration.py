import gym
from roboverse.assets.shapenet_object_lists \
	import GRASP_TRAIN_OBJECTS, GRASP_TEST_OBJECTS, PICK_PLACE_TRAIN_OBJECTS, \
	PICK_PLACE_TEST_OBJECTS, TRAIN_CONTAINERS, TEST_CONTAINERS

ENVIRONMENT_SPECS = (
	{
		'id': 'UR5GraspEasy-v0',
		'entry_point': 'roboverse.envs.ur5:UR5Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (1.0,),
				   'load_tray': False,
				   'object_position_high': (.6, .2, -.30),
				   'object_position_low': (.6, .2, -.30),

				   'xyz_action_scale':0.2,
				   }
	},
	{
		'id': 'UR5PlaceTray-v0',
		'entry_point': 'roboverse.envs.ur5_pickplace:UR5PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_high': (.7, .2, -.30),
				   'object_position_low': (.7, .2, -.30),

				   'container_name': 'tray',
				   'fixed_container_position': True,
				   'start_object_in_gripper': True,

				   'use_neutral_action': True,
				   'neutral_gripper_open': False,

				   'xyz_action_scale':0.05,
				   }
	},
	{
		'id': 'UR5DrawerOpen-v0',
		'entry_point': 'roboverse.envs.ur5_drawer:UR5DrawerEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (1,),
				   'target_object': 'ball',
				   'load_tray': False,

				   'xyz_action_scale':0.2,
				   }
	},
	{
		'id': 'Widow250Grasp-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'duck',
				   'load_tray': True,
				   'xyz_action_scale': 0.2,
				   }
	},





	{
		'id': 'Widow250GraspEasy-shed-area-53-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.85, 0.35, -.30),
				   'object_position_low': (.35, 0.15, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-shed-area-43-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.80, .33, -.30),
				   'object_position_low': (.40, .17, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-shed-area-32-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.75, .31, -.30),
				   'object_position_low': (.45, .19, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-shed-area-21-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.70, .29, -.30),
				   'object_position_low': (.50, .21, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-shed-area-10-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.65, .27, -.30),
				   'object_position_low': (.55, .23, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-shed-area-00-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'shed',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.60, .25, -.30),
				   'object_position_low': (.60, .25, -.30),
				   }
	},



	{
		'id': 'Widow250GraspEasy-cube-area-53-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.85, 0.35, -.30),
				   'object_position_low': (.35, 0.15, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-cube-area-43-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.80, .33, -.30),
				   'object_position_low': (.40, .17, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-cube-area-32-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.75, .31, -.30),
				   'object_position_low': (.45, .19, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-cube-area-21-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.70, .29, -.30),
				   'object_position_low': (.50, .21, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-cube-area-10-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.65, .27, -.30),
				   'object_position_low': (.55, .23, -.30),
				   }
	},
	{
		'id': 'Widow250GraspEasy-cube-area-00-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.60, .25, -.30),
				   'object_position_low': (.60, .25, -.30),
				   }
	},

	







	{
		'id': 'Widow250DrawerRandomizedOpen-area-53-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'drawer_position_high': (.85, 0.35, -.35),
				   'drawer_position_low': (.35, 0.15, -.35),
				   }
	},
	{
		'id': 'Widow250DrawerRandomizedOpen-area-43-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'drawer_position_high': (.80, .33, -.35),
				   'drawer_position_low': (.40, .17, -.35),
				   }
	},
	{
		'id': 'Widow250DrawerRandomizedOpen-area-32-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'drawer_position_high': (.75, .31, -.35),
				   'drawer_position_low': (.45, .19, -.35),
				   }
	},
	{
		'id': 'Widow250DrawerRandomizedOpen-area-21-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'drawer_position_high': (.70, .29, -.35),
				   'drawer_position_low': (.50, .21, -.35),
				   }
	},
	{
		'id': 'Widow250DrawerRandomizedOpen-area-10-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'drawer_position_high': (.65, .27, -.35),
				   'drawer_position_low': (.55, .23, -.35),
				   }
	},
	{
		'id': 'Widow250DrawerRandomizedOpen-area-00-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'drawer_position_high': (.60, .25, -.35),
				   'drawer_position_low': (.60, .25, -.35),
				   }
	},




	{
		'id': 'Widow250ButtonPress-area-53-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'reward_type': 'button_press',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'button_position_high': (.85, 0.35, -.37),
				   'button_position_low': (.35, 0.15, -.37),
				   }
	},
	{
		'id': 'Widow250ButtonPress-area-43-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'reward_type': 'button_press',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'button_position_high': (.80, 0.33, -.37),
				   'button_position_low': (.40, 0.17, -.37),
				   }
	},
	{
		'id': 'Widow250ButtonPress-area-32-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'reward_type': 'button_press',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'button_position_high': (.75, 0.31, -.37),
				   'button_position_low': (.45, 0.19, -.37),
				   }
	},
	{
		'id': 'Widow250ButtonPress-area-21-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'reward_type': 'button_press',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'button_position_high': (.70, 0.29, -.37),
				   'button_position_low': (.50, 0.21, -.37),
				   }
	},
	{
		'id': 'Widow250ButtonPress-area-10-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'reward_type': 'button_press',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'button_position_high': (.65, .27, -.37),
				   'button_position_low': (.55, .23, -.37),
				   }
	},
	{
		'id': 'Widow250ButtonPress-area-00-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'reward_type': 'button_press',
				   'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   'load_objects': False,
				   'button_position_high': (.60, .25, -.37),
				   'button_position_low': (.60, .25, -.37),
				   }
	},















	

	{
		'id': 'Widow250GraspEasy-v1',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'target_object': 'cube',
				   'object_names': ('cube',),
				   'object_scales': (0.7,),
				   'load_tray': False,
				   'xyz_action_scale': 0.2,
				   'object_position_high': (.70, .30, -.30),
				   'object_position_low': (.50, .15, -.30),
				   }
	},
	{
		'id': 'Widow250MultiTaskGrasp-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_high': (.68, .25, -.30),
				   'object_position_low': (.53, .15, -.30),
				   'xyz_action_scale': 0.2,
				   }
	},
	{
		'id': 'Widow250MultiObjectGraspTrain-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250MultiObjectEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'possible_objects': GRASP_TRAIN_OBJECTS,
				   'num_objects': 2,

				   'load_tray': False,
				   'object_position_high': (.68, .25, -.30),
				   'object_position_low': (.53, .15, -.30),
				   'xyz_action_scale': 0.2,

				   }
	},
	{
		'id': 'Widow250MultiObjectGraspTest-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250MultiObjectEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',

				   'possible_objects': GRASP_TEST_OBJECTS,
				   'num_objects': 2,

				   'load_tray': False,
				   'object_position_high': (.68, .25, -.30),
				   'object_position_low': (.53, .15, -.30),
				   'xyz_action_scale': 0.2,

				   }
	},
	{
		'id': 'Widow250MultiThreeObjectGraspTrain-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250MultiObjectEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'possible_objects': GRASP_TRAIN_OBJECTS,
				   'num_objects': 3,

				   'load_tray': False,
				   'object_position_high': (.7, .25, -.30),
				   'object_position_low': (.5, .15, -.30),
				   'xyz_action_scale': 0.2,


				   # Next three entries are ignored
				   'object_names': ('beer_bottle', 'gatorade', 'shed'),
				   'object_scales': (0.7, 0.6, 0.8),
				   'object_orientations': (
					   (0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 1, 0)),
				   }
	},
	{
		'id': 'Widow250MultiThreeObjectGraspTest-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250MultiObjectEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',

				   'possible_objects': GRASP_TEST_OBJECTS,
				   'num_objects': 3,

				   'load_tray': False,
				   'object_position_high': (.7, .25, -.30),
				   'object_position_low': (.5, .15, -.30),
				   'xyz_action_scale': 0.2,


				   # Next three entries are ignored
				   'object_names': ('beer_bottle', 'gatorade', 'shed'),
				   'object_scales': (0.7, 0.6, 0.8),
				   'object_orientations': (
						(0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 1, 0)),
				   }
	},
	{
		'id': 'Widow250SingleObjGrasp-v0',
		'entry_point': 'roboverse.envs.widow250:Widow250Env',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_high': (.68, .25, -.30),
				   'object_position_low': (.53, .15, -.30),
				   'xyz_action_scale': 0.2,
				   }
	},
	# Pick and place environments
	{
		'id': 'Widow250PickPlaceEasy-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.6, .2, -.3),
				   'object_position_high': (.6, .2, -.3),

				   'container_name': 'bowl_small',
				   'fixed_container_position': True,

				   }
	},
	{
		'id': 'Widow250PickPlace-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.59, .27, -.30),

				   'container_name': 'bowl_small',


				   }
	},
	{
		'id': 'Widow250PickPlaceMultiObjectMultiContainerTrain-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace'
					   ':Widow250PickPlaceMultiObjectMultiContainerEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'load_tray': False,
				   'num_objects': 2,

				   'possible_objects': PICK_PLACE_TRAIN_OBJECTS,
				   'possible_containers': TRAIN_CONTAINERS,

				   }
	},
	{
		'id': 'Widow250PickPlaceMultiObjectMultiContainerTest-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace'
					   ':Widow250PickPlaceMultiObjectMultiContainerEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'load_tray': False,
				   'num_objects': 2,

				   'possible_objects': PICK_PLACE_TEST_OBJECTS,
				   'possible_containers': TEST_CONTAINERS,
				   }
	},
	{
		'id': 'Widow250PickTray-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.75, .27, -.30),

				   'container_name': 'tray',
				   'fixed_container_position': True,

				   'use_neutral_action': True,
				   'neutral_gripper_open': False,
				   }
	},
	{
		'id': 'Widow250PlaceTray-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.75, .27, -.30),

				   'container_name': 'tray',
				   'fixed_container_position': True,
				   'start_object_in_gripper': True,

				   'use_neutral_action': True,
				   'neutral_gripper_open': False,
				   }
	},
	{
		'id': 'Widow250SinglePutInBowl-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.59, .27, -.30),

				   'container_name': 'bowl_small',


				   }
	},
	{
		'id': 'Widow250SinglePutInBowlRandomBowlPosition-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed',),
				   'object_scales': (0.7,),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.5, .18, -.30),
				   'object_position_high': (.7, .27, -.30),

				   'container_name': 'bowl_small',


				   }
	},
	{
		'id': 'Widow250PutInBowlRandomBowlPosition-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.5, .18, -.30),
				   'object_position_high': (.7, .27, -.30),

				   'container_name': 'bowl_small',


				   }
	},
	{
		'id': 'Widow250MultiObjectPutInBowlRandomBowlPositionTrain-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceMultiObjectEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'possible_objects': PICK_PLACE_TRAIN_OBJECTS,
				   'num_objects': 2,
				   'load_tray': False,
				   'object_position_low': (.5, .18, -.30),
				   'object_position_high': (.7, .27, -.30),

				   'container_name': 'bowl_small',


				   }
	},
	{
		'id': 'Widow250MultiObjectPutInBowlRandomBowlPositionTest-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceMultiObjectEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'possible_objects': PICK_PLACE_TEST_OBJECTS,
				   'num_objects': 2,
				   'load_tray': False,
				   'object_position_low': (.5, .18, -.30),
				   'object_position_high': (.7, .27, -.30),

				   'container_name': 'bowl_small',


				   }
	},
	{
		'id': 'Widow250PutInTray-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.59, .27, -.30),

				   'container_name': 'tray',

				   }
	},
	{
		'id': 'Widow250PutInBox-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.59, .27, -.30),

				   'container_name': 'open_box',

				   }
	},
	{
		'id': 'Widow250PlaceOnCube-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.59, .27, -.30),

				   'container_name': 'cube',

				   }
	},
	{
		'id': 'Widow250PutInPanTefal-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'pan_tefal',

				   }
	},
	{
		'id': 'Widow250PutInPanTefalTestRL1-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('square_rod_embellishment',
									'grill_trash_can'),
				   'object_scales': (0.6, 0.5),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'square_rod_embellishment',

				   'load_tray': False,
				   'container_name': 'pan_tefal',

				   }
	},
	{
		'id': 'Widow250PutInPanTefalFixedTestRL1-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('square_rod_embellishment',
									'grill_trash_can'),
				   'object_scales': (0.6, 0.5),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'square_rod_embellishment',

				   'load_tray': False,
				   'container_name': 'pan_tefal',
				   'fixed_container_position': True,
				   }
	},
	{
		'id': 'Widow250PutInPanTefalTestRL2-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'sack_vase'),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'shed',

				   'load_tray': False,
				   'container_name': 'pan_tefal',
				   }
	},
	{
		'id': 'Widow250PutInPanTefalTestRL3-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('two_handled_vase',
									'thick_wood_chair',),
				   'object_scales': (0.45, 0.4),
				   'object_orientations': ((0, 0, 1, 0), (0, 0, 1, 0)),
				   'target_object': 'two_handled_vase',

				   'load_tray': False,
				   'container_name': 'pan_tefal',

				   }
	},
	{
		'id': 'Widow250PutInPanTefalRL4-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('curved_handle_cup',
									'baseball_cap',),
				   'object_scales': (0.5, 0.5),
				   'object_orientations': ((0, 0.707, 0.707, 0),
										   (0, -0.707, 0.707, 0)),
				   'target_object': 'curved_handle_cup',

				   'load_tray': False,
				   'container_name': 'pan_tefal',
				   }
	},
	{
		'id': 'Widow250PutInTableTop-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'table_top',

				   }
	},
	{
		'id': 'Widow250PutOnTorus-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'torus',
				   }
	},
	{
		'id': 'Widow250PutOnCubeConcave-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'cube_concave',

				   }
	},
	{
		'id': 'Widow250PutOnPlate-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'plate',

				   }
	},
	{
		'id': 'Widow250PutOnHusky-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'husky',

				   }
	},
	{
		'id': 'Widow250PutOnMarbleCube-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'marble_cube',

				   }
	},
	{
		'id': 'Widow250PutOnMarbleCubeTestRL1-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('square_rod_embellishment',
									'grill_trash_can'),
				   'object_scales': (0.6, 0.5),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'square_rod_embellishment',

				   'load_tray': False,

				   'container_name': 'marble_cube',

				   }
	},
	{
		'id': 'Widow250PutOnMarbleCubeTestRL2-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'sack_vase'),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'shed',

				   'load_tray': False,
				   'container_name': 'marble_cube',

				   }
	},
	{
		'id': 'Widow250PutOnMarbleCubeTestRL3-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('two_handled_vase',
									'thick_wood_chair',),
				   'object_scales': (0.45, 0.4),
				   'object_orientations': ((0, 0, 1, 0), (0, 0, 1, 0)),
				   'target_object': 'two_handled_vase',

				   'load_tray': False,
				   'container_name': 'marble_cube',

				   }
	},
	{
		'id': 'Widow250PutOnMarbleCubeTestRL4-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('curved_handle_cup',
									'baseball_cap',),
				   'object_scales': (0.5, 0.5),
				   'object_orientations': ((0, 0.707, 0.707, 0),
										   (0, -0.707, 0.707, 0)),
				   'target_object': 'curved_handle_cup',

				   'load_tray': False,
				   'container_name': 'marble_cube',

				   }
	},
	{
		'id': 'Widow250PutOnMarbleCubeFixedTestRL4-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('curved_handle_cup',
									'baseball_cap',),
				   'object_scales': (0.5, 0.5),
				   'object_orientations': ((0, 0.707, 0.707, 0),
										   (0, -0.707, 0.707, 0)),
				   'target_object': 'curved_handle_cup',

				   'load_tray': False,
				   'container_name': 'marble_cube',
				   'fixed_container_position': True,

				   }
	},
	{
		'id': 'Widow250PutInBasket-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',

				   'load_tray': False,
				   'container_name': 'basket',

				   }
	},
	{
		'id': 'Widow250PutInBasketTestRL1-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('square_rod_embellishment',
									'grill_trash_can'),
				   'object_scales': (0.6, 0.5),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'square_rod_embellishment',

				   'load_tray': False,
				   'container_name': 'basket',

				   }
	},
	{
		'id': 'Widow250PutInBasketTestRL2-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'sack_vase'),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'shed',

				   'load_tray': False,
				   'container_name': 'basket',

				   }
	},
	{
		'id': 'Widow250PutInBasketFixedTestRL2-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'sack_vase'),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': 'shed',

				   'load_tray': False,
				   'container_name': 'basket',
				   'fixed_container_position': True,

				   }
	},
	{
		'id': 'Widow250PutOnCheckerboardTable-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('shed', 'two_handled_vase'),
				   'object_scales': (0.7, 0.6),
				   'target_object': 'shed',
				   'load_tray': False,
				   'object_position_low': (.49, .18, -.30),
				   'object_position_high': (.69, .27, -.30),

				   'container_name': 'checkerboard_table',

				   }
	},
	{
		'id': 'Widow250PutOnCheckerboardTableTestRL3-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('two_handled_vase',
									'thick_wood_chair',),
				   'object_scales': (0.45, 0.4),
				   'object_orientations': ((0, 0, 1, 0), (0, 0, 1, 0)),
				   'target_object': 'two_handled_vase',

				   'load_tray': False,
				   'container_name': 'checkerboard_table',

				   }
	},
	{
		'id': 'Widow250PutOnCheckerboardTableFixedTestRL3-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('two_handled_vase',
									'thick_wood_chair',),
				   'object_scales': (0.45, 0.4),
				   'object_orientations': ((0, 0, 1, 0), (0, 0, 1, 0)),
				   'target_object': 'two_handled_vase',

				   'load_tray': False,
				   'container_name': 'checkerboard_table',
				   'fixed_container_position': True,

				   }
	},
	{
		'id': 'Widow250PutOnCheckerboardTableTestRL4-v0',
		'entry_point': 'roboverse.envs.widow250_pickplace:Widow250PickPlaceEnv',
		'kwargs': {'reward_type': 'pick_place',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('curved_handle_cup',
									'baseball_cap',),
				   'object_scales': (0.5, 0.5),
				   'object_orientations': ((0, 0.707, 0.707, 0),
										   (0, -0.707, 0.707, 0)),
				   'target_object': 'curved_handle_cup',

				   'load_tray': False,
				   'container_name': 'checkerboard_table',

				   }
	},
	# Drawer environments
	{
		'id': 'Widow250DrawerOpen-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   }
	},
	{
		'id': 'Widow250DrawerOpenNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'use_neutral_action': True
				   }
	},
	{
		'id': 'Widow250DrawerGrasp-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'start_opened': True,
				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   }
	},
	{
		'id': 'Widow250DrawerGraspNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'start_opened': True,
				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'use_neutral_action': True
				   }
	},
	{
		'id': 'Widow250DrawerOpenGrasp-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerEnv',
		'kwargs': {'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',
				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'use_neutral_action': True
				   }
	},
	{
		'id': 'Widow250DrawerRandomizedOpen-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   }
	},
	{
		'id': 'Widow250DoubleDrawerOpenNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DoubleDrawerEnv',
		'kwargs': {'drawer_pos': (0.47, 0.2, -.35),
				   'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'use_neutral_action': True
				   }
	},
	{
		'id': 'Widow250DoubleDrawerOpenGraspNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DoubleDrawerEnv',
		'kwargs': {'drawer_pos': (0.47, 0.2, -.35),
				   'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'use_neutral_action': True
				   }
	},
	{
		'id': 'Widow250DoubleDrawerGraspNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DoubleDrawerEnv',
		'kwargs': {'drawer_pos': (0.47, 0.2, -.35),
				   'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'start_opened': True,
				   'use_neutral_action': True
				   }
	},
	{
		'id': 'Widow250DoubleDrawerPickPlaceOpenGraspNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DoubleDrawerEnv',
		'kwargs': {'drawer_pos': (0.47, 0.2, -.35),
				   'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'start_opened': False,
				   'use_neutral_action': True,
				   'blocking_object_in_tray': False,
				   }
	},
	{
		'id': 'Widow250DoubleDrawerCloseOpenNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DoubleDrawerEnv',
		'kwargs': {'drawer_pos': (0.47, 0.2, -.35),
				   'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'start_opened': False,
				   'start_top_opened': True,
				   'use_neutral_action': True,
				   }
	},
	{
		'id': 'Widow250DoubleDrawerCloseOpenGraspNeutral-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DoubleDrawerEnv',
		'kwargs': {'drawer_pos': (0.47, 0.2, -.35),
				   'reward_type': 'grasping',
				   'control_mode': 'discrete_gripper',

				   'object_names': ('ball',),
				   'object_scales': (0.75,),
				   'target_object': 'ball',
				   'load_tray': False,
				   'start_opened': False,
				   'start_top_opened': True,
				   'use_neutral_action': True,
				   }
	},
	{

		'id': 'Widow250DrawerRandomizedOpenTwoObjGrasp-v0',
		'entry_point': 'roboverse.envs.widow250_drawer:Widow250DrawerRandomizedEnv',
		'kwargs': {'reward_type': 'opening',
				   'control_mode': 'discrete_gripper',

				   'object_names': ("shed", "sack_vase"),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'target_object': "shed",
				   'load_tray': False,
				   }
	},
	# Button environments
	{
		'id': 'Widow250ButtonPress-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'control_mode': 'discrete_gripper',
				   'load_tray': False,
				   }
	},
	{
		'id': 'Widow250ButtonPressTwoObjGrasp-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'control_mode': 'discrete_gripper',

				   'object_names': ("shed", "sack_vase"),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'object_position_high': (.75, .25, -.30),
				   'object_position_low': (.6, .1, -.30),
				   'target_object': "shed",
				   'load_tray': False,
				   }
	},
	{
		'id': 'Widow250RandPosButtonPressTwoObjGrasp-v0',
		'entry_point': 'roboverse.envs.widow250_button:Widow250ButtonEnv',
		'kwargs': {'control_mode': 'discrete_gripper',
				   'button_pos_low': (0.5, 0.25, -.34),
				   'button_pos_high': (0.55, 0.15, -.34),

				   'object_names': ("shed", "sack_vase"),
				   'object_scales': (0.6, 0.6),
				   'object_orientations': ((0, 0, 1, 0), (0, 0.707, 0.707, 0)),
				   'object_position_high': (.75, .25, -.30),
				   'object_position_low': (.65, .1, -.30),
				   'target_object': "shed",
				   'load_tray': False,
				   }
	},
)


def register_environments():
	for env in ENVIRONMENT_SPECS:
		gym.register(**env)

	gym_ids = tuple(
		environment_spec['id']
		for environment_spec in ENVIRONMENT_SPECS)

	return gym_ids


def make(env_name, *args, **kwargs):
	env = gym.make(env_name, *args, **kwargs)
	return env
