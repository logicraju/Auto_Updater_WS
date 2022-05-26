ROBOT UPDATER
=============


Description
-----------
ROS Package to update from git automatically when the robot boots up


Instructions
------------

1. Install robot-upstart package using the following command
	sudo apt install ros-$ROS_DISTRO-robot-upstart
	
2. Create a launch file which runs a bash script

3. Edit the file in: Auto_Updater_WS/src/auto_update_git/src/auto_update.sh and mention your local git repo path

4. Run the robot upstart, and specify the launch file path and specify the service name (here, "auto_update_git")
	rosrun robot_upstart install auto_update_git/src/auto_update.launch --job auto_update_git
	
5. Finally, enable the service using the command for it to trigger during next boot:
	sudo systemctl enable auto_update_git.service
	sudo systemctl daemon-reload

6. You may also start the service immediately using:
	sudo systemctl start auto_update_git.service

7. Also, you may check the status of the service using the command:
	sudo systemctl status auto_update_git.service
	journalctl -u auto_update_git -f

8. Make sure this ros worksapce is "sourced" in .bashrc beforehand


Dependencies
------------
sudo apt-get update
sudo apt-get install python3-catkin-tools
