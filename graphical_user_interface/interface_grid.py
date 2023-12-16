import numpy as np
import cv2

from graphical_user_interface import constants
from graphical_user_interface import interface_cell as ic

class Grid():
    '''This class represents the grid of the sudoku. It is composed of cells.
    The grid is represented by a numpy array of cells.
    The grid is completed when all the cells have a value.
    
    Attributes : 
        main_coordinates : list[int]
        list_cells_origin : list[list[int]]
        cells : np.ndarray
        completed : bool

    Methods :
        draw_grid : draw the grid on the screen
        draw_lines : draw the main lines of the grid
        draw_cells : draw the cells of the grid
        create_cells : create the cells of the grid
        display_digits_grid : display the digits of the grid 
        is_completed : check if the grid is completed
        display_completion : display the message "Sudoku Completed" if the grid is completed
    '''

    def __init__(self, list_cells_origin :list[list[int]]):
        self.main_coordinates = constants.MAIN_GRID_COORDINATES
        self.list_cells_origin = list_cells_origin
        self.cells = np.ndarray((constants.MAIN_GRID_SIZE, constants.MAIN_GRID_SIZE), dtype=ic.Cell)
        self.completed = False
        self.create_cells()
    
    def draw_grid(self, screen: np.ndarray) -> None:
        '''Draw the grid on the screen and the empty cells'''
        # Draw the cells
        self.draw_cells(screen, constants.CELLS_COLOR, constants.CELLS_THICKNESS, constants.CELL_TRANSPARENCY)

        # Draw the main grid
        cv2.rectangle(screen,(self.main_coordinates[0], self.main_coordinates[2]), (self.main_coordinates[1], self.main_coordinates[3]), constants.MAIN_GRID_COLOR, constants.MAIN_GRID_THICKNESS)

        # Draw the main lines
        sqrt_sudoku_size = int(np.sqrt(constants.MAIN_GRID_SIZE))
        self.draw_lines(screen, sqrt_sudoku_size, constants.MAIN_LINES_COLOR, constants.MAIN_LINES_THICKNESS)

        # Draw the other lines
        self.draw_lines(screen, constants.MAIN_GRID_SIZE, constants.OTHER_LINES_COLOR, constants.OTHER_LINES_THICKNESS)

    def draw_lines(self, screen : np.ndarray, size : int, color : tuple[int], thickness : int) -> None:
        '''Draw the main lines of the grid'''
        for i in range(size + 1):
            x = self.main_coordinates[0] + i * (self.main_coordinates[1] - self.main_coordinates[0]) // size
            y = self.main_coordinates[2] + i * (self.main_coordinates[3] - self.main_coordinates[2]) // size
            cv2.line(screen, (x, self.main_coordinates[2]), (x, self.main_coordinates[3]), color, thickness)
            cv2.line(screen, (self.main_coordinates[0], y), (self.main_coordinates[1], y), color, thickness)

    def draw_cells(self, screen : np.ndarray, color : tuple[int], thickness : int, transparency : float) -> None:
        '''Draw the cells of the grid'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                xmin = self.main_coordinates[0] + i * (self.main_coordinates[1] - self.main_coordinates[0]) // constants.MAIN_GRID_SIZE
                xmax = self.main_coordinates[0] + (i + 1) * (self.main_coordinates[1] - self.main_coordinates[0]) // constants.MAIN_GRID_SIZE
                ymin = self.main_coordinates[2] + j * (self.main_coordinates[3] - self.main_coordinates[2]) // constants.MAIN_GRID_SIZE
                ymax = self.main_coordinates[2] + (j + 1) * (self.main_coordinates[3] - self.main_coordinates[2]) // constants.MAIN_GRID_SIZE
                screen1 = screen.copy()
                cv2.rectangle(screen1, (xmin, ymin), (xmax, ymax), color, thickness)
                cv2.addWeighted(screen1, transparency, screen, 1 - transparency, 0, screen)

    def create_cells(self) -> None:
        '''Create the objects "cell" of the grid'''
        # Check the size of the input list
        if len(self.list_cells_origin) != constants.MAIN_GRID_SIZE :
            raise ValueError("The number of rows of the input list is not correct : {} instead of {}".format(len(self.list_cells_origin), constants.MAIN_GRID_SIZE))
        if len(self.list_cells_origin[0]) != constants.MAIN_GRID_SIZE :
            raise ValueError("The number of columns of the input list is not correct : {} instead of {}".format(len(self.list_cells_origin[0]), constants.MAIN_GRID_SIZE))
        
        # Create the cells
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                if self.list_cells_origin[i][j] != 0:
                    self.cells[i][j] = ic.Cell((i, j), self.list_cells_origin[i][j], True)
                else:
                    self.cells[i][j] = ic.Cell((i, j))

    def display_digits_grid(self, screen : np.ndarray) -> None:
        '''Display the digits of the grid'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                self.cells[i][j].display_cell(screen)


    def is_completed(self) -> bool:
        '''Check if the grid is completed'''
        for rows in self.cells:
            for cell in rows:
                if cell.value is None:
                    return False
        return True
    
    def display_completion(self, screen : np.ndarray) -> None:
        '''Display the message "Sudoku Completed" if the grid is completed'''
        if self.is_completed():
            cv2.putText(screen, "Sudoku Completed ! \n Congrats ! ", (constants.WIDTH_CAMERA//2 - 50, constants.HEIGHT_CAMERA//2), cv2.FONT_HERSHEY_SIMPLEX, constants.COMPLETION_FONTSCALE, constants.COMPLETION_COLOR, constants.COMPLETION_THICKNESS, cv2.LINE_AA)