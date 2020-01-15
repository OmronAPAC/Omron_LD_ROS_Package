#include <ros/ros.h>
#include <sensor_msgs/JointState.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/Quaternion.h>
#include <tf/transform_broadcaster.h>
#include <om_aiv_util/Location.h>
#include <string>

// Global values
double pos_x;
double pos_y;
double pos_z;
geometry_msgs::Quaternion theta;

const int JOINTS_SIZE = 7;
const std::string HEAD_FRAME = "/pose";
const std::string CHILD_FRAME = "/base_link";
const std::string MAIN_BODY_JOINT = "main_body_to_base";
const std::string RIGHT_WHEEL_JOINT = "right_wheel_joint";
const std::string LEFT_WHEEL_JOINT = "left_wheel_joint";
const std::string RIGHT_FR_WHEEL_JOINT = "right_front_small_wheel_joint";
const std::string LEFT_FR_WHEEL_JOINT = "left_front_small_wheel_joint";
const std::string RIGHT_BK_WHEEL_JOINT = "left_back_small_wheel_joint";
const std::string LEFT_BK_WHEEL_JOINT = "right_back_small_wheel_joint";

// Function prototypes
void pose_cb(const om_aiv_util::LocationConstPtr& pose_msg);

int main(int argc, char** argv) 
{
    ros::init(argc, argv, "joints_publisher");
    ros::NodeHandle nh;
    ros::Publisher joint_pub = nh.advertise<sensor_msgs::JointState>("joint_states", 1);
    ros::Subscriber pose_sub = nh.subscribe<om_aiv_util::Location>("ldarcl_status_location", 10, pose_cb);
    tf::TransformBroadcaster broadcaster;
    ros::Rate loop_rate(50);

    pos_x = 0;
    pos_y = 0;
    pos_z = 0;
    theta = geometry_msgs::Quaternion();
    theta.w = 1.0;

    // Joint states
    double main_body_to_base_pos = 0;
    double right_wheel_joint_pos = 0;
    double left_wheel_joint_pos = 0;
    double right_front_small_wheel_joint_pos = 0;
    double left_front_small_wheel_joint_pos = 0;
    double left_back_small_wheel_joint_pos = 0;
    double right_back_small_wheel_joint_pos = 0;
    double angle = 0;
    double trans_x = 0;

    // Messages to publish
    sensor_msgs::JointState joint_state;
    geometry_msgs::TransformStamped pose_trans;
    pose_trans.header.frame_id = HEAD_FRAME;
    pose_trans.child_frame_id = CHILD_FRAME;
    joint_state.name.resize(JOINTS_SIZE);
    joint_state.position.resize(JOINTS_SIZE);
    joint_state.name[0] = MAIN_BODY_JOINT;
    joint_state.name[1] = RIGHT_WHEEL_JOINT;
    joint_state.name[2] = LEFT_WHEEL_JOINT;
    joint_state.name[3] = RIGHT_FR_WHEEL_JOINT;
    joint_state.name[4] = LEFT_FR_WHEEL_JOINT;
    joint_state.name[5] = RIGHT_BK_WHEEL_JOINT;
    joint_state.name[6] = LEFT_BK_WHEEL_JOINT;

    while (ros::ok()) 
    {
        // Update joints
        joint_state.header.stamp = ros::Time::now();
        joint_state.position[0] = main_body_to_base_pos;
        joint_state.position[1] = right_wheel_joint_pos;
        joint_state.position[2] = left_wheel_joint_pos;
        joint_state.position[3] = right_front_small_wheel_joint_pos;
        joint_state.position[4] = left_front_small_wheel_joint_pos;
        joint_state.position[5] = left_back_small_wheel_joint_pos;
        joint_state.position[6] = right_back_small_wheel_joint_pos;

        // update transform
        pose_trans.header.stamp = ros::Time::now();
        pose_trans.transform.translation.x = pos_x;
        pose_trans.transform.translation.y = pos_y;
        pose_trans.transform.translation.z = pos_z;
        pose_trans.transform.rotation = theta;

        // Update transforms
        // NOTE: The joints states does not change at the moment.
        // TODO: Calculate the next joint state.
        joint_pub.publish(joint_state);
        broadcaster.sendTransform(pose_trans);

        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}

/**
 * @brief Callback function for receiving Location message.
 * 
 * @param pose_msg Location message data received.
 */
void pose_cb(const om_aiv_util::LocationConstPtr& pose_msg)
{
    // The values are in millimeters, convert to meters.
    pos_x = pose_msg->x / 1000.0; 
    pos_y = pose_msg->y / 1000.0; 
    pos_z = 0;

    // Angle is in degree, convert to radians.
    double rad = pose_msg->theta;
    rad = rad * M_PI / 180;
    if (rad < 0) rad += (2 * M_PI);
    theta = tf::createQuaternionMsgFromYaw(rad);

    ROS_INFO("pos_x: %lf", pos_x);
    ROS_INFO("pos_y: %lf", pos_y);
    ROS_INFO("pos_z: %lf", pos_z);
    ROS_INFO("rad  : %lf", rad);
    ROS_INFO("q_x  : %lf", theta.x);
    ROS_INFO("q_y  : %lf", theta.y);
    ROS_INFO("q_z  : %lf", theta.z);
    ROS_INFO("q_w  : %lf", theta.w);
}