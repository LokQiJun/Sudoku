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
    possibility_matrix = zp(row_flags, column_flags, box_flags, zero_locations)
    # print_status(10000, zero_locations, row_flags, column_flags, box_flags, possibility_matrix)
    solve(user_input, possibility_matrix)
    print_status(10000, zero_locations, row_flags, column_flags, box_flags, possibility_matrix)
    print_output_list(user_input)
    
if __name__ == "__main__":
    main()
    
'''
Algorithm
Save as 2D matrix
Get all unused value for row, column and box
Get all possible value for each 0
Create 9x9 matrix of list (overall 3D matrix) append possible values to location of zero
implement a counter list to travel row by row, column by column & box by box
'''