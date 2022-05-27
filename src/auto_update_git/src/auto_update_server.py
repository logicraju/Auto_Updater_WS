#! /usr/bin/env python3
import os,subprocess,rospy,rospkg
from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    try:
        rospack = rospkg.RosPack()
        filepath = rospack.get_path('auto_update_git')
        os.chdir(filepath+"/src")
        print(os.getcwd())
        output = subprocess.run(['./robot_update.sh'])
        print('Return code:', output)
        print(os.getcwd())
        if(output == 0):
            status = True
            msg = "Robot update succesful !"
        else:
            status = False
            msg = "Robot update unsuccesful ..."    
    except Exception as e:
        rospy.loginfo("Exception: " + str(e))
        status = False
        msg = "Robot update unsuccesful ..."
    return TriggerResponse(success=status,message=msg)

rospy.init_node('robot_update_server')
rospy.loginfo("Starting robot update service. Waiting for trigger")
my_service = rospy.Service('/robot_update', Trigger, trigger_response)
rospy.spin()