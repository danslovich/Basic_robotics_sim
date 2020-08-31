# Move Robot into room with orange bench
# Req: Utilize RobotControl functs discussed
# Additional: Print funct output after each movement

from robot_control_class import RobotControl

rc = RobotControl()

# Move robot into the room with Orange bench
# Args: direction, speed m/s, time s
rc.move_straight_time('forward', 2.5, 0.5)
rc.turn('counter-clockwise', 2, 1.07)
rc.move_straight_time('forward', 2.5, 0.7)
rc.turn('counter-clockwise', 2, 1.07)
rc.move_straight_time('forward', 2.5, 1.6)
rc.turn('clockwise', 2, 2.14)
