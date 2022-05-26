#! /usr/bin/env python3
import os,sys,rospy,rospkg,time
from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    rospack = rospkg.RosPack()

    try:
        filepath = rospack.get_path('auto_update_git')
        os.chdir(filepath)
        os.chdir("../../")
        os.system("git pull")
        os.system("catkin build")
        rospy.loginfo("Catkin build successfully executed !")
        status = True
        msg = "Robot updated succesfully !"
        os.system("exit 0")
    except Exception as e:
        rospy.loginfo("Exception: " + str(e))
        status = False
        msg = "Robot update unsuccesful"
    return TriggerResponse(success=status,message=msg)

rospy.init_node('robot_update_server')
rospy.loginfo("Starting robot update service. Waiting for trigger")
my_service = rospy.Service('/robot_update', Trigger, trigger_response)
rospy.spin()