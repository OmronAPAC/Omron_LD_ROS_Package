# om_aiv - ROS Packages for Omron Mobile Robot
![omron ld robot](https://assets.omron.com/m/438d82ed579472a4/Portrait_M-Mobile_Robot_Product-News-jpg.jpg "omron ld robot")
### List of packages
#### 1. om_aiv_util
robot status commands 

#### 2. om_aiv_util_em
enterprise manager commands 

#### 3. om_aiv_navigation
navigation commands like dock, undock, dotask move , patrol

### ROS Package Diagram
![ROS Diagram](https://user-images.githubusercontent.com/8951670/70422919-83b8ac00-1aa7-11ea-82f9-acbde1137f7d.png)


### Prerequisites
```
Ubuntu 18.04
ROS Melodic 
```
### Compatibility

Tested on ARAM 4.9.27 and FLOW 1.0.16 to be fully compatible

### Installation

This readme assumes that you have installed catkin and sourced your environment. If you installed catkin via apt-get for ROS melodic, your command would look like this:
```
source /opt/ros/melodic/setup.bash
```
Clone the repository into the your home directory:
```
git clone https://github.com/tthmatt/Omron_LD_ROS_Package.git
```
Your workspace hierarchy should look like this:

![workspace hierarchy](https://user-images.githubusercontent.com/8951670/70413338-1d755e80-1a92-11ea-8640-88861fa8692b.png)


Use catkin build to compile and make sure to source the workspace:
```
cd ~/Omron_LD_ROS_Package

catkin clean

catkin build

source ~/Omron_LD_ROS_Package/devel/setup.bash
```
### Initial Configuration
Specify the robot ip address, name(for multiple robots) and enterprise manager ip address when running the launch file from the command line as a command line argument, for example:

for one robot: roslaunch om_aiv_util 1robot.launch ip:=168.3.201.123 

for multiple robots: roslaunch om_aiv_util multiple_robots.launch ip:=168.3.201.123 name:=robot1 
(client files have to be modified with the correct service/action namespace. For an example looks at ~/Omron_LD_ROS_Package/om_aiv_util/scripts/multiple_robots_example_client.py)

### Usage
For one robot:
```
roslaunch om_aiv_util 1robot.launch ip:=<ip address of robot>
```
For multiple robots(run this command once for each robot):
```
roslaunch om_aiv_util multiple_robots.launch ip:=<ip address of robot> name:=<robot name> 
```
For Enterprise Manager:
```
roslaunch om_aiv_util_em em_robot.launch ip:=<ip address of enterprise manager>
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

In doTask_action_client.py in ~/Omron_LD_ROS_Package/src/om_aiv_navigation/scripts set the goal.goal_goal = "move 1000". Then in a terminal window run(goal set in client program):
```
rosrun om_aiv_navigation doTask_action_client.py
```
![example_action](https://user-images.githubusercontent.com/8951670/73995595-184e6600-4994-11ea-8de1-998a87545194.png)

To view services:
```
rosservice list
```
Command arguments are to be input as command line arguments. For example, command arclSendText:
```
rosrun om_aiv_util arclSendText_client.py text
```
To run another service command, example analogInputList:
```
rosrun om_aiv_util analogInputList_client.py
```
To clear an application fault with fault name as the argument which in this case is "fault":
```
rosrun om_aiv_util applicationFaultClear_client.py <fault name> 
```
![example_ros_service_command](https://user-images.githubusercontent.com/8951670/73994608-1f27a980-4991-11ea-8582-019bdad564fa.png)

### Code Explanation
ld_topic_publisher.py in ~/Omron_LD_ROS_Package/src/om_aiv_util/scripts and em_topic_publisher.py in ~ld_ROS/src/om_aiv_util_em/scripts: 

command = actual command to be sent

command2 = end of required data that is sent back from arcl. Example: "End of End of ApplicationFaultQuery"

command3 = required data to be printed out. Example: "ApplicationFaultQuery:......"

text = what to print if required data is not received. Example: "No Faults"

### Limitations
ROS is not able to have access to robot hardware, therefore map creation and scanning is not possible. This ROS package makes use of ARCL to send commands and receive data from the robot. 

### Known Issues and Bugs
Service call failed: unable to connect to service: remote error reported: request from \[/unnamed]:

### References
ARCL Reference Guide, 18448-000 Rev A, Updated: 1/19/2017 which is included in root directory of this workspace
