from math import floor

sample_flags = [False, False, False, False, False, False, False, False, False, False]

def row_checks(user_input):
    compiled_checks = []
    for i in range(9):
        row_flags = sample_flags.copy()
        for j in range(9):
            element = int(user_input[i][j])
            if element == 0:
                row_flags[element] = False
            else:
                row_flags[element] = True
        compiled_checks.append(row_flags)
    return compiled_checks

def column_checks(user_input):
    compiled_checks = []
    for i in range(9):
        column_flags = sample_flags.copy()
        for j in range(9):
            element = int(user_input[j][i])
            column_flags[element] = True
        compiled_checks.append(column_flags)
    return compiled_checks

def box_identifier(rol, col):
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
            box_num = box_identifier(i, j)
            element = int(user_input[j][i])
            compiled_checks[box_num][element] = True
    return compiled_checks
            