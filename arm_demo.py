from arm_controller import ArmController

ac=ArmController()
ac.set_joints([.1,.5,.9,.8])
print(ac.get_pose())
