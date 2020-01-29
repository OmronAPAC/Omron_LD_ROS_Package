#include <ros/ros.h>
#include <visualization_msgs/Marker.h>
#include <visualization_msgs/MarkerArray.h>
#include <geometry_msgs/Quaternion.h>
#include <std_msgs/String.h>
#include <tf/transform_broadcaster.h>
#include <om_aiv_util/ArclApi.h>
#include <om_aiv_util/ArclListen.h>

// Configurable values.
std::string head_frame;
std::string goals_vis_topic;
float goals_a_clr;
float goals_r_clr;
float goals_g_clr;
float goals_b_clr;
float goal_texts_a_clr;
float goal_texts_r_clr;
float goal_texts_g_clr;
float goal_texts_b_clr;
int32_t goals_id = 0;
int32_t goal_texts_id = 0;

// Non configurable values.
const std::string GOALS_NS = "goals";
const std::string GOALS_TEXT_NS = "goal_texts";
const std::string GOAL_RESP_H = "Goal";
const std::string COORD_H = "MapObjectInfoCoord: ";
const std::string GOAL_CMD = "MapObjectInfo ";
const std::string GOALS_LIST_END = "End of MapObjectInfo";
const std::string API_SRV_NAME = "arcl_api_service";
const std::string ALL_GOALS_TOPIC = "ldarcl_all_goals";
const double GOALS_X_SCALE = 0.5;
const double GOALS_Y_SCALE = 0.1;
const double GOALS_Z_SCALE = 0.07;
const double GOAL_TEXT_X_SCALE = 0.1;
const double GOAL_TEXT_Y_SCALE = 0.1;
const double GOAL_TEXT_Z_SCALE = 0.5;
const double GOAL_TEXT_HEIGHT_Z = 0.5;

// Names for all config parameters.
const std::string HEAD_FRAME_PARAM = "head_frame";
const std::string GOALS_VIS_TOPIC = "goals_vis_topic";
const std::string GOALS_A_CLR_PARAM = "goals_a_colour";
const std::string GOALS_R_CLR_PARAM = "goals_r_colour";
const std::string GOALS_G_CLR_PARAM = "goals_g_colour";
const std::string GOALS_B_CLR_PARAM = "goals_b_colour";
const std::string GOAL_TEXTS_A_CLR_PARAM = "goal_texts_a_colour";
const std::string GOAL_TEXTS_R_CLR_PARAM = "goal_texts_r_colour";
const std::string GOAL_TEXTS_G_CLR_PARAM = "goal_texts_g_colour";
const std::string GOAL_TEXTS_B_CLR_PARAM = "goal_texts_b_colour";

// Global variables
std::vector<std::string> goals_list;

// Function prototypes
void req_goals_coord(
    ros::ServiceClient& arcl_api_client, 
    om_aiv_util::ArclApi& goals_info_req, 
    visualization_msgs::MarkerArray& goals,
    visualization_msgs::MarkerArray& goals_text,
    visualization_msgs::Marker one_goal,
    visualization_msgs::Marker one_goal_text);

void all_goals_cb(const std_msgs::StringConstPtr& msg);

