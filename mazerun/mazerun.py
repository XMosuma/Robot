import sys


command_run = sys.argv

if "turtle" in command_run:
    import world.turtle.world as world
else:
    import world.text.world as world

def is_front_free(steps, r_name, x_position, y_position, direction):
    """Move the robot forward then return the new x, y position."""

    new_x = x_position
    new_y = y_position

    if direction == 0:
        new_y += abs(int(steps))
    elif direction == 90:
        new_x += abs(int(steps))
    elif direction == 180:
        new_y -= abs(int(steps))
    elif direction == 270:
        new_x -= abs(int(steps))
    
    if world.position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, x_position, y_position, ""
    
    if world.limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, x_position, y_position, ""

    return False, x_position, y_position, "end"


def is_back_free(steps, r_name, x_position, y_position, direction):
    """Move the robot back then return the new x, y position."""

    new_x = x_position
    new_y = y_position

    if direction == 0:
        new_y -= abs(int(steps))
    elif direction == 90:
        new_x -= abs(int(steps))
    elif direction == 180:
        new_y += abs(int(steps))
    elif direction == 270:
        new_x += abs(int(steps))
    
    if world.position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, x_position, y_position, ""
    
    if world.limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, x_position, y_position, ""

    return False, x_position, y_position, "end"



def is_right_free(steps, r_name, x_position, y_position, temp_direct):

    new_x = x_position
    new_y = y_position

    if temp_direct == 0:
        temp_direct = 90
    elif temp_direct == 90:
        temp_direct = 180
    elif temp_direct == 180:
        temp_direct = 270
    elif temp_direct == 270:
        temp_direct = 0
    
    if temp_direct == 0:
        new_y += steps
    elif temp_direct == 90:
        new_x += steps
    elif temp_direct == 180:
        new_y -= steps
    elif temp_direct == 270:
        new_x -= steps
    
    if world.position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, x_position, y_position, ""
    
    if world.limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, x_position, y_position, ""

    return False, x_position, y_position, "end"


def is_left_free(steps, r_name, x_position, y_position, temp_direct):
    
    new_x = x_position
    new_y = y_position

    if temp_direct == 0:
        temp_direct = 270
    elif temp_direct == 270:
        temp_direct = 180
    elif temp_direct == 180:
        temp_direct = 90
    elif temp_direct == 90:
        temp_direct = 0
    
    if temp_direct == 0:
        new_y += steps
    elif temp_direct == 90:
        new_x += steps
    elif temp_direct == 180:
        new_y -= steps
    elif temp_direct == 270:
        new_x -= steps
    
    if world.position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, x_position, y_position, ""
    
    if world.limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, x_position, y_position, ""

    return False, x_position, y_position, "end"



def maze_run(r_name, x_position, y_position, direction, maze_direction):

    steps = 12
    temp_x = x_position
    temp_y = y_position
    direction = 0
    front_list = [(temp_x, temp_y)]
    visited = list()
    solution_list = list()
    track_dict = {front_list[0]:front_list[0]}
    msg = ""

    while len(front_list) != 0:
        current = front_list[0]
        bool_front, x_front, y_front, path_front = is_front_free(steps,r_name, current[0], current[1], direction)
        bool_back, x_back, y_back, path_back = is_back_free(steps, r_name, current[0], current[1], direction)
        bool_left, x_left, y_left, path_left = is_left_free(steps, r_name, current[0], current[1], direction)
        bool_right, x_right, y_right, path_right = is_right_free(steps, r_name, current[0], current[1], direction)

        if bool_front and (x_front, y_front) not in visited and front_list.count(current) == 1:
            front_list.append((x_front, y_front))

        if bool_back and (x_back, y_back) not in visited and front_list.count(current) == 1:
            front_list.append((x_back, y_back))
            
        if bool_left and (x_left, y_left) not in visited and front_list.count(current) == 1:
            front_list.append((x_left, y_left))
            
        if bool_right and (x_right, y_right) not in visited and front_list.count(current) == 1:
            front_list.append((x_right, y_right))
     
        
        if current != (x_position,y_position):

            if bool_back and (current[0], current[1]-12) in visited:
                track_dict[current] = (current[0], current[1]-12)

            elif bool_front and (current[0], current[1]+12) in visited:
                track_dict[current] = (current[0], current[1]+12)

            elif bool_right and (current[0]+12, current[1]) in visited:
                track_dict[current] = (current[0]+12, current[1])

            elif bool_left and (current[0]-12, current[1]) in visited:
                track_dict[current] = (current[0]-12, current[1])
            
            # if( path_back == 'end' or path_front == 'end' or path_right == 'end' or\
            #     path_left == 'end') and maze_direction =='':

            #     msg = f"{r_name}: mazerun complited."
            #     break  

            if  path_front == "end" and (maze_direction == "top" or maze_direction ==''):
                msg = f"{r_name}: I am at the top edge."
                break

            elif path_back == "end" and maze_direction == "bottom":
                msg = f"{r_name}: I am at the bottom edge."
                break

            elif path_left == "end" and maze_direction == "left":
                msg = f"{r_name}: I am at the left edge."
                break

            elif path_right == "end" and maze_direction == "right":
                msg = f"{r_name}: I am at the right edge."
                break
        
        if current not in visited:
            visited.append(current)
        front_list.pop(0)
    
    start = list(track_dict)[-1]
    solution_list.append(start)
    key_value = track_dict[start]
    value_key = track_dict[key_value]
    
    while True:
        solution_list.append(key_value)
        solution_list.append(value_key)
        key_value = track_dict[value_key]
        value_key = track_dict[key_value]

        if key_value == (x_position,y_position):
            solution_list.append(key_value)
            solution_list.append(value_key)
            break

    solution_list.reverse()

    return solution_list, msg

