def print_all_possibilities(zero_positions):
    for i in range(len(zero_positions)):
        print(zero_positions[i])
        
def print_all_flags(flag_list, identifier):
    print(identifier, ": ")
    for i in range(len(flag_list)):
        print(flag_list[i])  