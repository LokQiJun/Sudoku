from zero_processing import get_box_number
from math import floor
from debug_print import print_possibility_matrix as printm

def solve(user_input, pm):
    has_update = True
    dir_row = get_direction_flag("row")
    dir_col = get_direction_flag("col")
    while(has_update):
        has_update = False
        row_counter_list = []
        col_counter_list = []
        for i in range(9):
            row_counter = [[] for x in range(10) ]
            col_counter = [[] for x in range(10) ]
            for j in range(9):
                if len(pm[i][j]) == 1:
                    has_update = update_value(user_input, pm, (i,j), pm[i][j][0])
                else:
                    for k in range(len(pm[i][j])):
                        row_counter[pm[i][j][k]].append((i, j))
                if len(pm[j][i]) == 1:
                    has_update = update_value(user_input, pm, (j,i), pm[j][i][0])
                else:
                    for k in range(len(pm[j][i])):
                        col_counter[pm[j][i][k]].append((j, i))
            
            row_counter_list.append(row_counter)
            col_counter_list.append(col_counter)
            
            for j in range(10):
                if len(row_counter[j]) == 1:
                    has_update = update_value(user_input, pm, row_counter[j][0], j)
                if len(col_counter[j]) == 1:
                    has_update = update_value(user_input, pm, col_counter[j][0], j)
                    
        if has_update == False:
            for i in range(9):
                has_update = locate_hidden_subset(pm, row_counter_list[i], i, dir_row)
                has_update = locate_hidden_subset(pm, col_counter_list[i], i, dir_col)
      
def locate_hidden_subset(possibility_matrix, counters, num, dir):
    print(dir)
    print(counters)
    
    values = []
    pos = []
    for i in range(len(counters)):
        if len(counters[i]) == 2:
            values.append(i)
            pos.append(counters[i])
    length = len(pos)
    if length == 2:
        return False
    for i in range(length):
        for j in range(i+1, length - i):
            if counters[i] == counters[j]:
                print("Locating Subset")
                printm(possibility_matrix)
                if dir == get_direction_flag("row"):
                    update_possible_values(possibility_matrix, pos[i], num, -1, values[i], dir)
                    update_possible_values(possibility_matrix, pos[i], num, -1, values[j], dir)
                elif dir == get_direction_flag("col"):
                    update_possible_values(possibility_matrix, pos[i], -1, num, values[i], dir)
                    update_possible_values(possibility_matrix, pos[i], -1, num, values[j], dir)
                printm(possibility_matrix)
                print("Done")
                return True
    return False
            
def update_value(user_input, possibility_matrix, zero_position, value):
    row = zero_position[0]
    col = zero_position[1]
    possibility_matrix[row][col] = []
    direction = get_direction_flag("all")
    update_user_input(user_input, zero_position, value)
    update_possible_values(possibility_matrix, zero_position, row, col, value, direction)
    return True
                    
def update_user_input(user_input, zero_position, value):
    row = zero_position[0]
    col = zero_position[1]
    # print(f"Updating: row:{row} col:{col} with {value}")
    user_input[row] = user_input[row][:col] + str(value) + user_input[row][col+1:]

def update_possible_values(possibility_matrix, zero_position, row, col, value, direction):
    box = get_box_number(row, col)
    for i in range(9):
        if(i, col) not in zero_position and direction%2 == 1:
            try:
                possibility_matrix[i][col].remove(value)
            except ValueError:
                pass
        if(row, i) not in zero_position and (direction == 1 or direction == 4):
            try:
                possibility_matrix[row][i].remove(value)
            except ValueError:
                pass
    box_starting_row = floor(box/3) * 3
    box_starting_col = box%3 * 3
    for i in range(3):
        for j in range(3):
            if(box_starting_row+i, box_starting_col+j) not in zero_position and direction <= 2:
                try:
                    possibility_matrix[box_starting_row+i][box_starting_col+j].remove(value)
                except ValueError:
                    pass
                
def get_direction_flag(direction):
    return {
        'all': 1,
        'box': 2,
        'row': 3,
        'col': 4 
    }[direction]