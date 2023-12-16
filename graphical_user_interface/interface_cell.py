import cv2
import numpy as np

from graphical_user_interface import constants

class Cell():
    '''This class represents a cell of the sudoku. It is composed of a value and coordinates.
    
    Attributes :
        coordinates : tuple[int]
        value : int
        initial : bool
        is_drawn : bool
        
    Methods :
        display_cell : display a number in a given cell
        erase_cell : erase the number in a given cell
    '''

    def __init__(self, coordinates : tuple[int], value : int = None, initial : bool = False):
        self.coordinates = coordinates
        self.value = value
        self.initial = initial
        self.is_drawn = False

    def display_cell(self, screen : np.ndarray) -> None:
        '''Display a number in a given cell'''
        if not self.is_drawn:
            if self.value is not None:
                if self.initial : 
                    color = constants.INITIAL_DIGITS_COLOR
                else:
                    color = constants.OTHER_DIGITS_COLOR
                cv2.putText(screen, str(self.value), (constants.MAIN_GRID_COORDINATES[0] + int((self.coordinates[1] + 2/5)*(constants.MAIN_GRID_COORDINATES[1] - constants.MAIN_GRID_COORDINATES[0])//constants.MAIN_GRID_SIZE), constants.MAIN_GRID_COORDINATES[2] + int((self.coordinates[0] + 3/5)*(constants.MAIN_GRID_COORDINATES[3] - constants.MAIN_GRID_COORDINATES[2])//constants.MAIN_GRID_SIZE)), cv2.FONT_HERSHEY_SIMPLEX, constants.DIGITS_FONTSCALE, color, constants.DIGITS_THICKNESS, cv2.LINE_AA)

    def erase_cell(self, screen):
        '''Erase the number in a given cell'''
        pass
