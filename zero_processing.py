import numpy as np
from itertools import repeat
from input_processing import get_box_number

def get_all_possible_values(row_flags, column_flags, box_flags, zero_positions):
    
    possibility_matrix = [[[] for x in range(9)] for x in range(9) ]
    
    for i in range(len(zero_positions)):
        possible_values = get_possible_value(row_flags, column_flags, box_flags, 
                                             zero_positions[i][0], zero_positions[i][1])
        # zero_positions[i].append(possible_values)
        possibility_matrix[zero_positions[i][0]][zero_positions[i][1]].extend(possible_values)
        
    return possibility_matrix
    
def get_possible_value(row_flags, column_flags, box_flags, row, column):
    overall_flags = np.logical_or(np.logical_or(row_flags[row], column_flags[column]), 
                                  box_flags[get_box_number(row, column)])
    
    possible_values = []
    for i in range (len(overall_flags)):
        if overall_flags[i] == False:
            possible_values.append(i)
    return possible_values