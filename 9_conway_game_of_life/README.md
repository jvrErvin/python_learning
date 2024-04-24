- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Rules:
- Any live cell with fewer than `n` live neighbors dies, as if by underpopulation.
- Any live cell with `n` or `n+1` live neighbors lives on to the next generation.
- Any live cell with more than `n+1` live neighbors dies, as if by overpopulation.
- Any dead cell with exactly `n+1` live neighbors becomes a live cell, as if by reproduction.