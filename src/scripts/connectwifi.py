#!/usr/bin/env python

import dbus
import time

def connecttowifi():
    global manager
    global connection_path
    global settings_path
    global manager_props
    global connection_params
    global connection_props


    SEEKED_SSID = "Linksys_2.4G"
    SEEKED_PASSPHRASE = "adeptlab"

    
    bus = dbus.SystemBus()
    manager_bus_object = bus.get_object("org.freedesktop.NetworkManager",
                                        "/org/freedesktop/NetworkManager")
    manager = dbus.Interface(manager_bus_object,
                             "org.freedesktop.NetworkManager")
    manager_props = dbus.Interface(manager_bus_object,
                                   "org.freedesktop.DBus.Properties")

    was_wifi_enabled = manager_props.Get("org.freedesktop.NetworkManager",
                                         "WirelessEnabled")
    if not was_wifi_enabled:
        print "Enabling WiFi and sleeping for 10 seconds ..."
        manager_props.Set("org.freedesktop.NetworkManager", "WirelessEnabled",
                          True)
        time.sleep(10)

    device_path = manager.GetDeviceByIpIface("wlp4s0")
    print "wlp4s0 path: ", device_path

    device = dbus.Interface(bus.get_object("org.freedesktop.NetworkManager",
                                           device_path),
                            "org.freedesktop.NetworkManager.Device.Wireless")
    accesspoints_paths_list = device.GetAccessPoints()

    our_ap_path = None
    for ap_path in accesspoints_paths_list:
        ap_props = dbus.Interface(
            bus.get_object("org.freedesktop.NetworkManager", ap_path),
            "org.freedesktop.DBus.Properties")
        ap_ssid = ap_props.Get("org.freedesktop.NetworkManager.AccessPoint",
                               "Ssid")
       
        str_ap_ssid = "".join(chr(i) for i in ap_ssid)
        print ap_path, ": SSID =", str_ap_ssid
        if str_ap_ssid == SEEKED_SSID:
            our_ap_path = ap_path
            break

    if not our_ap_path:
        print "AP not found :("
        exit(2)
    # print "Our AP: ", our_ap_path

    connection_params = {
        "802-11-wireless": {
            "security": "802-11-wireless-security",
        },
        "802-11-wireless-security": {
            "key-mgmt": "wpa-psk",
            "psk": SEEKED_PASSPHRASE
        },
    }

    settings_path, connection_path = manager.AddAndActivateConnection(
        connection_params, device_path, our_ap_path)
    # print "settings_path =", settings_path
    # print "connection_path =", connection_path

    NM_ACTIVE_CONNECTION_STATE_ACTIVATED = 2
    print """Connecting to wifi Linksys_2.4G...""" 
    connection_props = dbus.Interface(
        bus.get_object("org.freedesktop.NetworkManager", connection_path),
        "org.freedesktop.DBus.Properties")
    state = 0
    while True:
        state = connection_props.Get(
            "org.freedesktop.NetworkManager.Connection.Active", "State")
        if state == NM_ACTIVE_CONNECTION_STATE_ACTIVATED:
            break
        time.sleep(0.001)
    print "Connection established to wifi!"

# connecttowifi()


