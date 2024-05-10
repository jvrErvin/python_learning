from pathlib import Path

import imageio
import matplotlib.pyplot as plt
import numpy as np


def create_gif_from_plots(output_folder: Path, gif_name: str = "simulation.gif", fps: float = 10):
    """
    Reads all the plots from the specified folder and creates a GIF.

    Parameters:
        output_folder (Path): The path to the folder containing the image files.
        gif_name (str): The name of the resulting GIF file.
        fps (float): The frames per second for the GIF (default is 10).
    """
    image_files = output_folder.glob("*.png")
    image_files = sorted(image_files, key=lambda x: int(x.stem.split("_")[-1]))
    images = [imageio.v2.imread(file) for file in image_files]

    # Save the images as a GIF
    gif_path = output_folder / gif_name
    imageio.mimsave(gif_path, images, duration=1 / fps)

    print(f"GIF saved at {gif_path}")


def plot_grid(grid: np.ndarray, timestep: int, target_folder: Path):
    """
    Create and save a plot of the grid to the specified folder.

    Parameters:
        grid (np.ndarray): The grid to plot.
        timestep (int): The current timestep, used for naming the file.
        target_folder (Path): The folder where the image will be saved.
    """
    # Create a new figure and axes for the plot
    fig, ax = plt.subplots(figsize=(10, 10))  # Set the figure size

    # Plot the grid on the axes
    ax.imshow(grid)
    ax.set_xticks([])  # Hide the x-axis ticks
    ax.set_yticks([])  # Hide the y-axis ticks
    ax.set_title(f"Conway's Game of Life at Timestep {timestep}")

    # File path for saving the image
    filepath = target_folder / f"timestep_{timestep}.png"
    plt.savefig(filepath)
    plt.close(fig)  # Close the figure to free up memory


def glider_gun_grid(N: int, states: list[int]) -> np.ndarray:
    """
    Generate an NxN grid initialized with a Gosper glider gun.

    Parameters:
        N (int): Size of the grid, must be at least 40.
        states (list[int]): List of possible states for a cell (e.g., [0, 1]).
    Returns:
        np.ndarray: NxN grid with the Gosper glider gun initialized.
    """
    alive, dead = states
    grid = np.zeros((N, N), dtype=int)  # Create an empty grid

    # Define the positions of the 'alive' cells in the Gosper glider gun
    # Adjusted for position to be roughly centered or at a suitable starting point
    gun = np.array(
        [
            (5, 1),
            (5, 2),
            (6, 1),
            (6, 2),
            (5, 11),
            (6, 11),
            (7, 11),
            (4, 12),
            (8, 12),
            (3, 13),
            (9, 13),
            (3, 14),
            (9, 14),
            (6, 15),
            (4, 16),
            (8, 16),
            (5, 17),
            (6, 17),
            (7, 17),
            (6, 18),
            (3, 21),
            (4, 21),
            (5, 21),
            (3, 22),
            (4, 22),
            (5, 22),
            (2, 23),
            (6, 23),
            (1, 25),
            (2, 25),
            (6, 25),
            (7, 25),
            (3, 35),
            (4, 35),
            (3, 36),
            (4, 36),
        ]
    )

    # Place the glider gun on the grid
    for (x, y) in gun:
        if x < N and y < N:
            grid[x, y] = alive

    return grid


def random_grid(N: int, states: list[int], p: list[float]) -> np.ndarray:
    """
    Generate a random NxN grid

    Args:
        N (int): Size of the grid
        states (list[int]): List of possible states for a cell (e.g., [0, 1])
        p (list[float]): Sampling probabilities for the states
    Returns:
        np.ndarray: NxN grid with random states
    """
    return np.random.choice(states, N * N, p=p).reshape(N, N)


def set_boundary(
    grid: np.ndarray, boundary_condition: str, N: int, states: list[int], p: list[float] = [0.5, 0.5]
) -> np.ndarray:
    """
    Set the boundary condition for the grid

    Args:
        grid (np.ndarray): The grid
        boundary_condition (str): The boundary condition to set
        N (int): Size of the grid
        states (list[int]): List of possible states for a cell (e.g., [0, 1])
        p (list[float]): Sampling probabilities for the states (default is [0.5, 0.5])
    Returns:
        np.ndarray: Grid with the boundary condition set
    """
    alive, dead = states
    if boundary_condition == "dead":
        grid[0, :] = dead
        grid[N + 1, :] = dead
        grid[:, 0] = dead
        grid[:, N + 1] = dead
    elif boundary_condition == "alive":
        grid[0, :] = alive
        grid[N + 1, :] = alive
        grid[:, 0] = alive
        grid[:, N + 1] = alive
    elif boundary_condition == "periodic":
        # Side Wrapping
        grid[0, 1:-1] = grid[N, 1:-1]
        grid[N + 1, 1:-1] = grid[1, 1:-1]
        grid[1:-1, 0] = grid[1:-1, N]
        grid[1:-1, N + 1] = grid[1:-1, 1]

        # Corner Wrapping
        grid[0, 0] = grid[N, N]
        grid[0, N + 1] = grid[N, 1]
        grid[N + 1, 0] = grid[1, N]
        grid[N + 1, N + 1] = grid[1, 1]
    elif boundary_condition == "random":
        # Randomly choose the state for the top and bottom rows
        grid[0, :] = np.random.choice(states, N + 2, p=p)
        grid[N + 1, :] = np.random.choice(states, N + 2, p=p)

        # Randomly choose the state for the first and last columns (excluding the already set corners)
        grid[1 : N + 1, 0] = np.random.choice(states, N, p=p)
        grid[1 : N + 1, N + 1] = np.random.choice(states, N, p=p)
    return grid


def count_alive_neighbors(grid: np.ndarray, i: int, j: int) -> int:
    """
    Count the number of alive neighbors of a cell and also add the cell's state

    Args:
        grid (np.ndarray): The grid
        i (int): Row index of the cell
        j (int): Column index of the cell
    Returns:
        int: Number of alive neighbors
    """
    return (
        grid[i][j + 1]
        + grid[i][j - 1]
        + grid[i + 1][j]
        + grid[i - 1][j]
        + grid[i - 1][j + 1]
        + grid[i - 1][j - 1]
        + grid[i + 1][j + 1]
        + grid[i + 1][j - 1]
    )


if __name__ == "__main__":
    # States of a cell
    alive = 1
    dead = 0
    states = [alive, dead]

    N = 60  # Size of the grid
    n = 2  # Number of neighbors for a cell to be alive/dead in the next generation
    boundary_condition = "dead"  # "dead" or "periodic" or "alive" or "random"
    T = 301  # Number of timesteps to simulate
    t = 0  # Initial time
    p_alive_dead_sampling = [0.5, 0.5]  # Sampling probabilities for alive and dead cells
    initial_state = "glidergun"  # "random" or "glidergun"

    output_folder = Path("./9_simulation_output")
    output_folder.mkdir(exist_ok=True, parents=True)

    if initial_state == "random":
        grid = random_grid(N + 2, states, p_alive_dead_sampling)
    elif initial_state == "glidergun":
        grid = glider_gun_grid(N + 2, states)
    else:
        ValueError("Invalid initial state")

    grid = set_boundary(grid, boundary_condition, N, states)

    while t < T:
        plot_grid(grid=grid, timestep=t, target_folder=output_folder)

        grid_new = grid.copy()
        for i_row in range(1, N + 1):
            for i_col in range(1, N + 1):
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

    create_gif_from_plots(output_folder=output_folder, gif_name="simulation.gif", fps=1)
    
