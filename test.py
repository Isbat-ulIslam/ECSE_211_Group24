from utils.brick import EV3ColorSensor, wait_ready_sensors, Motor, TouchSensor, reset_brick
from color_detection import color_detect_func
from time import sleep

print("Hola")

LEFT_COLOR_SENSOR = EV3ColorSensor(3)
RIGHT_COLOR_SENSOR = EV3ColorSensor(4)

LEFT_MOTOR = Motor("C")
RIGHT_MOTOR = Motor("B")

TOUCH_SENSOR = TouchSensor(1)
RIGHT_MOTOR.set_power(0)
LEFT_MOTOR.set_power(0)

print("Hello World")

def drive():
    #reset_brick()
    wait_ready_sensors(True)
    
    print("It is in drive")
    
    global last_seen
    
    while True:
        if TOUCH_SENSOR.is_pressed():
            print("TOUCH SENSOR PRESSED")
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(0)
            exit()
        
        global LEFT_COLOR_SENSOR
        global RIGHT_COLOR_SENSOR
        
        left_color = color_detect_func(LEFT_COLOR_SENSOR)
        right_color = color_detect_func(RIGHT_COLOR_SENSOR)
        
#         print(left_color + " " + right_color)
    
        if (left_color == "table" and right_color == "table"):
            LEFT_MOTOR.set_power(20)
            RIGHT_MOTOR.set_power(20)
        
        if left_color == "green" and right_color == "green":
            status = "On Green"
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(0)
            return status
        
        if left_color == "green" and right_color != "green":
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(10)
        
        if right_color == "green" and left_color != "green":
            RIGHT_MOTOR.set_power(0)
            LEFT_MOTOR.set_power(10)
        
        
        if (left_color == "red" or left_color == "blue") and right_color == "table":
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(20)
            time.sleep(0.2)
            LEFT_MOTOR.set_power(20)
        if (right_color == "red" or right_color == "blue") and left_color == "table":
            RIGHT_MOTOR.set_power(0)
            LEFT_MOTOR.set_power(20)
            time.sleep(0.2)
            RIGHT_MOTOR.set_power(20)
            

print("Hello World")
drive()