from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    robot_desc = Command([
        'xacro ',
        PathJoinSubstitution([
             FindPackageShare('my_simple_arm'),
             'urdf',
             'simple_arm.urdf.xacro'
        ])
    ])

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_desc}],
            output='screen'
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        ExecuteProcess(
            cmd=[
                'rviz2', '-d',
                PathJoinSubstitution([
                    FindPackageShare('my_simple_arm'),
                    'rviz',
                    'arm.rviz'
                ])
            ],
            output='screen'
        )
    ])
