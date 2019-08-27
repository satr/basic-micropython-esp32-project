#!/bin/sh
#provide an argument in Script Options of Run/Debug Configuration - your board device path. E.g. /dev/cu.SLAB_USBtoUART, /dev/ttyUSB0
#Use the command to read devices: ls /dev/*
#Or replace "$1" with this device path
rshell -p "$1" -b 115200