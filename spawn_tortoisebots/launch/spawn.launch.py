from ament_index_python.packages import get_package_share_directory
import os
import launch
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # Get the package share directory for source (not installed) path
    pkg_share = get_package_share_directory('tortoisebot_description')

    # Path to the world file
    world_path = os.path.join(get_package_share_directory('tortoisebot_gazebo'), 'worlds/room2.sdf')

    # Path to the robot xacro file (using source path)
    xacro_file_path = os.path.join(pkg_share, 'models', 'urdf', 'tortoisebot_simple.xacro')

    # Verify the file exists
    if not os.path.exists(xacro_file_path):
        raise FileNotFoundError(f"Xacro file not found at {xacro_file_path}")

    # Launch configuration for simulation time
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Robot description command with namespace substitution
    def robot_description_command(namespace):
        return launch.substitutions.Command([
            'xacro ', xacro_file_path, ' namespace:=', namespace
        ])

    # Spawn the first TortoiseBot in namespace 'robot1'
    tortoisebot1 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_tortoisebot1',
        namespace='robot1',
        arguments=[
            '-entity', 'tortoisebot1',
            '-topic', '/robot1/robot_description',
            '-x', '0', '-y', '0', '-z', '0'
        ],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # Spawn the second TortoiseBot in namespace 'robot2'
    tortoisebot2 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_tortoisebot2',
        namespace='robot2',
        arguments=[
            '-entity', 'tortoisebot2',
            '-topic', '/robot2/robot_description',
            '-x', '2', '-y', '2', '-z', '0'
        ],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    # Spawn the third TortoiseBot in namespace 'robot3'
    tortoisebot3 = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_tortoisebot3',
        namespace='robot3',
        arguments=[
            '-entity', 'tortoisebot3',
            '-topic', '/robot3/robot_description',
            '-x', '-2', '-y', '-2', '-z', '0'
        ],
        parameters=[{'use_sim_time': use_sim_time}]
    )

    return launch.LaunchDescription([
        # Declare the use_sim_time argument
        launch.actions.DeclareLaunchArgument(
            name='use_sim_time', default_value='True',
            description='Flag to enable use_sim_time'
        ),

        # Launch Gazebo with the specified world
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path],
            output='screen'
        ),

        # Spawn the TortoiseBot entities in namespaces
        tortoisebot1,
        tortoisebot2,
        tortoisebot3,
    ])
