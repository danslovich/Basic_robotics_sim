# Demonstrate two new RobotControl functs
# Req: Move robot forward 5s. Turn robot clockwise 7s
# Print funct output after each movement

from robot_control_class import RobotControl

rc = RobotControl()

# Move robot straight at 1 m/s for 5 s
# Args: direction, speed m/s, time s
print rc.move_straight_time('forward', 1, 5)

# Rotate robot clockwise at 2 m/s for 7 s
# Args: direction, speed m/s, time s
print rc.turn('clockwise', 2, 7)