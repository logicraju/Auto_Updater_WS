#!/bin/bash

cd ~/ROS_Workspaces/Auto_Updater_WS
sleep 1
git pull
sleep 1
catkin build
