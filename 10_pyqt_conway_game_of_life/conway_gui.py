import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QLabel, QLineEdit, QPushButton, QComboBox, 
                             QWidget, QFormLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap

class GameOfLifeGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Conway\'s Game of Life')
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QHBoxLayout(self.central_widget)
        self.visualization_label = QLabel()
        main_layout.addWidget(self.visualization_label)

        control_layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.input_N = QLineEdit('60')
        self.input_n = QLineEdit('2')
        self.input_T = QLineEdit('200')
        self.input_t = QLineEdit('0')
        self.input_p_alive = QLineEdit('0.5')
        self.input_p_dead = QLineEdit('0.5')

        self.boundary_condition = QComboBox()
        self.boundary_condition.addItems(['random', 'dead', 'periodic', 'alive'])

        self.initial_state = QComboBox()
        self.initial_state.addItems(['glidergun', 'random'])

        self.form_layout.addRow('Grid Size (N):', self.input_N)
        self.form_layout.addRow('Neighbors (n):', self.input_n)
        self.form_layout.addRow('Timesteps (T):', self.input_T)
        self.form_layout.addRow('Current Time (t):', self.input_t)
        self.form_layout.addRow('Probability Alive:', self.input_p_alive)
        self.form_layout.addRow('Probability Dead:', self.input_p_dead)
        self.form_layout.addRow('Boundary Condition:', self.boundary_condition)
        self.form_layout.addRow('Initial State:', self.initial_state)

        self.start_button = QPushButton('Start Simulation')
        self.start_button.clicked.connect(self.start_simulation)

        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self.close)

        control_layout.addLayout(self.form_layout)
        control_layout.addWidget(self.start_button)
        control_layout.addWidget(self.exit_button)

        main_layout.addLayout(control_layout)

    def start_simulation(self):
        N = int(self.input_N.text())
        n = int(self.input_n.text())
        T = int(self.input_T.text())
        t = int(self.input_t.text())
        p_alive = float(self.input_p_alive.text())
        p_dead = float(self.input_p_dead.text())
        boundary_condition = self.boundary_condition.currentText()
        initial_state = self.initial_state.currentText()

        self.simulate(N, n, T, t, p_alive, p_dead, boundary_condition, initial_state)

    def simulate(self, N, n, T, t, p_alive, p_dead, boundary_condition, initial_state):
        alive = 1
        dead = 0
        states = [alive, dead]
        p_alive_dead_sampling = [p_alive, p_dead]

        if initial_state == 'random':
            grid = self.random_grid(N + 2, states, p_alive_dead_sampling)
        elif initial_state == 'glidergun':
            grid = self.glider_gun_grid(N + 2, states)
        else:
            raise ValueError("Invalid initial state")

        grid = self.set_boundary(grid, boundary_condition, N, states)

        self.t = t
        self.T = T
        self.N = N
        self.n = n
        self.grid = grid
        self.boundary_condition = boundary_condition
        self.states = states

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_simulation)
        self.timer.start(100)

    def update_simulation(self):
        if self.t < self.T:
            self.plot_grid(self.grid, self.t)
            grid_new = self.grid.copy()
            for i_row in range(1, self.N + 1):
                for i_col in range(1, self.N + 1):
                    alive_neighbors = self.count_alive_neighbors(self.grid, i_row, i_col)
                    if self.grid[i_row][i_col] == 1 and alive_neighbors < self.n:
                        grid_new[i_row][i_col] = 0
                    if self.grid[i_row][i_col] == 1 and (alive_neighbors == self.n or alive_neighbors == self.n + 1):
                        grid_new[i_row][i_col] = 1
                    if self.grid[i_row][i_col] == 1 and alive_neighbors > self.n + 1:
                        grid_new[i_row][i_col] = 0
                    if self.grid[i_row][i_col] == 0 and alive_neighbors == self.n + 1:
                        grid_new[i_row][i_col] = 1
            self.grid = grid_new
            self.grid = self.set_boundary(self.grid, self.boundary_condition, self.N, self.states)
            self.t += 1
        else:
            self.timer.stop()

    def plot_grid(self, grid, timestep):
        image = QImage(grid.shape[1], grid.shape[0], QImage.Format_RGB888)
        for x in range(grid.shape[1]):
            for y in range(grid.shape[0]):
                color = 0 if grid[y, x] == 0 else 255
                image.setPixel(x, y, color << 16 | color << 8 | color)
        pixmap = QPixmap.fromImage(image)
        self.visualization_label.setPixmap(pixmap)

    def random_grid(self, N, states, p):
        return np.random.choice(states, N * N, p=p).reshape(N, N)

    def glider_gun_grid(self, N, states):
        alive, dead = states
        grid = np.zeros((N, N), dtype=int)
        gun = np.array(
            [
                (5, 1), (5, 2), (6, 1), (6, 2), (5, 11), (6, 11), (7, 11),
                (4, 12), (8, 12), (3, 13), (9, 13), (3, 14), (9, 14),
                (6, 15), (4, 16), (8, 16), (5, 17), (6, 17), (7, 17),
                (6, 18), (3, 21), (4, 21), (5, 21), (3, 22), (4, 22),
                (5, 22), (2, 23), (6, 23), (1, 25), (2, 25), (6, 25),
                (7, 25), (3, 35), (4, 35), (3, 36), (4, 36)
            ]
        )
        for (x, y) in gun:
            if x < N and y < N:
                grid[x, y] = alive
        return grid

    def set_boundary(self, grid, boundary_condition, N, states, p=[0.5, 0.5]):
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
            grid[0, 1:-1] = grid[N, 1:-1]
            grid[N + 1, 1:-1] = grid[1, 1:-1]
            grid[1:-1, 0] = grid[1:-1, N]
            grid[1:-1, N + 1] = grid[1:-1, 1]
            grid[0, 0] = grid[N, N]
            grid[0, N + 1] = grid[N, 1]
            grid[N + 1, 0] = grid[1, N]
            grid[N + 1, N + 1] = grid[1, 1]
        elif boundary_condition == "random":
            grid[0, :] = np.random.choice(states, N + 2, p=p)
            grid[N + 1, :] = np.random.choice(states, N + 2, p=p)
            grid[1:N + 1, 0] = np.random.choice(states, N, p=p)
            grid[1:N + 1, N + 1] = np.random.choice(states, N, p=p)
        return grid

    def count_alive_neighbors(self, grid, i, j):
        return (
            grid[i][j + 1] + grid[i][j - 1] + grid[i + 1][j] + grid[i - 1][j] +
            grid[i - 1][j + 1] + grid[i - 1][j - 1] + grid[i + 1][j + 1] + grid[i + 1][j - 1]
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameOfLifeGUI()
    ex.show()
    sys.exit(app.exec_())
