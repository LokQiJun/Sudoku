def print_status(zero_locations, row_flags, column_flags, box_flags):
    print_all_possibilities(zero_locations)
    print_all_flags(row_flags, "row")
    print_all_flags(column_flags, "column")
    print_all_flags(box_flags, "box")

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