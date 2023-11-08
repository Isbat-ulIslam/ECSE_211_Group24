from navigation.shortPath import astar

NUMBER_OF_FIRES = 3;
FIRE_STATION = (0, 0)
FIRE_TYPES = ['A', 'B', 'C', 'D', 'E', 'F']
INVALID_COORDINATE_INPUT_MSG = "Invalid input. Enter coordinates between 0 and 3."
INVALID_FIRE_TYPE_INPUT_MSG = f"Invalid input. Enter one of the following fire types: {FIRE_TYPES}"

# ADD STATUSES TO DISPLAY DURING RUNTIME
# hola

def start():
    init_robot()    # Complete this function

    coordinates = []
    fire_types = []
    counter = 1

    print("Welcome to the Robot Firefighter Program!\n")

    while True:
        if (counter == 4):
            break

        x = int(input(f"Enter x-coordinate for fire {counter}: "))
        y = int(input(f"Enter y-coordinate for fire {counter}: "))

        if (not validate_coordinate (x) or not validate_coordinate(y)):
            print(INVALID_COORDINATE_INPUT_MSG)
            continue
        
        fire_type = input(f"Enter fire type for fire {counter}: ")
        if (not validate_fire_type(fire_type)):
            print(INVALID_FIRE_TYPE_INPUT_MSG)
            continue

        coordinates.append((x, y))
        fire_types.append(fire_type)
        counter += 1
        print()

    fire_colors = get_fire_colors(fire_types)   # the list of fire colors e.g. [blue, green, orange]
    paths = compute_shortest_path(coordinates)  # list of the 4 paths from start to finish
    print(paths)


def init_robot():
    # Write initialization code for all motors and sensors in the BrickPi
    print("INITIALIZING")

def compute_shortest_path(coordinates):
    paths = []
    start=FIRE_STATION
    for i in range(len(coordinates)+1):
        if(i == (len(coordinates))):
           end=FIRE_STATION
        else:
            end= coordinates[i]
        obstacles= []
        for j in range(len(coordinates)):
            temp= coordinates[j]
            if not(temp==end) and not (temp==start):
                obstacles.append(temp)
        added=(astar(start, end, obstacles))
        for element in added:
            paths.append(element)
        start = paths[-2]
        # if i == 0:
        #     start = FIRE_STATION
        #     end = coordinates[i]
        #     obstacles = [coordinates[i + 1], coordinates[i + 2]]
        # elif i == 1:
        #     start = coordinates[i - 1]
        #     end = coordinates[i]
        #     obstacles = [coordinates[i - 1], coordinates[i + 1]]
        # elif i == 2:
        #     start = coordinates[i - 1]
        #     end = coordinates[i]
        #     obstacles = [coordinates[i - 2], coordinates[i - 1]]
        # elif i == 3:
        #     start = coordinates[i - 1]
        #     end = FIRE_STATION
        #     obstacles = [coordinates[i - 3], coordinates[i - 2], coordinates[i - 1]]
        # paths.append(astar(start, end, obstacles))
    
    return paths

def get_fire_colors(fire_types):
    fire_colors = []

    for fire in fire_types:
        if fire == 'A':
            fire_colors.append('blue')
        elif fire == 'B':
            fire_colors.append('yellow')
        elif fire == 'C':
            fire_colors.append('purple')
        elif fire == 'D':
            fire_colors.append('red')
        elif fire == 'E':
            fire_colors.append('orange')
        elif fire == 'F':
            fire_colors.append('green')
    
    return fire_colors

def validate_coordinate(x):
    if x > 3 or x < 0:
        return False
    return True

def validate_fire_type(fire_type):
    if fire_type not in FIRE_TYPES:
        return False
    return True

start()