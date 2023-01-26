"""
Generation class module
"""

from cell import Cell
from random import randint
import os


class Generation:
    def __init__(self, rows: int, columns: int):
        """
        Generation class to accept number or Rows, Columns
        """

        # Class Attributes
        self.rows = rows
        self.columns = columns
        self.grid = [
            [Cell() for column in range(self.columns)]  # pyright: ignore
            for row in range(self.rows)  # pyright: ignore
        ]
        self.grid_str = ""

        self.generate_board()

    def draw_board(self):
        os.system("clear")
        print()
        for row in self.grid:
            for column in row:
                print(column.get_symbol(), end="")
            print()

    def generate_board(self):
        for row in self.grid:
            for column in row:
                cell_poll = bool(randint(0, 1))
                if cell_poll:
                    column.set_alive()

    def update_board(self):
        alive = []
        killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                neighbors = self.get_neighbor(row, column)

                living_neighbors = []
                for neighbor in neighbors:
                    if neighbor.is_alive():
                        living_neighbors.append(neighbor)
                current_cell = self.grid[row][column]

                if current_cell.is_alive():
                    if len(living_neighbors) < 2 or len(living_neighbors) > 3:
                        killed.append(current_cell)

                    if len(living_neighbors) == 3 or len(living_neighbors) == 2:
                        alive.append(current_cell)
                else:
                    if len(living_neighbors) == 3:
                        alive.append(current_cell)

        for item in alive:
            item.set_alive()

        for item in killed:
            item.set_dead()

    def get_neighbor(self, n_row: int, n_column: int) -> list:

        # Search settings
        _min = -1
        _max = 2

        neighbors = []

        for row in range(_min, _max):
            for column in range(_min, _max):
                neighbor_row = n_row + row
                neighbor_col = n_column + column

                valid_neighbor = True

                if (neighbor_row) == n_row and (neighbor_col) == n_column:
                    valid_neighbor = False

                if (neighbor_row) < 0 or (neighbor_row) >= self.rows:
                    valid_neighbor = False

                if (neighbor_col) < 0 or (neighbor_col) >= self.columns:
                    valid_neighbor = False

                if valid_neighbor:
                    neighbors.append(self.grid[neighbor_row][neighbor_col])
        return neighbors

    def to_str(self) -> str:
        """Class method to convert the board to string"""
        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                self.grid_str += str(self.grid[row][column].get_symbol())
            self.grid_str += "\n"

        return self.grid_str

    # Operator Overloading
    def __eq__(self, other: object) -> bool:
        if self.grid == other.grid:
            return True
        else:
            return False
