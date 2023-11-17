from  utils.brick import EV3ColorSensor, wait_ready_sensors, Motor, TouchSensor, reset_brick
import time
import math

LEVER_MOTOR = Motor("A")
PLATFORM_ROTATION_MOTOR = Motor("D")
# Rotation limits are pre-set so that robots don't rotate too quick.
LEVER_MOTOR.set_limits(50)
PLATFORM_ROTATION_MOTOR.set_limits(10)
MOTOR_WAIT = 0.1
# Dictionary ordering colours, COld Colours --> Warm Colours. Keys = Colors, Values = Approximate Degrees
COLORS_ON_PLATFORM = {"A": 0, "B": 50, "C": 130, "D": -180, "E": -130, "F": -50}

# Rotates platform.
def rotate_platform(degrees):
        PLATFORM_ROTATION_MOTOR.set_position_relative(degrees)
        print("done rotating")
        wait_sleep_movement(PLATFORM_ROTATION_MOTOR)
        # reset_brick()
        
# Activates lever to kick cube and brings it back.
def kick_lever():
    LEVER_MOTOR.set_position_relative(-45)
    wait_sleep_movement(LEVER_MOTOR)
    LEVER_MOTOR.set_position_relative(45)
    wait_sleep_movement(LEVER_MOTOR)


def wait_sleep_movement(motor):
    while math.isclose(motor.get_dps(), 0): 
        time.sleep(MOTOR_WAIT)
    while not math.isclose(motor.get_dps(),0):
        time.sleep(MOTOR_WAIT)

def drop_color(color):
    degrees = COLORS_ON_PLATFORM[color]
    print(degrees)
    if degrees!=0:
        rotate_platform(degrees)
    print("platform rotated")
    kick_lever()
    if degrees!=0:
        rotate_platform(-1*degrees)
    

