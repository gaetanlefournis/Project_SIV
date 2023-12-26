import cv2
import numpy as np

from graphical_user_interface import constants

class Cell():
    '''This class represents a cell of the sudoku. It is composed of a value and coordinates.
    
    Attributes :
        position_in_grid : tuple[int]
        value : int
        initial : bool
        is_drawn : bool
        is_active : bool
        size_cell : int
        coordinates : tuple[int]

    Methods :
        calculate_size_cell : calculate the size of a cell
        calculate_coordinates : calculate the coordinates of the cell
        display_cell : display a number in a given cell
        is_clicked : check if a cell is clicked
        erase_cell : erase the number in a given cell
    '''

    def __init__(self, position_in_grid : tuple[int], value : int = None, initial : bool = False):
        self.position_in_grid = position_in_grid
        self.value = value
        self.initial = initial
        self.is_drawn = False
        self.is_active = False
        self.size_cell = self.calculate_size_cell()
        self.coordinates = self.calculate_coordinates()

    def calculate_size_cell(self) -> int:
        '''Calculate the size of a cell'''
        return (constants.MAIN_GRID_COORDINATES[1] - constants.MAIN_GRID_COORDINATES[0]) // constants.MAIN_GRID_SIZE

    def calculate_coordinates(self) -> None:
        '''Calculate the coordinates of the cell'''
        return (constants.MAIN_GRID_COORDINATES[0] + self.position_in_grid[1]*(constants.MAIN_GRID_COORDINATES[1] - constants.MAIN_GRID_COORDINATES[0])//constants.MAIN_GRID_SIZE, constants.MAIN_GRID_COORDINATES[0] + (self.position_in_grid[1] + 1)*(constants.MAIN_GRID_COORDINATES[1] - constants.MAIN_GRID_COORDINATES[0])//constants.MAIN_GRID_SIZE, constants.MAIN_GRID_COORDINATES[2] + self.position_in_grid[0]*(constants.MAIN_GRID_COORDINATES[3] - constants.MAIN_GRID_COORDINATES[2])//constants.MAIN_GRID_SIZE, constants.MAIN_GRID_COORDINATES[2] + (self.position_in_grid[0] + 1)*(constants.MAIN_GRID_COORDINATES[3] - constants.MAIN_GRID_COORDINATES[2])//constants.MAIN_GRID_SIZE)

    def display_cell(self, screen : np.ndarray) -> None:
        '''Display a number in a given cell'''
        if self.value is not None:
            if self.initial : 
                color = constants.INITIAL_DIGITS_COLOR
            else:
                color = constants.OTHER_DIGITS_COLOR
            cv2.putText(screen, str(self.value), (self.coordinates[0] + int(2/5*self.size_cell), self.coordinates[2] + int(3/5*self.size_cell)), cv2.FONT_HERSHEY_SIMPLEX, constants.DIGITS_FONTSCALE, color, constants.DIGITS_THICKNESS, cv2.LINE_AA)
            self.is_drawn = True

    def is_clicked(self, coordinates_click : tuple[int]) -> bool:
        '''Check if a cell is clicked. An ititial cell cannot be clicked'''
        if coordinates_click[0] >= self.coordinates[0] and coordinates_click[0] < self.coordinates[1] and coordinates_click[1] >= self.coordinates[2] and coordinates_click[1] < self.coordinates[3] and not self.initial:
            return True
        else:
            return False

    def erase_cell(self):
        '''Erase the number in a given cell'''
        self.value = None
        self.is_drawn = False

