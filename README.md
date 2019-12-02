# om_aiv - ROS Packages for Omron Mobile Robot

![omron ld robot](https://d2t1xqejof9utc.cloudfront.net/screenshots/pics/440c4d03c225fbe74adf238d73ed8f00/large.png "omron ld robot")

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
### Compatibility

Tested on ARAM 4.9.27 and ARAM 5.0.12 to be fully compatible

### Installation

This readme assumes that you have installed catkin and sourced your environment. If you installed catkin via apt-get for ROS melodic, your command would look like this:
```
source /opt/ros/melodic/setup.bash
```
First create a catkin workspace and name it ld_ROS:
```
mkdir -p ~/ld_ROS/src

cd ~/ld_ROS/
```
Then clone the repository into the src/ folder:
```
git clone https://github.com/tthmatt/Omron_LD_ROS_Package.git
```
Your workspace hierarchy should look like this:

![ld_ROS workspace hierarchy](https://user-images.githubusercontent.com/8951670/69391247-2c77b500-0d0d-11ea-86ba-6e29d512abf4.png)

Make sure to source the correct setup file according to your workspace hierarchy, then use catkin build to compile:
```
source ~/ld_ROS/devel/setup.bash

catkin build
```
### Initial Configuration
Specify robot ip address, name and enterprise manager ip address when running the launch file from the command line as a command line argment, for example:
roslaunch om_aiv_util robot1.launch ip:=168.3.201.123 name:=robot1

### Usage
```
roslaunch om_aiv_util robot1.launch ip:=<ip address of robot> name:=<robot name>
roslaunch om_aiv_util_em em_robot.launch ip:=<ip address of robot>

```

View the topics published and do a rostopic echo (topic name) to view the data:
```
rostopic list

rostopic echo /(rostopic name)
```
![rostopic list](https://user-images.githubusercontent.com/8951670/69392258-68f8e000-0d10-11ea-8597-a2c577feb3b5.png)

For example to view the battery level of the robot:

![rostopic echo example](https://user-images.githubusercontent.com/8951670/69392375-cdb43a80-0d10-11ea-8da4-8e39f4f72525.png)

To run navigation commands, example to move the robot 1000mm:
```
rosrun om_navigation doTask_action_client.py move 1000
```
### Known Issues and Bugs
Service call failed: unable to connect to service: remote error reported: request from \[/unnamed]:
