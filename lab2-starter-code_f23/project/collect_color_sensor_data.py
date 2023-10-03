#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

from utils import sound
from utils.brick import EV3ColorSensor, wait_ready_sensors, TouchSensor
from time import sleep

COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"
DELAY_SEC = 0.01  # seconds of delay between measurements
SOUND = sound.Sound(duration=0.3, pitch="A4", volume=60)

# complete this based on your hardware setup
color = EV3ColorSensor(1)
touch = TouchSensor(2)

wait_ready_sensors(True) # Input True to see what the robot is trying to initialize! False to be silent.
color.get_raw_value()

def collect_color_sensor_data():
    "Collect color sensor data."
    try:
        output_file = open(COLOR_SENSOR_DATA_FILE, "w")
        while not touch.is_pressed():
            pass
        print("Touch sensor pressed")
        sleep(1)
        print("Starting to collect CS samples")
        while not touch.is_pressed():
            cs_data = color.get_rgb()  
            if cs_data is not None: # If None is given, then data collection failed that time
                print(cs_data)
                output_file.write(f"{cs_data}\n")
            sleep(DELAY_SEC)
    except BaseException:  # capture all exceptions including KeyboardInterrupt (Ctrl-C)
        pass
    finally:
        print("Done collecting CS distance samples")
        output_file.close()
        reset_brick() # Turn off everything on the brick's hardware, and reset it
        exit()
            
        
        
    


if _name_ == "_main_":
    collect_color_sensor_data()