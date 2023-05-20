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