ROBOT UPDATER
=============


Description
-----------
ROS Package to update this workspace from git automatically when the robot boots up


Instructions
------------

1. Install robot-upstart package using the following command
	sudo apt install ros-$ROS_DISTRO-robot-upstart
	
2. Run the robot upstart, and specify the launch file path and specify the service name (here, "auto_update_git")
	rosrun robot_upstart install auto_update_git/src/auto_update.launch --job robot_update --symlink
	
3. Finally, enable the service using the command for it to trigger during next boot:
	sudo systemctl enable auto_update_git.service
	sudo systemctl daemon-reload

4. You may also start the service immediately using:
	sudo systemctl start auto_update_git.service

5. Also, you may check the status of the service using the command:
	sudo systemctl status auto_update_git.service
	journalctl -u auto_update_git -f

6. Trigger the robot update by calling the ros service: "/robot_update"

6. Make sure this ros worksapce is "sourced" in .bashrc beforehand


Dependencies
------------
sudo apt-get update

sudo apt-get install python3-catkin-tools


Author: Kannan
