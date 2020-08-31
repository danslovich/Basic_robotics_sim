# Create funct that takes 3 args for lazer angles (0<->719)
# Returns list of distance values in m at each arg angle

from robot_control_class import RobotControl

rc = RobotControl()

# Define funct for lazer readings with 3 args
# Read distance value in m with get_laser_summit()
def laserList(a=360, b=360, c=360):
    Lazer1 = rc.get_laser_summit(a)
    Lazer2 = rc.get_laser_summit(b)
    Lazer3 = rc.get_laser_summit(c)
    # Return the distance values in a list
    return [Lazer1, Lazer2, Lazer3]

# Call funct with 3 angle args (0<->719) and print values
L_Read = laserList(120, 360, 700)
print 'The laser readings are', L_Read[0],',', L_Read[1],', and', L_Read[2], 'meters'