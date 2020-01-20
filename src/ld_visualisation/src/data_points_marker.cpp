#include <ros/ros.h>
#include <ros/package.h>
#include <visualization_msgs/Marker.h>
#include <sensor_msgs/LaserScan.h>
#include <om_aiv_util/ArclApi.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

// Configurable values.
std::string PACK_NAME;
std::string MAP_NAME;
std::string HEAD_FRAME;
std::string VIS_TOPIC;
std::string rng_device;
float POINTS_A_CLR;
float POINTS_R_CLR;
float POINTS_G_CLR;
float POINTS_B_CLR;
float LINES_A_CLR;
float LINES_R_CLR;
float LINES_G_CLR;
float LINES_B_CLR;
float LS_POINTS_A_CLR;
float LS_POINTS_R_CLR;
float LS_POINTS_G_CLR;
float LS_POINTS_B_CLR;

// Non configurable values.
const std::string MAP_FOLDER = "/map";
const std::string POINTS_NUM_H = "NumPoints";
const std::string LINES_NUM_H = "NumLines";
const std::string POINTS_H = "DATA";
const std::string LINES_H = "LINES";
const std::string POINTS_NS = "points";
const std::string LINES_NS = "lines";
const std::string LS_POINTS_NS = "ls_points";
const int32_t POINTS_M_ID = 0;
const int32_t LINES_M_ID = 1;
const int32_t LS_POINTS_M_ID = 2;
const double POINTS_X_SCALE = 0.045;
const double POINTS_Y_SCALE = 0.045;
const double LINES_X_SCALE = 0.045;
const double LS_POINTS_X_SCALE = 0.045;
const double LS_POINTS_Y_SCALE = 0.045;

// Names for all config parameters.
const std::string PACK_NAME_PARAM = "pkg_name";
const std::string MAP_NAME_PARAM = "map_name";
const std::string HEAD_FRAME_PARAM = "head_frame";
const std::string VIS_TOPIC_PARAM = "vis_topic";
const std::string RNG_DEVICE_PARAM = "range_device";
const std::string POINTS_A_CLR_PARAM = "points_a_colour";
const std::string POINTS_R_CLR_PARAM = "points_r_colour";
const std::string POINTS_G_CLR_PARAM = "points_g_colour";
const std::string POINTS_B_CLR_PARAM = "points_b_colour";
const std::string LINES_A_CLR_PARAM = "lines_a_colour";
const std::string LINES_R_CLR_PARAM = "lines_r_colour";
const std::string LINES_G_CLR_PARAM = "lines_g_colour";
const std::string LINES_B_CLR_PARAM = "lines_b_colour";
const std::string LS_POINTS_A_CLR_PARAM = "ls_points_a_colour";
const std::string LS_POINTS_R_CLR_PARAM = "ls_points_r_colour";
const std::string LS_POINTS_G_CLR_PARAM = "ls_points_g_colour";
const std::string LS_POINTS_B_CLR_PARAM = "ls_points_b_colour";

// Function prototypes
bool get_map_data(std::string filename, 
    std::vector<geometry_msgs::Point>& points, 
    std::vector<geometry_msgs::Point>& lines);
void req_range_scan(ros::ServiceClient& service, om_aiv_util::ArclApi& srv, std::vector<geometry_msgs::Point>& points);