int main(int argc, char** argv)
{
    ros::init(argc, argv, "goals_marker");
    ros::NodeHandle nh;
    ros::Rate rate(0.1);

    nh.param<std::string>(HEAD_FRAME_PARAM, head_frame, "/pose");
    nh.param<std::string>(GOALS_VIS_TOPIC, goals_vis_topic, "visualization_marker_array");
    nh.param<float>(GOALS_A_CLR_PARAM, goals_a_clr, 1.0);
    nh.param<float>(GOALS_R_CLR_PARAM, goals_r_clr, 0);
    nh.param<float>(GOALS_G_CLR_PARAM, goals_g_clr, 1.0);
    nh.param<float>(GOALS_B_CLR_PARAM, goals_b_clr, 0);
    nh.param<float>(GOAL_TEXTS_A_CLR_PARAM, goal_texts_a_clr, 1.0);
    nh.param<float>(GOAL_TEXTS_R_CLR_PARAM, goal_texts_r_clr, 0);
    nh.param<float>(GOAL_TEXTS_G_CLR_PARAM, goal_texts_g_clr, 1.0);
    nh.param<float>(GOAL_TEXTS_B_CLR_PARAM, goal_texts_b_clr, 0);

    ros::Publisher goals_pub = nh.advertise<visualization_msgs::MarkerArray>(goals_vis_topic, 10);
    ros::ServiceClient arcl_api_client = nh.serviceClient<om_aiv_util::ArclApi>(API_SRV_NAME);
    ros::Subscriber all_goals_sub = nh.subscribe<std_msgs::String>(ALL_GOALS_TOPIC, 10, all_goals_cb);

    // TODO: ARROW is used wrongly, read the documentation!
    // Create MarkerArray for all goals Markers. Each goal is one Marker object that is of ARROW type.
    // Cannot use Marker.points, it works differently from POINTS type.
    // ALSO LOOK AT getGoals, think its a simpler way to get goal coordinates.
    visualization_msgs::MarkerArray goals;
    visualization_msgs::Marker one_goal;
    visualization_msgs::MarkerArray goals_text;
    visualization_msgs::Marker one_goal_text;
    one_goal.header.frame_id = head_frame;
    one_goal.ns = GOALS_NS;
    one_goal.action = visualization_msgs::Marker::MODIFY;
    one_goal.id = goals_id;
    one_goal.type = visualization_msgs::Marker::ARROW;
    one_goal.scale.x = GOALS_X_SCALE;
    one_goal.scale.y = GOALS_Y_SCALE;
    one_goal.scale.z = GOALS_Z_SCALE;
    one_goal.color.a = goals_a_clr;
    one_goal.color.r = goals_r_clr;
    one_goal.color.g = goals_g_clr;
    one_goal.color.b = goals_b_clr;
    one_goal_text.header.frame_id = head_frame;
    one_goal_text.ns = GOALS_TEXT_NS;
    one_goal_text.action = visualization_msgs::Marker::MODIFY;
    one_goal_text.pose.orientation.w = 1.0;
    one_goal_text.id = goal_texts_id;
    one_goal_text.type = visualization_msgs::Marker::TEXT_VIEW_FACING;
    one_goal_text.pose.position.z = GOAL_TEXT_HEIGHT_Z;
    one_goal_text.scale.z = GOAL_TEXT_Z_SCALE;
    one_goal_text.color.a = goals_a_clr;
    one_goal_text.color.r = goals_r_clr;
    one_goal_text.color.g = goals_g_clr;
    one_goal_text.color.b = goals_b_clr;

    // Create the service request messages to get goals data.
    om_aiv_util::ArclListen goals_list_req;
    om_aiv_util::ArclApi goals_info_req;
    goals_list_req.request.resp_header = GOAL_RESP_H;
    goals_info_req.request.line_identifier = GOALS_LIST_END;


    while (ros::ok())
    {
        req_goals_coord(arcl_api_client, goals_info_req, goals, goals_text, one_goal, one_goal_text);
        for (int i = 0; i < goals.markers.size(); i++)
        {
            goals.markers[i].header.stamp = ros::Time::now();
        }

        goals_pub.publish(goals);
        goals_pub.publish(goals_text);
        
        ros::spinOnce();
        rate.sleep();
    }

    return 0;
}

void req_goals_coord(
    ros::ServiceClient& arcl_api_client, 
    om_aiv_util::ArclApi& goals_info_req, 
    visualization_msgs::MarkerArray& goals,
    visualization_msgs::MarkerArray& goals_text,
    visualization_msgs::Marker one_goal,
    visualization_msgs::Marker one_goal_text)
{
    // Request for every known goal's coordinates.
    goals.markers.clear();
    goals_id = 0;
    goal_texts_id = 0;
    std::string cmd = GOAL_CMD;
    for (int i = 0; i < goals_list.size(); i++)
    {
        goals_info_req.request.command = cmd + goals_list[i];

        // Send request to ROS service.
        if (arcl_api_client.call(goals_info_req))
        {
            std::string info_resp = goals_info_req.response.response;
            std::string::size_type pos = info_resp.find(COORD_H);
            if (pos != std::string::npos)
            {
                // We have found the line containing the coordinates, collect them.
                std::string::size_type end = info_resp.find("\r\n", pos);
                std::string val_str = info_resp.substr(pos+COORD_H.size(), end);
                std::istringstream val_iss(val_str);
                std::string dummy;
                double x, y, theta;
                if (!(val_iss >> dummy >> x >> y >> theta)) ROS_ERROR("Error reading goal coordinates");
                x /= 1000.0;
                y /= 1000.0;
                one_goal.pose.position.x = x; // Convert from mm to metre.
                one_goal.pose.position.y = y;
                one_goal.pose.position.z = 0;
                if (theta < 0) theta += 360.0;
                theta = theta * 0.01745329252; // Convert lineto radian
                one_goal.pose.orientation = tf::createQuaternionMsgFromYaw(theta);
                one_goal.id = goals_id++;
                goals.markers.push_back(one_goal);
                one_goal_text.pose.position.x = x;
                one_goal_text.pose.position.y = y;
                one_goal_text.text = goals_list[i];
                one_goal_text.id = goal_texts_id++;
                goals_text.markers.push_back(one_goal_text);
            }
        }
        else
        {
            ROS_ERROR("%s - Failed to call %s service for goal info.", 
                ros::this_node::getName().c_str(), API_SRV_NAME.c_str());
        }
    }
}

/**
 * @brief Callback function for subscribing to list of goals.
 * 
 * @param msg Message containing the string of list of goals.
 */
void all_goals_cb(const std_msgs::StringConstPtr& msg)
{
    goals_list.clear();
    std::string raw_resp = msg->data;
    std::istringstream iss(raw_resp);
    // Retrieve all goals' name.
    std::string name;
    while (iss >> name)
    {
        goals_list.push_back(name);
    }
}