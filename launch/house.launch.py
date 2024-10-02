import os

import launch
from ament_index_python.packages import get_package_share_directory
from launch.actions import ExecuteProcess, SetEnvironmentVariable


def generate_launch_description():
    package_dir = get_package_share_directory('plasys_house_world')
    world = os.path.join(package_dir, 'worlds', 'plasys_house', 'plasys_house.world')

    model_path = os.path.join(package_dir, 'models')

    gazebo_server_cmd_line = [
        'gz', 'sim', '-r', '-v4', world]

    gazebo = ExecuteProcess(
        cmd=gazebo_server_cmd_line, output='screen')

    ld = launch.LaunchDescription([
        SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', model_path),
        launch.actions.DeclareLaunchArgument(
            'world',
            default_value=[world, ''],
            description='SDF world file'),
        gazebo
        ])

    return ld


if __name__ == '__main__':
    generate_launch_description()
