# Create funct with integer arg
# Move robot for arg value in secs

from robot_control_class import RobotControl
import time

rc = RobotControl()

# Define funct for foward movement with 1 arg
def forward_t_secs(t=0):

	rc.move_straight()
    # Wait for t seconds
	time.sleep(t) 
    # Now stop
	rc.stop_robot()

# Call funct with 1 time arg
forward_t_secs(3)
