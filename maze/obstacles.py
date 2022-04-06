import random


obstacle_list = []

def get_obstacles():
    global obstacle_list
    obstacle_list = []
    ran_obs = random.randint(1, 11)
    for i in range(ran_obs):
        x_pos = random.randint(-100, 101)
        y_pos = random.randint(-200, 201)
        tuple_ = (x_pos, y_pos)

        while tuple_ in obstacle_list:
            x_pos = random.randint(-100, 101)
            y_pos = random.randint(-200, 201)
            tuple_ = (x_pos, y_pos)

        obstacle_list.append(tuple_)

    return obstacle_list

def is_position_blocked(x,y):

    for position_tuple in obstacle_list:

        if (position_tuple[0] <= x <= (position_tuple[0]+4)) and (position_tuple[1]\
            <= y <= (position_tuple[1]+4)):

            return True

    return False


def  is_path_blocked(x1,y1, x2, y2):

    for position_tuple in obstacle_list:
        if (y1 < position_tuple[1] < y2 and position_tuple[0] <= x1 <=\
            (position_tuple[0]+4)) or (x1 < position_tuple[0] < x2 and\
            position_tuple[1] <= y1 <= (position_tuple[1]+4)):

            return True

    return False