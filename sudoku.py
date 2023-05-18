import input_processing as ip
from file_reader import get_user_input
        
def print_output_list(user_input):    
    print ("Output:")
    print (*user_input, sep="\n")

def main():
    user_input = get_user_input()
    row_flags = ip.row_checks(user_input)
    column_flags = ip.column_checks(user_input)
    box_flags = ip.box_checks(user_input)
    # print(row_flags)
    # print(column_flags)
    # print(box_flags)

if __name__ == "__main__":
    main()
    
'''
Algorithm
Save as 2D matrix
Create array of size 81 that store possible values in empty squares
For all '0', check row, column and box
'''