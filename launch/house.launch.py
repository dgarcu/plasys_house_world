import os
import sys

import launch
import launch_ros.actions
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
  world_id = os.environ.get('WORLD_ID', "plasys_house")
  world = os.path.join(get_package_share_directory('plasys_house_world'),
    'worlds', world_id, world_id + '.world')

  gazebo = launch.actions.IncludeLaunchDescription(
    launch.launch_description_sources.PythonLaunchDescriptionSource(
      os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')),
    launch_arguments={
      'gui': launch.substitutions.LaunchConfiguration('gui')
    }.items()
  )

  ld = launch.LaunchDescription([
    launch.actions.DeclareLaunchArgument(
      'world',
      default_value=[world, ''],
      description='SDF world file'),
    launch.actions.DeclareLaunchArgument(
      name='gui',
      default_value='false'
    ),
    gazebo
  ])
  return ld


if __name__ == '__main__':
  generate_launch_description()
