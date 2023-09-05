def make_grid(entry):
    global grid
    grid = list(grid)
    entry = list(entry)
    grid[12] = entry[0]
    grid[14] = entry[1]
    grid[16] = entry[2]
    grid[22] = entry[3]
    grid[24] = entry[4]
    grid[26] = entry[5]
    grid[32] = entry[6]
    grid[34] = entry[7]
    grid[36] = entry[8]
    grid = "".join(grid)
    print(grid)
    grid = list(grid)
    return grid
def row_check_X(grid):
    if grid[12] == 'X' and grid[14] == 'X' and grid[16] == 'X':
        return True
    elif grid[22] == 'X' and grid[24] == 'X' and grid[26] == 'X':
        return True
    elif grid[32] == 'X' and grid[34] == 'X' and grid[36] == 'X':
        return True
    elif grid[12] == 'X' and grid[22] == 'X' and grid[32] == 'X':
        return True
    elif grid[14] == 'X' and grid[24] == 'X' and grid[34] == 'X':
        return True
    elif grid[16] == 'X' and grid[26] == 'X' and grid[36] == 'X':
        return True
    elif grid[12] == 'X' and grid[24] == 'X' and grid[36] == 'X':
        return True
    elif grid[16] == 'X' and grid[24] == 'X' and grid[32] == 'X':
        return True
    else:
        return False
def row_check_O(grid):
    if grid[12] == 'O' and grid[14] == 'O' and grid[16] == 'O':
        return True
    elif grid[22] == 'O' and grid[24] == 'O' and grid[26] == 'O':
        return True
    elif grid[32] == 'O' and grid[34] == 'O' and grid[36] == 'O':
        return True
    elif grid[12] == 'O' and grid[22] == 'O' and grid[32] == 'O':
        return True
    elif grid[14] == 'O' and grid[24] == 'O' and grid[34] == 'O':
        return True
    elif grid[16] == 'O' and grid[26] == 'O' and grid[36] == 'O':
        return True
    elif grid[12] == 'O' and grid[24] == 'O' and grid[36] == 'O':
        return True
    elif grid[16] == 'O' and grid[24] == 'O' and grid[32] == 'O':
        return True
    else:
        return False
def check_empty(grid):
    if grid[12] == "_" or grid[14] == "_" or grid[16] == "_" or grid[22]  == "_" or grid[24] == "_" or grid[26] == "_" or grid[32] == "_" or grid[34] == "_" or grid[36] == "_":
        return True
    else:
        return False
def check_diff(grid):
    x = grid.count('X')
    o = grid.count('O')
    if x - o >= 2 or o - x >= 2:
        return True
    else:
        return False
def check_impossible(grid):
    if row_check_X(grid) == True  and row_check_O(grid) == True:
        return True
    elif check_diff(grid) == True:
        return True
    else:
        return False
def not_finished(grid):
    if row_check_X(grid) == False and row_check_O(grid) == False and check_empty(grid) == True:
        return True
    else:
        return False
def draw(grid):
    if row_check_X(grid) == False and row_check_O(grid) == False and check_empty(grid) == False:
        return True
    else:
        return False
def x_win(grid):
    if row_check_X(grid) == True and row_check_O(grid) == False:
        return True
    else:
        return False
def O_win(grid):
    if row_check_X(grid) == False and row_check_O(grid) == True:
        return True
    else:
        return False
def is_digit_ignore_space(move):
    # Remove spaces from the string
    s_without_spaces = move.replace(" ", "")

    # Check if the modified string contains only digits
    return s_without_spaces.isdigit()
def check_input(move):                                             
    if not is_digit_ignore_space(move):
        print('You Should enter numbers!')
        return True
    elif not move in ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']:         
        print("Coordinates should be from 1 to 3!")
        return True
    else:                                                          
        return False
def convert_dict(grid):                                            
    global new_dic                                                 
    global ind                                                     
    ind = [12, 14, 16, 22, 24, 26, 32, 34, 36]                     
    keys = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']                    
    new_dic ={keys[i] : grid[idx] for i,idx in enumerate(ind)}     
    return new_dic
def check_occupied(move):
    if new_dic[move] != "_":
        print(new_dic[move])
        return True
    else:
        return False
def replace_move_x(move):
    new_dic[move] = 'X'
    return new_dic
def replace_move_o(move):
    new_dic[move] = 'O'
    return new_dic
def update_grid(grid):
    new_list = list(new_dic.values())
    grid[12] = new_list[0]
    grid[14] = new_list[1]
    grid[16] = new_list[2]
    grid[22] = new_list[3]
    grid[24] = new_list[4]
    grid[26] = new_list[5]
    grid[32] = new_list[6]
    grid[34] = new_list[7]
    grid[36] = new_list[8]
    return grid
grid = '''---------
| _ _ _ |
| _ _ _ |
| _ _ _ |
---------'''
print(grid)
grid = list(grid)
move = input()
count = 0
while not any([x_win(grid), O_win(grid), draw(grid)]):
    count = count + 1
    convert_dict(grid)
    print(check_input(move))
    print(check_occupied(move))
    if count % 2 != 0:
        print(check_input(move))
        print(check_occupied(move))
        while check_input(move):
            move = input()
        print(count)
        print(new_dic)
        print(check_occupied(move))
        while check_occupied(move):
            print('This cell is occupied! Choose another one!')
            move = input()
        replace_move_x(move)
        update_grid(grid)
        print(''.join(grid))
    elif count % 2 == 0:
        while check_input(move):
            move = input()
        print(count)
        print(new_dic)
        print(check_occupied(move))
        while check_occupied(move):
            print('This cell is occupied! Choose another one!')
            move = input()
        replace_move_o(move)
        update_grid(grid)
        print(''.join(grid))

if x_win(grid):
    print('X wins')
elif O_win(grid):
    print('O wins')
elif draw(grid):
    print('Draw')
