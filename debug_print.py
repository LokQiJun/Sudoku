def print_status(flag, zero_locations, row_flags, column_flags, box_flags, possibility_matrix):
    if flag%10 == 1:
        print_all_possibilities(zero_locations)
    flag = flag/10
    if flag%10 == 1:
        print_all_flags(row_flags, "row")
    flag = flag/10
    if flag%10 == 1:
        print_all_flags(column_flags, "column")
    flag = flag/10
    if flag%10 == 1:
        print_all_flags(box_flags, "box")
    flag = flag/10
    if flag%10 == 1:
        print_possibility_matrix(possibility_matrix)

def print_all_possibilities(zero_positions):
    for i in range(len(zero_positions)):
        print(zero_positions[i])
        
def print_all_flags(flag_list, identifier):
    print("\n\n", identifier, ": ")
    for i in range(len(flag_list)):
        print(f"\n {i+1}: ", end = "")
        for j in range(1, len(flag_list[i])):
            if flag_list[i][j] == True:
                print(j, end = " ")

def print_possibility_matrix(possibility_matrix):
    print("Possibility Matrix:")
    for i in range(len(possibility_matrix)):
        print(possibility_matrix[i])