from email import message
import re
import sys

command_run = sys.argv

maze = False

if "play_ground" in command_run:
    import maze.play_ground as obs
else:
    import maze.obstacles as obs

if "turtle" in command_run:
    import world.turtle.world as world
    import mazerun.mazerun as mazerun
    maze = True

else:
    import world.text.world as world
    import mazerun.mazerun as mazerun
    maze = True





def get_robot_name():
    """Get the robot name, greet the user and return the name."""

    name = input("What do you want to name your robot? ")
    print(f"{name}: Hello kiddo!")
    return name


def validate_the_command(command, robot_name):
    """Checks if the command is valid."""

    valid_command = ["off", "help", "forward", "back", "right",
    "left", "sprint", "history", "replay", "replay silent",
    "replay reversed", "replay reversed silent", "mazerun",
    "mazerun top", "mazerun bottom", "mazerun left", "mazerun right"]


    return_value = False

    if command == []:
        return False

    user_command = " ".join(list(filter(lambda word: word.isalpha(), command)))
    user_num = "".join((filter(lambda num: not num.isalpha(), command)))
    if user_num == "":
        if user_command.lower() in valid_command:
            return_value =  True
    elif user_num.isdigit():
        if user_command.lower() in valid_command and user_num.isdigit():
            return_value = True
    elif len(user_num.split("-")) > 1 and user_num.count('-') == 1:
        if user_command.lower() in valid_command and "".join(user_num.split("-")).isdigit():
            return_value =  True
    
    if return_value == False:
        if type(command) == list:
            print(f"{robot_name}: Sorry, I did not understand '{' '.join(command)}'.")
        else:
            print(f"{robot_name}: Sorry, I did not understand '{command}'.")
        return False
    else:
        return True


def get_command(robot_name):
    """Get the command from the user and return it as list."""

    command = input(f"{robot_name}: What must I do next? ")

    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:+=,.]')
     
    if string_check.search(command) == None:
        comm_list = command.split()
        if command == "forward" and len(comm_list) == 1:
            comm_list.append("0")
        elif command == "back" and len(comm_list) == 1:
            comm_list.append("0")
        elif command == "sprint" and len(comm_list) == 1:
            comm_list.append("0")

        return comm_list
    else:
        return command


def shutdown(robot_name, user_command, user_num):
    """[summary]"""

    if user_command == "off" and not user_num.isdigit():
        print(f"{robot_name}: Shutting down..")
        return True
    else:
        return False


def do_help():
    """Displays the info to the user."""

    return "I can understand these commands:\n\
OFF  - Shut down robot\n\
HELP - provide information about commands\n\
FORWARD - move the robot forward\n\
BACK - move the robot backward\n\
RIGHT - turn the robot right\n\
LEFT - turn the robot left\n\
SPRINT - sprint the robot\n\
HISTORY - displays history of commands\n\
REPLAY - replay the movement commands\n\
REPLAY SILENT - replay of the commands without showing output\n\
REPLAY REVERSED - play back the commands in reverse order\n\
REPLAY REVERSED SILENT - play back the commands in reverse without showing output\n\
MAZERUN — the robot figure out a short path to any end of the maze.\n"


def history(history_list):
    """Shows history of commands to the user."""
    return history_list


def replay_command(user_command, replay_list, robot_name, user_num, x_position, y_position, direction):
    """Replay all the commands the user has used then returns
    the new x, y position and direction."""

    n = len(replay_list)
    m = 0

    if user_num.isdigit():
        n = int(user_num)

    elif len(user_num.split("-")) > 1:
        comm_list = user_num.split("-")
        n = int(comm_list[0])
        m = int(comm_list[1])

    if "reversed" in user_command:
        replay_list.reverse()

    if m == 0:
        replay_list = replay_list[-n:]
    else:
        replay_list = replay_list[-n:-m]

    for commands in replay_list:
        if commands[0] == "forward":
            do_next, command_output, x_position, y_position = world.forward(int(commands[1]), robot_name, x_position, y_position, direction)

            if do_next == False:
                print(command_output)
                if 'turtle' not in command_run :
                    world.show_position(robot_name, x_position, y_position)
                continue

            if "silent" not in user_command:
                print(command_output)

        elif commands[0] == "back":
            do_next,command_output,x_position,y_position = world.back(int(commands[1]),\
            robot_name,x_position, y_position, direction)

            if do_next == False:
                print(command_output)
                if 'turtle' not in command_run :
                    world.show_position(robot_name,x_position,y_position)
                continue

            if "silent" not in user_command:
                print(command_output)

        elif commands[0] == "right":
            command_output, direction = world.right(robot_name, direction)

            if "silent" not in user_command:
                print(command_output)

        elif commands[0] == "left":
            command_output, direction = world.left(robot_name, direction)

            if "silent" not in user_command:
                print(command_output)

        elif commands[0] == "sprint":
            do_next, command_output, x_position, y_position = world.sprint_command(robot_name, int(commands[1]), x_position, y_position, direction)
            if do_next == False:
                print(command_output)
                if 'turtle' not in command_run :
                    world.show_position(robot_name, x_position, y_position)
                continue

            if "silent" not in user_command:
                command_output
        
        if 'turtle' not in command_run and "silent" not in user_command :
            world.show_position(robot_name, x_position, y_position)

    if user_command == "replay":
        print(f" > {robot_name} replayed {len(replay_list)} commands.")
    elif user_command == "replay silent":
        print(f" > {robot_name} replayed {len(replay_list)} commands silently.")
    elif user_command == "replay reversed":
        print(f" > {robot_name} replayed {len(replay_list)} commands in reverse.")
    elif user_command == "replay reversed silent":
        print(f" > {robot_name} replayed {len(replay_list)} commands in reverse silently.")
    
    return x_position, y_position, direction
    


