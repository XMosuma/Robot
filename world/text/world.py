import sys

if "play_ground" in sys.argv:
    import maze.play_ground as obs
else:
    import maze.obstacles as obs

x_position = 0
y_position = 0
direction = 0
min_x, max_x = -100, 100
min_y, max_y = -200, 200

obstacle_list = obs.obstacle_list

def position_or_path_blocked(x_position, y_position, new_x, new_y):
    return obs.is_position_blocked(new_x,new_y) or\
    obs.is_path_blocked(x_position,y_position, new_x, new_y)


def limit(new_x, new_y):
    """Checks if the robot is within the range"""
    
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def show_obstacles():
    print("There are some obstacles:")
    for tup in obs.obstacle_list:
        x = tup[0]
        y = tup[1]
        print(f"- At position {x},{y} (to {tup[0]+4},{tup[1]+4})")


def forward(command_2, r_name, x_position, y_position, direction):
    """Move the robot forward then return the new x, y position."""

    new_x = x_position
    new_y = y_position

    if direction == 0:
        new_y += abs(int(command_2))
    elif direction == 90:
        new_x += abs(int(command_2))
    elif direction == 180:
        new_y -= abs(int(command_2))
    elif direction == 270:
        new_x -= abs(int(command_2))
    
    if position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, f"{r_name}: Sorry, there is an obstacle in the way.", x_position, y_position
    
    if limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, f" > {r_name} moved forward by {abs(int(command_2))} steps.", x_position, y_position

    return False, f"{r_name}: Sorry, I cannot go outside my safe zone.", x_position, y_position


def back(command_2, r_name, x_position, y_position, direction):
    """Move the robot back then return the new x, y position."""

    new_x = x_position
    new_y = y_position

    if direction == 0:
        new_y -= abs(int(command_2))
    elif direction == 90:
        new_x -= abs(int(command_2))
    elif direction == 180:
        new_y += abs(int(command_2))
    elif direction == 270:
        new_x += abs(int(command_2))
    
    if position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, f"{r_name}: Sorry, there is an obstacle in the way.", x_position, y_position
    
    if limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, f" > {r_name} moved back by {abs(int(command_2))} steps.", x_position, y_position


    return False, f"{r_name}: Sorry, I cannot go outside my safe zone.", x_position, y_position

def right(r_name, direction):
    """Turn the robot right then return the new direction."""

    if direction == 0:
        direction = 90
    elif direction == 90:
        direction = 180
    elif direction == 180:
        direction = 270
    elif direction == 270:
        direction = 0

    return f" > {r_name} turned right.", direction


def left(r_name, direction):
    """Turn the robot left then return the new direction."""

    if direction == 0:
        direction = 270
    elif direction == 270:
        direction = 180
    elif direction == 180:
        direction = 90
    elif direction == 90:
        direction = 0

    return f" > {r_name} turned left.", direction


def show_position(r_name, x_position, y_position):

    print(f" > {r_name} now at position ({x_position},{y_position}).")

def sprint(command_2):
    """Does the calculations of sprint through recursion."""

    if command_2 < 1:
        return command_2

    return command_2 + sprint(command_2 - 1)


def sprint_display(command_2, r_name):
    """Print the output of sprint to the user."""

    for i in range(command_2):
        print(f" > {r_name} moved forward by {command_2 - i} steps.")


def sprint_command(r_name, command_2, x_position, y_position, direction):
    """Sprint the robot forward then return the new x, y position."""

    new_x = x_position
    new_y = y_position

    if direction == 0:
        new_y += sprint(int(command_2))
    elif direction == 90:
        new_x += sprint(int(command_2))
    elif direction == 180:
        new_y -= sprint(int(command_2))
    elif direction == 270:
        new_x -= sprint(int(command_2))
    
    if position_or_path_blocked(x_position, y_position, new_x, new_y):
        return False, f"{r_name}: Sorry, there is an obstacle in the way.", x_position, y_position
    
    if limit(new_x, new_y):
        x_position = new_x
        y_position = new_y
        return True, sprint_display(int(command_2), r_name), x_position, y_position
    
    return False, f"{r_name}: Sorry, I cannot go outside my safe zone.", x_position, y_position



