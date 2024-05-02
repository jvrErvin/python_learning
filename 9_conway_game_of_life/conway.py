import numpy as np
import matplotlib.pyplot as plt
import random as rand

# TODO: implement the glider gun grid
def glider_gun_grid(N: int, states: list[int]) -> np.ndarray:
    """
    Generate glider gun grid
    """
    """
    ........................O
    ......................O.O
    ............OO......OO............OO
    ...........O...O....OO............OO
    OO........O.....O...OO
    OO........O...O.OO....O.O
    ..........O.....O.......O
    ...........O...O
    ............OO
    """
    dead_grip = np.ndarray()
    dead_grip.resize(N*N)
    dead_grip.fill(states[1])
    pass

def random_grid(N: int, states: list[int], p: list[float]) -> np.ndarray:
    """
    Generate a random NxN grid
    """
    return np.random.choice(states, N*N, p=p).reshape(N, N)

def set_boundary(grid: np.ndarray, boundary_condition: str, N: int, states: list[int]) -> np.ndarray:
    """
    Set the boundary condition for the grid
    """
    alive, dead = states
    if boundary_condition == "dead":
        for i in range(0, N+2):
            grid[0][i]   = dead
            grid[N+1][i] = dead
            grid[i][0]   = dead
            grid[i][N+1] = dead
    elif boundary_condition == "alive":
        for i in range(0, N+2):
            grid[0][i]   = alive
            grid[N+1][i] = alive
            grid[i][0]   = alive
            grid[i][N+1] = alive
    elif boundary_condition == "periodic":
        grid[0][i]   = grid[-2][i]
        grid[N+1][i] = grid[1][i]
        grid[i][0]   = grid[i][-2]
        grid[i][N+1] = dead[i][1]
    elif boundary_condition == "random":
        for i in range(0, N+2):
            if rand.randint(1,2) % 2:
                grid[0][i]   = dead
            else:
                grid[0][i]   = alive
            if rand.randint(1,2) % 2:
                grid[N+1][i]   = dead
            else:
                grid[N+1][i]   = alive
            if rand.randint(1,2) % 2:
                grid[i][0]   = dead
            else:
                grid[i][0]   = alive
            if rand.randint(1,2) % 2:
                grid[i][N+1]   = dead
            else:
                grid[i][N+1]   = alive
    return grid

def count_alive_neighbors(grid: np.ndarray, i: int, j: int) -> int:
    """
    Count the number of alive neighbors of a cell and also add the cell's state
    """
    return  grid[i][j+1] + grid[i][j-1] + grid[i+1][j] + grid[i-1][j] + grid[i-1][j+1] + grid[i-1][j-1] + grid[i+1][j+1] + grid[i+1][j-1]


if __name__ == "__main__":
     # States of a cell
    alive  = 1
    dead   = 0
    states = [alive, dead]

    N = 6                              # Size of the grid
    n = 2                              # Number of neighbors for a cell to be alive/dead in the next generation
    boundary_condition = "dead"        # "dead" or "periodic" or "alive" or "random"
    T = 20                             # Number of timesteps to simulate
    t = 0                              # Initial time
    p_alive_dead_sampling = [0.5, 0.5] # Sampling probabilities for alive and dead cells
    initial_state = "random"           # "random" or "glidergun"
    
    if initial_state == "random":
        grid = random_grid(N+2, states, p_alive_dead_sampling)
    elif initial_state == "glidergun":
        grid = glider_gun_grid()    
        
    grid = set_boundary(grid, boundary_condition, N, states)

    while t < T:
        print(f"Time: {t}")
        print(grid) # TODO: instead of printing, do some matplotlib visualisation / gif
        
        grid_new = grid.copy()
        for i_row in range(1, N+1):
            for i_col in range(1, N+1):
                alive_neighbors = count_alive_neighbors(grid, i_row, i_col)
                
                # Rule 1: Any live cell with fewer than `n` live neighbors dies, as if by underpopulation.
                if grid[i_row][i_col] == alive and alive_neighbors < n:
                    grid_new[i_row][i_col] = dead
                # Rule 2: Any live cell with `n` or `n+1` live neighbors lives on to the next generation.
                if grid[i_row][i_col] == alive and (alive_neighbors == n or alive_neighbors == n + 1):
                    grid_new[i_row][i_col] = alive
                # Rule 3: Any live cell with more than `n+1` live neighbors dies, as if by overpopulation.
                if grid[i_row][i_col] == alive and alive_neighbors > n + 1:
                    grid_new[i_row][i_col] = dead
                # Rule 4: Any dead cell with exactly `n+1` live neighbors becomes a live cell, as if by reproduction.
                if grid[i_row][i_col] == dead and alive_neighbors == n + 1:
                    grid_new[i_row][i_col] = alive
            
        t += 1
        grid = grid_new
        grid = set_boundary(grid, boundary_condition, N, states)
        
