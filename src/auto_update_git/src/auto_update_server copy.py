#! /usr/bin/env python3
import subprocess,rospy,rospkg
from std_srvs.srv import Trigger, TriggerResponse

def trigger_response(request):
    rospack = rospkg.RosPack()

    try:
        command = "sh"
        options = "robot_update.sh"
        args=[]
        args.append(command)
        args.append(options)
        output = subprocess.run(args,capture_output=True)
        print('Return code:', output.returncode)
        print('Output:',output.stdout.decode("utf-8"))
    except Exception as e:
        rospy.loginfo("Exception: " + str(e))
        status = False
        msg = "Robot update unsuccesful"
    return TriggerResponse(success=status,message=msg)

rospy.init_node('robot_update_server')
rospy.loginfo("Starting robot update service. Waiting for trigger")
my_service = rospy.Service('/robot_update', Trigger, trigger_response)
rospy.spin()