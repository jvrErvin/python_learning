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

def map_making():
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
                    if np.random.randint(1, 6, 1)[0] % 2: # decide to write a number or leave the space empty
                        placed = False
                        while placed != True:
                            random_num = np.random.randint(1, 10, 1)[0]
                            if wrong_step(row_i, slice_i * 3 + letter_i, random_num, map) == False:
                                map[row_i][slice_i][letter_i] = random_num
                                placed = True
                        #TODO drop out wrong values, disable print
                    else:
                        pass
        return map
def wrong_step(given_row : int, given_column : int, given_number : int, map):
    """
    Args:
        given_row (int): the row you want the put the number in
        given_column (int): the column you want the put the number in
        given_number (int): the given number

    Returns:
        Bool: True if the step is wrong, False if the step is right
    """
    
    #check 3x3 slice
    need_to_check_rows = []
    need_to_check_slice = None
    
    if given_row in [1, 2, 3]:
        need_to_check_rows = [0, 1, 2]
    elif given_row in [4, 5, 6]:
        need_to_check_rows = [3, 4, 5]
    else:
        need_to_check_rows = [6, 7, 8]
    if given_column in [1, 2, 3]:
        need_to_check_slice = 0
    elif given_column in [4, 5, 6]:
        need_to_check_slice = 1
    else:
        need_to_check_slice = 2
    
    for row in map[need_to_check_rows[0]:need_to_check_rows[-1]]:
        for num in row[need_to_check_slice]:
            if type(num) != int: #because of the empty spaces ("x")
                continue
            else:
                if num == given_number:
                    print(f" A 3x3-as már szerepel a megadott szám ({given_number})")
                    return False
    #TODO
    
    #check column
    for row in map:
        if row[(given_column // 3)][given_column % 3] == given_number:
            print(f"Az oszlopban már szerepel a megadott szám ({given_number})")
            return False
    #TODO
    
    #check row
    for row in map:
            for slice in row:
                for num in slice:
                    if type(num) != int: #because of the empty spaces ("x")
                        continue
                    else:
                        if num == given_number:
                            print(f"A sorban már szerepel a megadott szám ({given_number})")
                            return False 
            #TODO check
    
    

if __name__ == "__main__":
    map = map_making()
    foo = 0