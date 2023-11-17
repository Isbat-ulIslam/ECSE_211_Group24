from math import sqrt
from utils.brick import EV3ColorSensor, wait_ready_sensors, Motor, TouchSensor
import time

# (R, G, B) average for red from our tests for the DRIVING sensor
rR = 256
gR = 25
bR = 28
normrR = rR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))
normgR = gR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))
normbR = bR / sqrt(pow(rR, 2) + pow(gR, 2) + pow(bR, 2))



# (R, G, B) average for green from our tests for the DRIVING sensor
rG= 18
gG= 80
bG= 24
normrG = rG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))
normgG = gG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))
normbG = bG / sqrt(pow(rG, 2) + pow(gG, 2) + pow(bG, 2))


# (R, G, B) average for blue from our tests for the DRIVING sensor
rB = 31
gB = 55
bB = 94
normrB = rB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))
normgB = gB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))
normbB = bB / sqrt(pow(rB, 2) + pow(gB, 2) + pow(bB, 2))

# (R, G, B) average for table color from our tests for the DRIVING sensor
rT = 162
gT = 102
bT = 50
normrT = rT / sqrt(pow(rT, 2) + pow(gT, 2) + pow(bT, 2))
normgT = gT / sqrt(pow(rT, 2) + pow(gT, 2) + pow(bT, 2))
normbT = bT / sqrt(pow(rT, 2) + pow(gT, 2) + pow(bT, 2))


def color_detection_drive(rgb):
  """
  Color detection function for the driving color sensor.
  Used to control which way our robot turns.
  
  Input - None
  Output - None
  """
  if (rgb[0] == None or rgb[1] == None or rgb[2] == None):
      return ""
  #normalized vector from hardcoded data for colors
  if pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5) == 0:
      return ""
  rgb = (rgb[0] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5), rgb[1] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5), 
         rgb[2] /pow((pow(rgb[0],2)+pow(rgb[1], 2)+pow(rgb[2],2)), 0.5))
  
  rgbRed = [normrR, normgR, normbR]
  rgbGreen = [normrG,normgG,normbG]
  rgbBlue = [normrB,normgB,normbB]
  rgbTable = [normrT, normgT, normbT]

  #calculating distance
  distanceFromRed = pow(pow(rgb[0]-rgbRed[0], 2) + pow(rgb[1]-rgbRed[1],2) + pow(rgb[2]-rgbRed[2],2),0.5) 
  distanceFromGreen = pow(pow(rgb[0]-rgbGreen[0], 2) + pow(rgb[1]-rgbGreen[1],2) + pow(rgb[2]-rgbGreen[2],2), 0.5) 
  distanceFromBlue = pow(pow(rgb[0]-rgbBlue[0], 2) + pow(rgb[1]-rgbBlue[1],2) + pow(rgb[2]-rgbBlue[2],2), 0.5)
  distanceFromTable = pow(pow(rgb[0] - rgbTable[0], 2) + pow(rgb[1]-rgbTable[1], 2) + pow(rgb[2]-rgbTable[2], 2), 0.5)
  
  distances = {
    "red": distanceFromRed,
    "green" : distanceFromGreen,
    "blue" : distanceFromBlue,
    "table": distanceFromTable,
  }

  miniumumDistance = min(distances.values())

  color = [k for k, v in distances.items() if v == miniumumDistance]

  return color[0]


def color_detect_func(color_sensor):
    return color_detection_drive(color_sensor.get_rgb())
    
def drive():
    greenCount = 0
    onGreen = False
    
    while True:
        if TOUCH_SENSOR.is_pressed():
            print("TOUCH SENSOR PRESSED")
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(0)
            print("GREEN COUNT", greenCount)
            exit()
        
        left_color = color_detect_func(LEFT_COLOR_SENSOR)
        right_color = color_detect_func(RIGHT_COLOR_SENSOR)
        
        if left_color == "" or right_color == "":
            print("Color sensor is returning None")
    
        if (left_color == "table" and right_color == "table"):
            print("TABLE")
            LEFT_MOTOR.set_power(30)
            RIGHT_MOTOR.set_power(30)
        
        
        if left_color == "green" and right_color != "green":
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(10)
        
        if right_color == "green" and left_color != "green":
            RIGHT_MOTOR.set_power(0)
            LEFT_MOTOR.set_power(10)
            
        
        
        if (left_color == "green" and right_color == "green"):
            if (not onGreen):
                onGreen = True
                print("ON GREEN")
                greenCount += 1
            else:
                LEFT_MOTOR.set_power(0)
                RIGHT_MOTOR.set_power(0)
                break

        
        if (left_color == "red" or left_color == "blue") and right_color == "table":
            LEFT_MOTOR.set_power(0)
            RIGHT_MOTOR.set_power(30)
            time.sleep(0.2)
            LEFT_MOTOR.set_power(30)
        if (right_color == "red" or right_color == "blue") and left_color == "table":
            RIGHT_MOTOR.set_power(0)
            LEFT_MOTOR.set_power(30)
            time.sleep(0.2)
            RIGHT_MOTOR.set_power(30)
            
# def main():
#     while True:
#         print(color_detect_func(LEFT_COLOR_SENSOR))
          