def handler_command(command, robot_name, history, replay_list, do_next, x_position, y_position, direction):
    """Runs all the commands.
    """
    
    user_command = " ".join(list(filter(lambda word: word.isalpha(), command))).lower()
    user_num = "".join((filter(lambda num: not num.isalpha(), command)))
    command_2 = 0

    if shutdown(robot_name, user_command, user_num):
        return False, history, replay_list, x_position, y_position, direction

    if user_num.isdigit():
        command_2 = int(user_num)
    
    if user_command == "mazerun" or user_command == "mazerun top"\
    or user_command == "mazerun bottom" or user_command == "mazerun left"\
    or user_command == "mazerun right":

        if len(user_command.split()) == 2:
            maze_direction = user_command.split()[1]
        else:
            maze_direction = ""
            
        print(f"> {robot_name} starting maze run..")
        solution_list, msg = mazerun.maze_run(robot_name, x_position, y_position, direction, maze_direction)
        
        if 'turtle' in command_run:
            position_ = world.move_robot_in_maze(solution_list)
            x_position, y_position = position_[0], position_[1]
        print(msg)
        return True, history, replay_list, x_position, y_position, direction
    
    elif user_command == "forward":
        do_next, command_output, x_position, y_position = world.forward(command_2, robot_name, x_position, y_position, direction)

        if do_next == False:
            print(command_output)
            if 'turtle' not in command_run :
                world.show_position(robot_name, x_position, y_position)
            return True, history, replay_list, x_position, y_position, direction

        print(command_output)

        replay_list.append((command))
        history.append(" ".join(command))

    elif user_command == "sprint":
        do_next, command_output, x_position, y_position = world.sprint_command(robot_name, command_2, x_position, y_position, direction)
        if do_next == False:
            print(command_output)
            if 'turtle' not in command_run :
                world.show_position(robot_name, x_position, y_position)
            return True, history, replay_list, x_position, y_position, direction
        
        command_output

        replay_list.append((command))
        history.append(" ".join(command))

    elif user_command == "back":
        do_next, command_output, x_position, y_position = world.back(command_2, robot_name, x_position, y_position, direction)
        if do_next == False:
            print(command_output)
            if 'turtle' not in command_run :
                world.show_position(robot_name, x_position, y_position)
            return True, history, replay_list, x_position, y_position, direction
        
        print(command_output)

        replay_list.append((command))
        history.append(" ".join(command))
    
    elif "replay" in user_command:
        x_position,y_position,direction = replay_command(user_command,replay_list,\
        robot_name,user_num, x_position,y_position,direction)

        history.append(" ".join(command))
    
    elif user_command == "right" and not user_num.isdigit():
        command_output, direction = world.right(robot_name, direction)
        print(command_output)

        history.append(" ".join(command))
        replay_list.append((command))

    elif user_command == "left" and not user_num.isdigit():
        command_output, direction = world.left(robot_name, direction)
        print(command_output)

        replay_list.append((command))
        history.append(" ".join(command))

    elif user_command == "history" and not user_num.isdigit():
        history(history)

    elif user_command == "help" and not user_num.isdigit():
        print(do_help())
        history.append(" ".join(command))

    else:
        print(f"{robot_name}: Sorry, I did not understand '{' '.join(command)}'.")
    
    if 'turtle' not in command_run :
        world.show_position(robot_name, x_position, y_position)
    
    return True, history, replay_list, x_position, y_position, direction


def robot_start():
    """Main function that runs the whole game."""

    robot_name =get_robot_name()
    x_position = world.x_position
    y_position = world.y_position
    direction = world.direction
    history = []
    replay_list = []
    do_next = True
    obstacle_list = obs.get_obstacles()

    if len(obstacle_list) > 0:

        if 'turtle' in command_run:

            if 'play_ground' in command_run:

                print(f"{robot_name}: Loaded play_ground.")
            else:
                print(f"{robot_name}: Loaded obstacles.")
                world.draw_turtle_screen() 

            world.draw_obstacles(obstacle_list)

        else:
            if 'play_ground' in command_run:
                print(f"{robot_name}: Loaded play_ground.")
            else:
                print(f"{robot_name}: Loaded obstacles.")
            world.show_obstacles()

    while do_next:
        command = get_command(robot_name)
        
        if validate_the_command(command,robot_name) == False:
            continue

        do_next,history,replay_list,x_position,y_position,direction =\
        handler_command(command,robot_name,history,replay_list,do_next,x_position,y_position,direction)


if __name__ == "__main__":
    robot_start()
