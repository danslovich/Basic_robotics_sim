# First Example
# Move robot forward until a 
# wall is less than 1 meter away

from robot_control_class import RobotControl

rc = RobotControl()

while True:
    # Check distance
	dist = rc.get_laser(360)
	
	if dist < 1:
        # Stop robot when wall <1m away
		rc.stop_robot()
		print ("The robot stopped at %f meters from the wall" % dist)
		
	else:
	    # Move straight when wall >1m away
		rc.move_straight()
		print ("The robot is %f meters from the wall" % dist)