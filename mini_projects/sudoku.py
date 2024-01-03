"""
9x9 map
1 difficulty
def wrong step
def win
type error
playable
outpot/print looks normal
player given numbers -1!!!!!!!!!!!!!!!!!
"""
import numpy as np
import os

def map_making():
    #TODO handleinfinite loop better
    map = [
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]],
            [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
        ]
    # index be like --> row(0-8), slice(0-2), column(0-2)
    # overall 81 space
    
    for row_i, row in enumerate(map):
        #go row by row and add random amount of letter
        for slice_i, slice in enumerate(row):
            for letter_i, letter in enumerate(slice):
                if np.random.randint(1, 4, 1)[0] % 2: # decide to write a number or leave the space empty
                    placed = False
                    while placed != True:
                        random_num = np.random.randint(1, 10, 1)[0]
                        if suitable_step(row_i, slice_i * 3 + letter_i, random_num, map) == True:
                            map[row_i][slice_i][letter_i] = random_num
                            attempts = 0
                            placed = True
                        elif attempts == 10:
                            placed = True
                        else:
                            attempts += 1
                else:
                    pass
    os.system("cls") #clear terminal
    return map
def suitable_step(given_row : int, given_column : int, given_number : int, map):
    #TODO num != int
    #if type(num) != int: #because of the empty spaces ("x")
    #continue
    """
    Args:
        given_row (int): the row you want the put the number in
        given_column (int): the column you want the put the number in
        given_number (int): the given number

    Returns:
        Bool: True if the step is right, False if the step is wrong
    """
    
    #check 3x3 slice
    need_to_check_rows = []
    need_to_check_slice = None
    
    if given_row in [0, 1, 2]:
        need_to_check_rows = [0, 2]
    elif given_row in [3, 4, 5]:
        need_to_check_rows = [3, 5]
    elif given_row in [6, 7, 8]:
        need_to_check_rows = [6, 8]
    else:
        raise ValueError("Wrong number in the siutability check") #már be is bizonyosult az error használatának fontossága
    if given_column in [0, 1, 2]:
        need_to_check_slice = 0
    elif given_column in [3, 4, 5]:
        need_to_check_slice = 1
    elif given_column in [6, 7, 8]:
        need_to_check_slice = 2
    else:
        raise ValueError("Wrong number in the siutability check")
           
    for row in map[need_to_check_rows[0]:need_to_check_rows[-1]]:
        for num in row[need_to_check_slice]:
                if num == given_number:
                    print(f" A 3x3-as már szerepel a megadott szám ({given_number})")
                    return False    

   
    #check column
    for row in map:
        if row[(given_column // 3)][given_column % 3] == given_number:
            print(f"Az oszlopban már szerepel a megadott szám ({given_number})")
            return False  

   
    #check row
    for slice in map[given_row]:
        for num in slice:
            if num == given_number:
                print(f"A sorban már szerepel a megadott szám ({given_number})")
                return False
  
    return True
if __name__ == "__main__":
    map = map_making()
    foo = 0