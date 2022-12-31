# get_pose_perception
Part 5 ROS2 Perception of the Phase 2 project of The Construct's Robotics Developer Master Class

Same preamble as part 4

rviz shell
```
rviz2
```
Then use the rviz configuration file `perception_config.rviz` in `/home/user`

Clone the repository that contains the perception node you'll use:

```
cd ~/ros2_ws/src
git clone https://bitbucket.org/theconstructcore/perception_ros2.git
cd ..
source /opt/ros/foxy/setup.bash
colcon build
source install/setup.bash
```

## Option 1: Run scripts individually
`percept server` shell
```
cd ~/ros2_ws
source /opt/ros/foxy/setup.bash
colcon build
source install/setup.bash
ros2 run simple_grasping basic_grasping_perception_node --ros-args -p debug_topics:=true
```
`percept goal` shell
```
cd ~/ros2_ws
colcon build
source ~/ros2_ws/install/setup.bash
ros2 action list
ros2 action send_goal /find_objects grasping_msgs/action/FindGraspableObjects "{plan_grasps: false}"
```
NOTE: first time I sent a goal, I got in the `perception` shell
```
[ERROR] [1662543639.522423037] [basic_grasping_perception]: Failed to get camera data in alloted time.
```
and I got in the `percept goal` 
```
Goal finished with status: ABORTED
```
can echo in `ros2 info`
```
ros2 topic echo /wrist_rgbd/depth/points --qos-durability=volatile
```
run the client script in `percept goal`
```
cd ~/ros2_ws
cd ..
colcon build
. install/setup.bash
ros2 run get_pose_perception get_pose_client
```
Note that you might have to try several times, for instance
```
user:~/ros2_ws$ ros2 run get_pose_perception get_pose_client
[INFO] [1662602336.573544493] [get_pose_client]: Sending goal
[INFO] [1662602336.574860683] [get_pose_client]: Goal accepted by server, waiting for result
[ERROR] [1662602339.586497416] [get_pose_client]: Goal was aborted
user:~/ros2_ws$ ros2 run get_pose_perception get_pose_client
[INFO] [1662602351.773191872] [get_pose_client]: Sending goal
[INFO] [1662602351.775089598] [get_pose_client]: Goal accepted by server, waiting for result
[INFO] [1662602354.399966712] [get_pose_client]: Result received
[INFO] [1662602354.400847967] [get_pose_client]: X: 0.328123
[INFO] [1662602354.401105959] [get_pose_client]: Y: 0.281085
```

## Option 2: Run single script for perception server and client
In the `perception node` shell
```
ros2 launch get_pose_perception get_pose_client.launch.py
```
