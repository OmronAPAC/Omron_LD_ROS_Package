# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "om_aiv_util: 1 messages, 2 services")

set(MSG_I_FLAGS "-Iom_aiv_util:/home/tthmatt/ld_ROS/src/om_aiv_util/msg;-Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(om_aiv_util_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" NAME_WE)
add_custom_target(_om_aiv_util_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "om_aiv_util" "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" ""
)

get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" NAME_WE)
add_custom_target(_om_aiv_util_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "om_aiv_util" "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" ""
)

get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" NAME_WE)
add_custom_target(_om_aiv_util_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "om_aiv_util" "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/om_aiv_util
)

### Generating Services
_generate_srv_cpp(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/om_aiv_util
)
_generate_srv_cpp(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/om_aiv_util
)

### Generating Module File
_generate_module_cpp(om_aiv_util
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/om_aiv_util
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(om_aiv_util_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(om_aiv_util_generate_messages om_aiv_util_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_cpp _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_cpp _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_cpp _om_aiv_util_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(om_aiv_util_gencpp)
add_dependencies(om_aiv_util_gencpp om_aiv_util_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS om_aiv_util_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/om_aiv_util
)

### Generating Services
_generate_srv_eus(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/om_aiv_util
)
_generate_srv_eus(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/om_aiv_util
)

### Generating Module File
_generate_module_eus(om_aiv_util
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/om_aiv_util
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(om_aiv_util_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(om_aiv_util_generate_messages om_aiv_util_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_eus _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_eus _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_eus _om_aiv_util_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(om_aiv_util_geneus)
add_dependencies(om_aiv_util_geneus om_aiv_util_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS om_aiv_util_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/om_aiv_util
)

### Generating Services
_generate_srv_lisp(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/om_aiv_util
)
_generate_srv_lisp(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/om_aiv_util
)

### Generating Module File
_generate_module_lisp(om_aiv_util
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/om_aiv_util
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(om_aiv_util_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(om_aiv_util_generate_messages om_aiv_util_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_lisp _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_lisp _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_lisp _om_aiv_util_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(om_aiv_util_genlisp)
add_dependencies(om_aiv_util_genlisp om_aiv_util_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS om_aiv_util_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/om_aiv_util
)

### Generating Services
_generate_srv_nodejs(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/om_aiv_util
)
_generate_srv_nodejs(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/om_aiv_util
)

### Generating Module File
_generate_module_nodejs(om_aiv_util
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/om_aiv_util
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(om_aiv_util_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(om_aiv_util_generate_messages om_aiv_util_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_nodejs _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_nodejs _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_nodejs _om_aiv_util_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(om_aiv_util_gennodejs)
add_dependencies(om_aiv_util_gennodejs om_aiv_util_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS om_aiv_util_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util
)

### Generating Services
_generate_srv_py(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util
)
_generate_srv_py(om_aiv_util
  "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util
)

### Generating Module File
_generate_module_py(om_aiv_util
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(om_aiv_util_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(om_aiv_util_generate_messages om_aiv_util_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/ServiceExample.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_py _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/srv/Service.srv" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_py _om_aiv_util_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/tthmatt/ld_ROS/src/om_aiv_util/msg/Location.msg" NAME_WE)
add_dependencies(om_aiv_util_generate_messages_py _om_aiv_util_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(om_aiv_util_genpy)
add_dependencies(om_aiv_util_genpy om_aiv_util_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS om_aiv_util_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/om_aiv_util)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/om_aiv_util
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(om_aiv_util_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/om_aiv_util)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/om_aiv_util
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(om_aiv_util_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/om_aiv_util)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/om_aiv_util
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(om_aiv_util_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/om_aiv_util)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/om_aiv_util
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(om_aiv_util_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/om_aiv_util
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(om_aiv_util_generate_messages_py std_msgs_generate_messages_py)
endif()
