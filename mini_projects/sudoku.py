"""
type error (suitable_step)
clear terminal
"""
import numpy as np
import os

def map_making() -> list:
    """
    Returns:
        list: 9x9 map filled up with starter values
    """
    #TODO handle infinite loop better
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
def empty_spaces(map : list) -> list:
    """
    Generates a list which contains every "x" character's indexes (row, column)
    Args:
        map (list): the sudoku map loaded with starter values

    Returns:
        list: list, which contains the indexes of empty spaces in smaller lists
    """
    empty_spaces = [] 
    for row_i, row in enumerate(map):
        for slice_i, slice in enumerate(row):
            for letter_i, letter in enumerate(slice):
                if letter == "x":
                    empty_spaces.append([row_i, (slice_i * 3 + letter_i)])
                else:
                    continue
    return empty_spaces
def suitable_step(given_row : int, given_column : int, given_number : int, map : list) -> bool:
    #TODO num != int
    #if type(num) != int: #because of the empty spaces ("x")
    #continue
    """
    Args:
        given_row (int): the row you want the put the number in
        given_column (int): the column you want the put the number in
        given_number (int): the given number
        map (list): the list, witch contains the 9x9 map
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
def win(map : list) -> bool:
    """

    Args:
        map (list): The sudoku map

    Returns:
        bool: True if you have won, false if you haven't completed it yet
    """
    if empty_spaces(map) == []:
        return True
    else:
        return False
def game() -> None:
    """
    The runable game, when you win, it stops
    Args:
    Returns:
        None: The game is over, you have won
    """
    #preparations
    map = map_making()
    empty_spaces_list = empty_spaces(map)
    print("Üdvözlöm a sudoku játékban!\nA játékban, mind a sorok, oszlopok és a beírni kivánt számok 1 és 9 között vannak, ezeket ennek megfelelően adja meg")
    
    game_end = False
    while game_end == False:
        
        #check if you have won
        if win(map) == True:
            print("Gratulálok, teljesítetted a sudokut!")
            game_end = True
            break
        
        #display map
        for row in map: 
            row_elements = ""
            for slice in row:
                for num in slice:
                    row_elements += f"{num} "
            print(f"{row_elements}")
        
        #ask in the values
        given_number = input("Adjon meg egy számot vagy az x karaktert az üres mezőhöz! ")
        #TODO type
        player_given_place = str(input("Adja meg elősször a sor, majd az oszlop számát, egy vesszővel elválasztva! "))
        given_place = [int(player_given_place[0]) - 1, int(player_given_place[-1]) - 1]
        
        #check if the values are right
        if given_number not in [1, 2, 3, 4, 5, 6, 7, 8, 9, "x"] and given_place[0] not in [1, 2, 3, 4, 5, 6, 7, 8, 9] and given_place[1] not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            raise ValueError["Nem megfelelő számot adott meg, indítsa újra a játékot"]

        #manage the step
        if given_place in empty_spaces_list: #check if it's a starter field
            if suitable_step(given_place[0], given_place[1], given_number, map) == True: #chek if the step is right TODO
                map[given_place[0]][given_place[1] // 3][given_place[1] % 3] = given_number #make the step
            else:
                continue #wrong step already printed in suitable_step
        else:
            print("Ezt a mezőt nem változtathatod meg, válassz egy másikat")
        
        
    
    next_game = str(input("Akarsz még egyet játszani? (Igen/Nem) "))
    if next_game == "Igen":
        game()
    else:
        pass
     
if __name__ == "__main__":
    game()

"""test_map = [
            [[5, 3, 4], [6, 7, 8], [9, 1, 2]],
            [[6, 7, 2], [1, 9, 5], [3, 4, 8]],
            [[1, 9, 8], [3, 4, 2], [5, 6, 7]],
            [[8, 5, 9], [7, 6, 1], [4, 2, 3]],
            [[4, 2, 6], [8, 5, 3], [7, 9, 1]],
            [[7, 1, 3], [9, 2, 4], [8, 5, 6]],
            [[9, 6, 1], [5, 3, 7], [2, 8, 4]],
            [[2, 8, 7], [4, 1, 9], [6, 3, 5]],
            [[3, 4, 5], [2, 8, 6], [1, 7, 9]]
              ]"""