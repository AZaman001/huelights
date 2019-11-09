import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


# Cozmo program to go 'get towels'
def cozmo_program(robot: cozmo.robot.Robot):

	# uncomment if you want Cozmo to say that he is getting towels
	#robot.say_text(f"I am going to go get towels").wait_for_completed()

    # reset Cozmo's arms and head
    robot.set_head_angle(degrees(10.0)).wait_for_completed()
    robot.set_lift_height(0.0).wait_for_completed()

    robot.drive_straight(distance_mm(300), speed_mmps(100)).wait_for_completed()

cozmo.run_program(cozmo_program, use_viewer=True, force_viewer_on_top=True)