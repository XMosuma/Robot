import turtle
import time
import sys

x_position = 0
y_position = 0
direction = 0

min_x,max_x = -100, 100
min_y,max_y = -200, 200

if 'play_ground' in sys.argv:
    import maze.play_ground as pos
    size = 12
    turtle.bgcolor('black')
    turtle.title('play_ground')
    turtle.setworldcoordinates(-100,-200,100,200)
    turtle.tracer(2)  
else:
    import maze.obstacles as pos 
    turtle.bgcolor('black')
    turtle.title('obstacles')
    size = 4


x = turtle.Turtle()

def draw_obstacles(obstacles):
    """
    draws the obstacles
    """
    pen = turtle.Turtle()
    for i in obstacles:
        
        x_position = i[0] 
        y_position = i[1]
        x.penup()
        x.begin_fill()
        x.fillcolor('blue')
        x.goto(x_position,y_position)
        x.pendown()
        x.goto(x_position+size,y_position)
        x.goto(x_position+size,y_position+size)
        x.goto(x_position,y_position+size)
        x.goto(x_position,y_position)
        x.penup()
        x.end_fill()
    turtle.tracer(1)
    x.color('green','red')
    x.home()
    x.setheading(90)

def draw_turtle_screen():
    """
    draws the border of the turtle screen
    """
    
    x.penup()
    x.goto(-100,200)

    x.pendown()
    x.color('yellow','brown')

    x.fd(200)
    x.rt(90)

    x.fd(400)
    x.rt(90)

    x.fd(200)
    x.rt(90)

    x.fd(400)

    x.penup()
    x.goto(0,0)

   
    x.home()
    x.setheading(90)

def turn_robot(direction):
    if direction == 0:
        x.setheading(90)
    elif direction == 90:
        x.setheading(0)
    elif direction == 180:
        x.setheading(270)
    elif direction == 270:
        x.setheading(180)


def move_robot(x_position, y_position):

    x.goto(x_position, y_position)


def move_robot_in_maze(maze_list):
    for position in maze_list:
        x.pendown()
        x.pensize(7)
        x.goto(position)
    x.penup()
    return position




def position_or_path_blocked(x_position, y_position, new_x, new_y):

    return pos.is_position_blocked(new_x,new_y) or pos.is_path_blocked(x_position,y_position, new_x, new_y)


def limit(new_x, new_y):
    """Checks if the robot is within the range"""

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


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
        move_robot(x_position, y_position)
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
        move_robot(x_position, y_position)
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
    
    turn_robot(direction)

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
    
    turn_robot(direction)

    return f" > {r_name} turned left.", direction

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
        move_robot(x_position, y_position)
        return True, sprint_display(int(command_2), r_name), x_position, y_position

    return False, f"{r_name}: Sorry, I cannot go outside my safe zone.", x_position, y_position


