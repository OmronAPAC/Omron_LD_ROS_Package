execute_process(COMMAND "/home/tthmatt/Omron_LD_ROS_Package/build/om_aiv_util/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/tthmatt/Omron_LD_ROS_Package/build/om_aiv_util/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
