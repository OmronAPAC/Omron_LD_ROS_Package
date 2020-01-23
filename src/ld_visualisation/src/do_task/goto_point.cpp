#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/Quaternion.h>
#include <tf/transform_datatypes.h>
#include <om_aiv_util/ArclApi.h>

om_aiv_util::ArclApi req_msg;
ros::ServiceClient arcl_api_client;

const std::string API_SRV_NAME = "arcl_api_service";
const std::string GOTO_CMD = "doTask gotoPoint ";
const std::string LINE_ID = "Doing task gotoPoint ";
const std::string POINT_TOPIC = "/goto_point_goal";

void point_cb(const geometry_msgs::PoseStampedConstPtr& point_msg);

int main(int argc, char** argv)
{
    ros::init(argc, argv, "goto_point");
    ros::NodeHandle nh;
    ros::Rate rate(10);

    ros::Subscriber point_sub = nh.subscribe<geometry_msgs::PoseStamped>(POINT_TOPIC, 10, point_cb);
    arcl_api_client = nh.serviceClient<om_aiv_util::ArclApi>(API_SRV_NAME);

    ros::spin();

    return 0;
}

/**
 * @brief Callback function when the point to go to is published on topic.
 * 
 * @param point_msg Message containing the x, y and theta of the goto point.
 */
void point_cb(const geometry_msgs::PoseStampedConstPtr& point_msg)
{
    // Get the pose published.
    double dummy_roll;
    double dummy_pitch;
    double theta;
    int x = point_msg->pose.position.x * 1000;
    int y = point_msg->pose.position.y * 1000;
    tf::Quaternion tf_quat;
    tf::quaternionMsgToTF(point_msg->pose.orientation, tf_quat);
    tf::Matrix3x3(tf_quat).getRPY(dummy_roll, dummy_pitch, theta);
    theta *= 57.29577951; // Convert to degree
    if (theta > 180) theta -= 360;
    int theta_int = (int)theta;

    req_msg.request.command = GOTO_CMD;
    req_msg.request.line_identifier = LINE_ID;
    std::string vals_str = std::to_string(x) + " " + std::to_string(y) + " " + std::to_string(theta_int);
    req_msg.request.command += vals_str;
    req_msg.request.line_identifier += vals_str;
    // Send the request to ARCL api server.
    if (arcl_api_client.call(req_msg))
    {
        if (req_msg.response.response.find(LINE_ID) != std::string::npos)
        {
            ROS_INFO("%s - Executing %s", ros::this_node::getName().c_str(), req_msg.request.command.c_str());
        }
        else
        {
            ROS_ERROR("%s - gotoPoint task failed, response: %s", 
                ros::this_node::getName().c_str(), req_msg.response.response.c_str());
        }
    }
    else
    {
        ROS_ERROR("%s - Failed to call %s service for gotoPoint task", 
            ros::this_node::getName().c_str(), API_SRV_NAME.c_str());
    }
}