int main(int argc, char** argv)
{
    ros::init(argc, argv, "data_points_marker");
    ros::NodeHandle nh;
    ros::Rate rate(5);

    // Get all parameters.
    nh.param<std::string>(PACK_NAME_PARAM, PACK_NAME, "pkg");
    nh.param<std::string>(MAP_NAME_PARAM, MAP_NAME, "data.map");
    nh.param<std::string>(HEAD_FRAME_PARAM, HEAD_FRAME, "/pose");
    nh.param<std::string>(VIS_TOPIC_PARAM, VIS_TOPIC, "visualization_marker");
    nh.param<std::string>(RNG_DEVICE_PARAM, rng_device, "Laser_1");
    nh.param<float>(POINTS_A_CLR_PARAM, POINTS_A_CLR, 1.0);
    nh.param<float>(POINTS_R_CLR_PARAM, POINTS_R_CLR, 0);
    nh.param<float>(POINTS_G_CLR_PARAM, POINTS_G_CLR, 0);
    nh.param<float>(POINTS_B_CLR_PARAM, POINTS_B_CLR, 0);
    nh.param<float>(LINES_A_CLR_PARAM, LINES_A_CLR, 1.0);
    nh.param<float>(LINES_R_CLR_PARAM, LINES_R_CLR, 0);
    nh.param<float>(LINES_G_CLR_PARAM, LINES_G_CLR, 0);
    nh.param<float>(LINES_B_CLR_PARAM, LINES_B_CLR, 0);
    nh.param<float>(LS_POINTS_A_CLR_PARAM, LS_POINTS_A_CLR, 1.0);
    nh.param<float>(LS_POINTS_R_CLR_PARAM, LS_POINTS_R_CLR, 0);
    nh.param<float>(LS_POINTS_G_CLR_PARAM, LS_POINTS_G_CLR, 0);
    nh.param<float>(LS_POINTS_B_CLR_PARAM, LS_POINTS_B_CLR, 0);

    ros::Publisher points_pub = nh.advertise<visualization_msgs::Marker>(VIS_TOPIC, 10);
    ros::Publisher laser_scan_pub = nh.advertise<visualization_msgs::Marker>(VIS_TOPIC, 10);
    ros::ServiceClient arcl_api_client = nh.serviceClient<om_aiv_util::ArclApi>("arcl_api_service");

    //// Begin drawing points and line on RVIZ ////

    std::vector<geometry_msgs::Point> points;
    std::vector<geometry_msgs::Point> lines;
    if (!get_map_data(MAP_NAME, points, lines)) ROS_ERROR("Reading map failed");
    ROS_INFO("%s: Waiting for RVIZ", ros::this_node::getName().c_str());

    // Configure the messages to publish.
    visualization_msgs::Marker points_arr;
    visualization_msgs::Marker lines_list;
    points_arr.header.frame_id = lines_list.header.frame_id = HEAD_FRAME;
    points_arr.header.stamp = lines_list.header.stamp = ros::Time::now();
    points_arr.ns = POINTS_NS;
    lines_list.ns = LINES_NS;
    points_arr.action = lines_list.action = visualization_msgs::Marker::ADD;
    points_arr.pose.orientation.w = lines_list.pose.orientation.w = 1.0;
    points_arr.id = POINTS_M_ID;
    lines_list.id = LINES_M_ID;
    points_arr.type = visualization_msgs::Marker::POINTS;
    lines_list.type = visualization_msgs::Marker::LINE_LIST;
    points_arr.scale.x = POINTS_X_SCALE;
    points_arr.scale.y = POINTS_Y_SCALE;
    lines_list.scale.x = LINES_X_SCALE;
    points_arr.color.a = POINTS_A_CLR;
    points_arr.color.r = POINTS_R_CLR;
    points_arr.color.g = POINTS_G_CLR;
    points_arr.color.b = POINTS_B_CLR;
    lines_list.color.a = LINES_A_CLR;
    lines_list.color.r = LINES_R_CLR;
    lines_list.color.g = LINES_G_CLR;
    lines_list.color.b = LINES_B_CLR;

    // Prepare all points.
    for (int i = 0; i < points.size(); i++)
    {
        points_arr.points.push_back(points[i]);
    }

    // Prepare all lines.
    for (int i = 0; i < lines.size(); i++)
    {
        lines_list.points.push_back(lines[i]);
    }
    
    /// Draw laser scan data ///
    
    visualization_msgs::Marker laser_points;
    laser_points.header.frame_id = HEAD_FRAME;
    laser_points.action = visualization_msgs::Marker::ADD;
    laser_points.ns = LS_POINTS_NS;
    laser_points.pose.orientation.w = 1.0;
    laser_points.type = visualization_msgs::Marker::POINTS;
    laser_points.id = LS_POINTS_M_ID;
    laser_points.scale.x = LS_POINTS_X_SCALE;
    laser_points.scale.y = LS_POINTS_Y_SCALE;
    laser_points.color.a = LS_POINTS_A_CLR;
    laser_points.color.r = LS_POINTS_R_CLR;
    laser_points.color.g = LS_POINTS_G_CLR;
    laser_points.color.b = LS_POINTS_B_CLR;
    
    // Create the service request message to get laser scan data.
    om_aiv_util::ArclApi srv;
    std::string cmd = "RangeDeviceGetCurrent ";
    cmd.append(rng_device);
    srv.request.command = cmd;
    srv.request.line_identifier = "RangeDeviceGetCurrent:";

    while (ros::ok())
    {
        points_pub.publish(points_arr);
        points_pub.publish(lines_list);

        req_range_scan(arcl_api_client, srv, laser_points.points);
        laser_points.header.stamp = ros::Time::now();
        laser_scan_pub.publish(laser_points);
        
        rate.sleep();
    }
    return 0;
}

