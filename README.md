# om_aiv - ROS Packages for Omron Mobile Robot

#### om_aiv_util
robot status commands 

#### om_aiv_util_em
enterprise manager commands 

#### om_aiv_navigation
navigation commands like dock, undock, dotask move , patrol



### Prerequisites
```
Ubuntu 18.04
ROS Melodic 
```

### Installation

First set up a catkin workspace.
Then clone the repository into the src/ folder:
```
git clone https://github.com/tthmatt/Omron_LD_ROS_Package.git
```
Make sure to source the correct setup file according to your workspace hierarchy, then use catkin build to compile:
```
catkin build
```
### Initial Configuration
For a single robot:

Specify robot ip address and port number in /ld_ROS/src/om_aiv_util/launch/robot1.launch

For 2 robots:

WIP


### Usage
```
roslaunch om_aiv_util robot1.launch
roslaunch om_aiv_navigation robot1.launch
```

View the topics published and do a rostopic echo (topic name) to view the data:
```
rostopic list
```
```
rostopic echo /(rostopic name)
```

To run navigation commands, example to move the robot 1000mm:
```
rosrun om_navigation doTask_action_client.py move 1000
```
