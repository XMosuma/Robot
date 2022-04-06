obstacle_list = []

def get_obstacles():
    global obstacle_list

    obstacle_list = []

    obstacle_maze = [
"+++++++++ +++++++",
"++++          +++",
"+++++   ++ ++  ++",
"++    ++++ ++ +++",
"+  ++  +  ++  +++",
"+  +   +   + + ++",
"++++   +  ++    +",
"+  +   +  +++++++",
"   +  ++        +",
"+      +  ++   ++",
"+  ++  +  ++++  +",
"+  +++    ++   ++",
"+  ++     ++++ ++",
"++    +++       +",
"+       +       +",
"+  ++  ++ +++++++",
"+  +++ +        +",
"+  ++  +  ++  +++",
"+  ++++  ++++++++",
"+++++++   +++++++",
"++++             ",
"+++++   ++ ++  ++",
"++    ++++ ++ +++",
"+  ++  +  ++  +++",
"+  +   +   + + ++",
"++++   +  ++    +",
"+  +   +  +++++++",
"+  +  ++        +",
"+      +  ++   ++",
"+  ++  +  ++++  +",
"+      +  ++   ++",
"+  ++  +  ++++  +",
"+ +++++++++++++++"]
    x = -103
    y = 188
    for obs in obstacle_maze:
        for obs_ in obs:
            if obs_ == "+":
                tuple_ = (x, y)
                obstacle_list.append(tuple_)
            x += 12
        x = -103
        y -= 12

    return obstacle_list

size = 12

def is_position_blocked(x,y):

    for position_tuple in obstacle_list:

        if (position_tuple[0] <= x <= (position_tuple[0]+size)) and (position_tuple[1]\
            <= y <= (position_tuple[1]+size)):

            return True

    return False


def  is_path_blocked(x1,y1, x2, y2):

    for position_tuple in obstacle_list:
        if (y1 < position_tuple[1] < y2 and position_tuple[0] <= x1 <=\
            (position_tuple[0]+size)) or (x1 < position_tuple[0] < x2 and\
            position_tuple[1] <= y1 <= (position_tuple[1]+size)):

            return True

    return False