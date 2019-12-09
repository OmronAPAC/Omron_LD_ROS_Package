#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/tthmatt/Omron_LD_ROS_Package/src/om_aiv_util"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/tthmatt/Omron_LD_ROS_Package/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/tthmatt/Omron_LD_ROS_Package/install/lib/python2.7/dist-packages:/home/tthmatt/Omron_LD_ROS_Package/build/om_aiv_util/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/tthmatt/Omron_LD_ROS_Package/build/om_aiv_util" \
    "/usr/bin/python2" \
    "/home/tthmatt/Omron_LD_ROS_Package/src/om_aiv_util/setup.py" \
    build --build-base "/home/tthmatt/Omron_LD_ROS_Package/build/om_aiv_util" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/tthmatt/Omron_LD_ROS_Package/install" --install-scripts="/home/tthmatt/Omron_LD_ROS_Package/install/bin"
