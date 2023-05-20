from file_reader import get_user_input
from input_processing import input_checks
from zero_processing import get_all_possible_values as zp
from debug_print import print_status
from solving_algorithm import solve
        
def print_output_list(user_input):    
    print ("Output:")
    print (*user_input, sep="\n")

def main():
    user_input = get_user_input()
    row_flags, column_flags, box_flags, zero_locations = input_checks(user_input)
    zp(row_flags, column_flags, box_flags, zero_locations)
    # print_status(zero_locations, row_flags, column_flags, box_flags)
    solve(user_input, zero_locations)
    print_output_list(user_input)
    
if __name__ == "__main__":
    main()
    
'''
Algorithm
Save as 2D matrix
Create array of size 81 that store possible values in empty squares
For all '0', check row, column and box
'''