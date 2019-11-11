# om_aiv - ROS Packages for Omron Mobile Robot

#### om_aiv_util
robot status commands 

#### om_aiv_navigation
navigation commands like dock, undock, dotask move , patrol



### Prerequisites
```
Ubuntu 18.04
ROS Melodic 
```

### Installing
```
git clone https://github.com/tthmatt/Omron_LD_ROS_Package.git
catkin build
```
### Initial Configuration

Specify robot ip address and port number in /ld_ROS/src/om_aiv_util/launch/robot1.launch




### Usage
```
roslaunch om_aiv_util ldarcl_status.launch
roslaunch om_aiv_navigation ld_navigation.launch
```
```
rostopic list
```
View the topics published and do a rostopic echo (topic name) to view the data

To run navigation commands example to move the robot 1000mm
```
rosrun om_navigation doTask_action_client.py move 1000
```
