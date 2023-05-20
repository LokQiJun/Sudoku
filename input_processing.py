from math import floor

sample_flags = [False, False, False, False, False, False, False, False, False, False]

def row_checks(user_input):
    compiled_checks = []
    for i in range(9):
        row_flags = sample_flags.copy()
        for j in range(9):
            element = int(user_input[i][j])
            if element != 0 and row_flags[element] == True:
                exit("There is clashing entry on row " + str(i+1))
            row_flags[element] = True
        compiled_checks.append(row_flags)
    return compiled_checks

def column_checks(user_input):
    compiled_checks = []
    for i in range(9):
        column_flags = sample_flags.copy()
        for j in range(9):
            element = int(user_input[j][i])
            if element != 0 and column_flags[element] == True:
                exit("There is clashing entry on column " + str(i+1))
            column_flags[element] = True
        compiled_checks.append(column_flags)
    return compiled_checks

def get_box_number(rol, col):
    row_num = floor(rol/3)
    col_num = floor(col/3)
    return row_num * 3 + col_num

def box_checks(user_input):
    compiled_checks = []
    for i in range(9):
        box_flags = sample_flags.copy()
        compiled_checks.append(box_flags)
    for i in range(9):
        for j in range(9):
            box_num = get_box_number(i, j)
            element = int(user_input[i][j])
            if element != 0 and compiled_checks[box_num][element] == True:
                exit("There is clashing entry on box " + str(box_num+1))
            compiled_checks[box_num][element] = True
    return compiled_checks

def find_zero_locations(user_input):
    zero_locations = []
    for i in range(9):
        for j in range(9):
            if user_input[i][j] == '0':
                zero_locations.append([i, j])
    return zero_locations