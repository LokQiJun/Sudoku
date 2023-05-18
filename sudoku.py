from file_reader import get_user_input
import input_processing as ip
import zero_processing as zp
import debug_print as dp
        
def print_output_list(user_input):    
    print ("Output:")
    print (*user_input, sep="\n")

def main():
    user_input = get_user_input()
    row_flags = ip.row_checks(user_input)
    column_flags = ip.column_checks(user_input)
    box_flags = ip.box_checks(user_input)
    zero_locations = ip.find_zero_locations(user_input)
    zp.get_all_possible_values(row_flags, column_flags, box_flags, zero_locations)
    dp.print_all_possibilities(zero_locations)
    dp.print_all_flags(row_flags, "row")
    dp.print_all_flags(column_flags, "column")
    dp.print_all_flags(box_flags, "box")
    

if __name__ == "__main__":
    main()
    
'''
Algorithm
Save as 2D matrix
Create array of size 81 that store possible values in empty squares
For all '0', check row, column and box
'''