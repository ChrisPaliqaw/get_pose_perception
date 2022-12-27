from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
    # ros2 run simple_grasping basic_grasping_perception_node --ros-args -p debug_topics:=true
        Node(
            package='simple_grasping',
            executable='basic_grasping_perception_node',
            name='basic_grasping_perception_node',
            output='screen',
            parameters=[{
                "debug_topics": True
            }]
        ),
        Node(
            package='get_pose_perception',
            executable='get_pose_client',
            name='get_pose_client',
            output='screen'
        )
    ])