/**
 * @brief Attemps to open .map file with the given file name and read all points and lines coordinates.
 * 
 * @param filename name of .map file to read, including file extension.
 * @param points Vector to store all read points.
 * @param lines Vector to store all read lines.
 * @return true if data is read without issue.
 * @return false if file fails to open or there is error in reading data.
 */
bool get_map_data(std::string filename, 
    std::vector<geometry_msgs::Point>& points,
    std::vector<geometry_msgs::Point>& lines)
{
    // Read map file
    std::string path = ros::package::getPath(PACK_NAME);
    path = path.append(MAP_FOLDER).append("/");
    std::string map_path = path.append(filename);
    std::ifstream map_file(map_path);
    if (map_file.fail()) return false;

    int num_of_points = 0;
    int num_of_lines = 0;
    std::string line;
    std::string ignore_head;
    while (std::getline(map_file, line))
    {
        // Retrieve the number of points.
        if (line.find(POINTS_NUM_H) != std::string::npos)
        {
            std::istringstream iss(line);
            iss >> ignore_head;
            iss >> num_of_points;
        }

        // Retrieve the number of lines.
        if (line.find(LINES_NUM_H) != std::string::npos)
        {
            std::istringstream iss(line);
            iss >> ignore_head;
            iss >> num_of_lines;
        }

        // We have seen the points data, collect them.
        if (line.find(POINTS_H) != std::string::npos)
        {
            int x, y;
            for (int i = 0; i < num_of_points; i++)
            {
                std::getline(map_file, line);
                std::istringstream iss(line);
                if (!(iss >> x >> y)) ROS_ERROR("Error reading points from file.");
                geometry_msgs::Point p;
                p.x = (double)x / 1000.0; // Values are in millimeter.
                p.y = (double)y / 1000.0;
                p.z = 0;
                points.push_back(p);
            }
        }

        // We have seen the lines data, collect them.
        if (line.find(LINES_H) != std::string::npos)
        {
            int x1, y1, x2, y2;
            for (int i = 0; i < num_of_lines; i++)
            {
                std::getline(map_file, line);
                std::istringstream iss(line);
                if(!(iss >> x1 >> y1 >> x2 >> y2)) ROS_ERROR("Error reading points from file.");
                geometry_msgs::Point p1;
                geometry_msgs::Point p2;
                p1.x = (double)x1 / 1000.0; // Values are in millimeter.
                p1.y = (double)y1 / 1000.0;
                p1.z = 0;
                p2.x = (double)x2 / 1000.0;
                p2.y = (double)y2 / 1000.0;
                p2.z = 0;
                // Needs two consecutive points to form a line.
                lines.push_back(p1);
                lines.push_back(p2);
            }
        }
    }
    return true;
}

/**
 * @brief Requests for laser scan data from ARCL server and return as a vector of values. 
 * 
 * @param service Reference to ros::ServiceClient object to request from.
 * @param srv Reference to service message object that will be used.
 * @param ranges Reference to vector<float> to store laser scan values.
 */
void req_range_scan(ros::ServiceClient& service, om_aiv_util::ArclApi& srv, std::vector<geometry_msgs::Point>& points)
{
    if (service.call(srv))
    {
        std::string raw_resp = srv.response.response;
        std::string::size_type pos = raw_resp.find(rng_device);
        if (pos != std::string::npos)
        {
            std::string vals_str;
            try
            {
                vals_str = raw_resp.substr(pos + rng_device.length() + 1); // +1 to exclude the following space.
            }
            catch(const std::out_of_range& e)
            {
                ROS_ERROR("%s: No laser scan values in incoming response.", e.what());
                vals_str.clear();
            }
            
            std::istringstream iss(vals_str);
            double x, y = 0.0;
            points.clear();
            while (iss >> x >> y)
            {
                geometry_msgs::Point p;
                p.x = x / 1000.0;
                p.y = y / 1000.0;
                p.z = 0;
                points.push_back(p);
            }
        }
    }
    else
    {
        ROS_ERROR("Failed to call %s service", "arcl_api_service");
    }
}