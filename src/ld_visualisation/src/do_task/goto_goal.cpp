#include <ros/ros.h>
#include <interactive_markers/interactive_marker_server.h>

void button_cb(const visualization_msgs::InteractiveMarkerFeedbackConstPtr& feedback)
{
  ROS_INFO_STREAM(feedback->marker_name << " at " << feedback->pose.position.x << ", " << feedback->pose.position.y);
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "buttons");
  
  interactive_markers::InteractiveMarkerServer sever("buttons");

  visualization_msgs::InteractiveMarker int_button;
  int_button.header.frame_id = "/pose";
  int_button.header.stamp = ros::Time::now();
  int_button.name = "click_button";
  int_button.description = "Clicking button";

  visualization_msgs::Marker button;
  button.type = visualization_msgs::Marker::CUBE;
  button.scale.x = 0.5;
  button.scale.y = 0.5;
  button.scale.z = 0.5;
  button.color.a = 1.0;

  return 0;
}