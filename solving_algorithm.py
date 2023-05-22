from zero_processing import get_box_number
from math import floor

def solve(user_input, possibility_matrix):
    has_update = True
    while(has_update):
        has_update = False
        row_counter = [[] for x in range(10) ]
        col_counter = [[] for x in range(10) ]
        box_counter = [[] for x in range(10) ]
        for i in range(9):
            for j in range(9):
                for k in range(len(possibility_matrix[i][j])):
                    row_counter[possibility_matrix[i][j][k]].append((i, j))
                for k in range(len(possibility_matrix[j][i])):
                    col_counter[possibility_matrix[j][i][k]].append((j, i))
                    
            for i in range(10):
                if len(row_counter[i]) == 1:
                    update_user_input(user_input, row_counter[i][0], i)
                    update_possible_values(possibility_matrix, row_counter[i][0], i)
                    has_update = True
                if len(col_counter[i]) == 1:
                    update_user_input(user_input, col_counter[i][0], i)
                    update_possible_values(possibility_matrix, col_counter[i][0], i)
                    has_update = True
                    
def update_user_input(user_input, zero_position, value):
    row = zero_position[0]
    col = zero_position[1]
    user_input[row] = user_input[row][:col] + str(value) + user_input[row][col+1:]

def update_possible_values(possibility_matrix, zero_position, value):
    row = zero_position[0]
    col = zero_position[1]
    box = get_box_number(row, col)
    possibility_matrix[row][col] = []
    for i in range(9):
        try:
            possibility_matrix[i][col].remove(value)
        except ValueError:
            pass
        try:
            possibility_matrix[row][i].remove(value)
        except ValueError:
            pass
    box_starting_row = floor(box/3) * 3
    box_starting_col = box%3 * 3
    for i in range(3):
        for j in range(3):
            try:
                possibility_matrix[box_starting_row+i][box_starting_col+j].remove(value)
            except ValueError:
                pass