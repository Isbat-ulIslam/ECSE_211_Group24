from navigation.shortPath import astar
from utils.brick import EV3ColorSensor, wait_ready_sensors, Motor, TouchSensor
from drop_block import *
from color_detection import color_detect_func


LEFT_MOTOR = Motor("C")
RIGHT_MOTOR = Motor("B")
LEFT_COLOR_SENSOR = EV3ColorSensor(3)
RIGHT_COLOR_SENSOR = EV3ColorSensor(4)
TOUCH_SENSOR = TouchSensor(1)
last_seen=""

fire=0
FIRE_STATION = (0, 0)

# ADD STATUSES TO DISPLAY DURING RUNTIME
status = ""
orientation = ""
curr_pos = 0

def start():
    init_robot()
    LEFT_MOTOR.set_power(0)
    RIGHT_MOTOR.set_power(0)

    coordinates = []
    fire_types = []
    counter = 1

    print("Welcome to the Robot Firefighter Program!\n")
    
    user_input = input("Enter the coordinates and types of fire:");
    fire_input = user_input.split(",")
    coordinates.append((int(fire_input[0]), int(fire_input[1])))
    coordinates.append((int(fire_input[3]), int(fire_input[4])))
    coordinates.append((int(fire_input[6]), int(fire_input[7])))
    
    fire_types.append(fire_input[2])
    fire_types.append(fire_input[5])
    fire_types.append(fire_input[8])

    paths = compute_shortest_path(coordinates)

    global curr_pos, fire
    while(curr_pos<len(paths)-1):
        print(paths[curr_pos])
        global orientation
        correct_orientation(paths)
        LEFT_MOTOR.set_power(10)
        RIGHT_MOTOR.set_power(10)
        time.sleep(0.5)
        drive()
        
        # if we encounter fire coordinates, then go backwards
        # then stop, drop the block, and go backwards to prev. coordinate
        if(paths[curr_pos + 1] in coordinates):
            print("FIRE NUMBER")
            color=fire_types[fire]
            LEFT_MOTOR.set_power(-20)
            RIGHT_MOTOR.set_power(-20)
            time.sleep(1.5)
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(0)
            drop_color(color)
            time.sleep(2)
            print("Drop block!")
            LEFT_MOTOR.set_power(10)
            RIGHT_MOTOR.set_power(10)
            time.sleep(0.5)
            fire += 1
            correct_orientation(paths) 
        else:
            print("NOT FIRE")
            skip_green()
            
        curr_pos+=1
        

def skip_green():
    RIGHT_MOTOR.set_power(20)
    LEFT_MOTOR.set_power(20)
    time.sleep(1)
    RIGHT_MOTOR.set_power(0)
    LEFT_MOTOR.set_power(0)
    
def init_robot():
    # Write initialization code for all motors and sensors in the BrickPi
    print("INITIALIZING")
    wait_ready_sensors(True)
    global status, curr_pos, orientation
    
    status = "Initializing"
    curr_pos=0
    orientation="+y"

def correct_orientation(paths):
    global curr_pos
    global orientation
    next_pos=paths[curr_pos+1]
    curr=paths[curr_pos]
    if (curr[0]==next_pos[0]):
        if (curr[1]>next_pos[1]):
            next_orientation="-y"
        else:
            next_orientation="+y"
    else:
        if (curr[0]>next_pos[0]):
            next_orientation="-x"
        else:
            next_orientation="+x"
    pivot(orientation,next_orientation)
    orientation=next_orientation

def pivot(c,n):
    if (c==n):
        return "done"
    if (c[0]==n[0]):
        if c[1]=="x":
            turn_left()
            return "done"
        else:
            turn_right()
            return "done"
    else:
        if c[1]==n[1]:
            turn_back()
            return "done"
        else:
            if c[1]=="x":
                turn_right()
                return "done"
            else:
                turn_left()
                return "done"
def turn_right():
    RIGHT_MOTOR.set_power(-23)
    LEFT_MOTOR.set_power(23)
    time.sleep(1)
    RIGHT_MOTOR.set_power(0)
    LEFT_MOTOR.set_power(0)
    print("TURNING RIGHT")
    
def turn_left():
    RIGHT_MOTOR.set_power(23)
    LEFT_MOTOR.set_power(-23)
    time.sleep(1)
    RIGHT_MOTOR.set_power(0)
    LEFT_MOTOR.set_power(0)
    print("TURNING LEFT")
    return "done"

def turn_back():
    RIGHT_MOTOR.set_power(-23)
    LEFT_MOTOR.set_power(23)
    time.sleep(2.2)             
    RIGHT_MOTOR.set_power(0)
    LEFT_MOTOR.set_power(0)
    return "done"
    
def compute_shortest_path(coordinates):
    paths = []
    start = FIRE_STATION

    for i in range(len(coordinates)+1):
        if i == (len(coordinates)):
            end=FIRE_STATION
        else:
            end = coordinates[i]
        obstacles = []
        
        for j in range(len(coordinates)):
            temp = coordinates[j]
            if not (temp==end) and not (temp==start):
                obstacles.append(temp)
        added=(astar(start,end,obstacles))
        for elmt in added:
            paths.append(elmt)
        start = paths[-2]
        
    
    return paths

def drive():
    greenCount = 0
    
    global last_seen
    while True:
        time.sleep(0.01)
        if TOUCH_SENSOR.is_pressed():
            print("TOUCH SENSOR PRESSED")
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(0)
            print("GREEN COUNT", greenCount)
            exit()
        
        left_color = color_detect_func(LEFT_COLOR_SENSOR)
        right_color = color_detect_func(RIGHT_COLOR_SENSOR)
    
        if (left_color == "table" and right_color == "table"):
            if (last_seen!="TABLE"):
                print("TABLE")
                last_seen= "TABLE"
            LEFT_MOTOR.set_power(20)
            RIGHT_MOTOR.set_power(20)
        
        if left_color == "green" and right_color == "green":
            greenCount += 1
            status = "On Green"
            if (last_seen!="GREEN"):
                print("GREEN")
                last_seen= "GREEN"
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
start()
reset_brick()



