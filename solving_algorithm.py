from zero_processing import get_box_number

def solve(user_input, zero_locations):
    has_update = True
    while(has_update):
        has_update = False
        for i in range(len(zero_locations)):
            row = zero_locations[i][0]
            col = zero_locations[i][1]
            box = get_box_number(row, col)
            if(len(zero_locations[i][2]) == 1):
                value = zero_locations[i][2][0]
                user_input[row] = user_input[row][:col] + str(value) + user_input[row][col+1:]
                update_possible_values(zero_locations, row, col, box, value)
                has_update = True

def update_possible_values(zero_locations, row, col, box, value):
    for i in range(len(zero_locations)):
        current_col = zero_locations[i][1]
        current_row = zero_locations[i][0]
        current_box = get_box_number(current_row, current_col)
        if col == current_col or row == current_row or box == current_box:
            try:
                zero_locations[i][2].remove(value)
            except ValueError:
                pass