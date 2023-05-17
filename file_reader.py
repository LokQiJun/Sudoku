INPUT_FILE = 'input.txt'

def is_correct_format(file_input):
    if(len(file_input)) != 9:
            print("WRONG NUM OF ROWS")
            return False
    for i in range(len(file_input)):
        if(len(file_input[i])) != 9:
            print("WRONG NUM OF INPUT ON ROW ", i+1)
            return False
        if(not file_input[i].isnumeric()):
            print("ROW ", i+1, " IS NOT NUMERIC")
    return True

def read_text_file():
    file_input = []
    with open(INPUT_FILE) as f:
        while True:
            line = f.readline()
            if not line:
                return file_input
            file_input.append(line.strip())
            
def get_user_input():
    user_input = read_text_file()
    if(not is_correct_format(user_input)):
        exit()
    return user_input