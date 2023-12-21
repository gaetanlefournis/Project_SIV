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
        self.draw_digit_is_active = False
        self.delete_cell_is_active = False
        self.validate_grid_is_active = False
        self.validate_digit_is_active = False
        self.erase_digit_is_active = False
        self.create_cells()

    def create_cells(self) -> None:
        '''Create the objects "cell" of the grid'''
        # Check the size of the input list
        if len(self.list_cells_origin) != constants.MAIN_GRID_SIZE :
            raise ValueError("The number of rows of the input list is not correct : {} instead of {}".format(len(self.list_cells_origin), constants.MAIN_GRID_SIZE))
        if len(self.list_cells_origin[0]) != constants.MAIN_GRID_SIZE :
            raise ValueError("The number of columns of the input list is not correct : {} instead of {}".format(len(self.list_cells_origin[0]), constants.MAIN_GRID_SIZE))
        
        # Create the objects cells
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                if self.list_cells_origin[i][j] != 0:
                    self.cells[i][j] = ic.Cell((i, j), self.list_cells_origin[i][j], True)
                else:
                    self.cells[i][j] = ic.Cell((i, j))
    
    def draw_grid(self, screen: np.ndarray) -> None:
        '''Draw the grid on the screen and the empty cells'''
        # Draw the cells
        self.draw_cells(screen, constants.CELLS_THICKNESS, constants.CELL_TRANSPARENCY)

        # Draw the main grid
        cv2.rectangle(screen,(self.main_coordinates[0], self.main_coordinates[2]), (self.main_coordinates[1], self.main_coordinates[3]), constants.MAIN_GRID_COLOR, constants.MAIN_GRID_THICKNESS)

        # Draw the main lines
        sqrt_sudoku_size = int(np.sqrt(constants.MAIN_GRID_SIZE))
        self.draw_lines(screen, sqrt_sudoku_size, constants.MAIN_LINES_COLOR, constants.MAIN_LINES_THICKNESS)

        # Draw the other lines
        self.draw_lines(screen, constants.MAIN_GRID_SIZE, constants.OTHER_LINES_COLOR, constants.OTHER_LINES_THICKNESS)

        # Draw the buttons of the sudoku interface
        self.draw_buttons_sudoku(screen)

    def draw_lines(self, screen : np.ndarray, size : int, color : tuple[int], thickness : int) -> None:
        '''Draw the main lines of the grid'''
        for i in range(size + 1):
            x = self.main_coordinates[0] + i * (self.main_coordinates[1] - self.main_coordinates[0]) // size
            y = self.main_coordinates[2] + i * (self.main_coordinates[3] - self.main_coordinates[2]) // size
            cv2.line(screen, (x, self.main_coordinates[2]), (x, self.main_coordinates[3]), color, thickness)
            cv2.line(screen, (self.main_coordinates[0], y), (self.main_coordinates[1], y), color, thickness)

    def draw_cells(self, screen : np.ndarray, thickness : int, transparency : float) -> None:
        '''Draw the cells of the grid'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                xmin = self.main_coordinates[0] + i * (self.main_coordinates[1] - self.main_coordinates[0]) // constants.MAIN_GRID_SIZE
                xmax = self.main_coordinates[0] + (i + 1) * (self.main_coordinates[1] - self.main_coordinates[0]) // constants.MAIN_GRID_SIZE
                ymin = self.main_coordinates[2] + j * (self.main_coordinates[3] - self.main_coordinates[2]) // constants.MAIN_GRID_SIZE
                ymax = self.main_coordinates[2] + (j + 1) * (self.main_coordinates[3] - self.main_coordinates[2]) // constants.MAIN_GRID_SIZE
                screen1 = screen.copy()
                if self.cells[j][i].is_active:
                    color = constants.CELLS_COLOR_ACTIVE
                else:
                    color = constants.CELLS_COLOR
                cv2.rectangle(screen1, (xmin, ymin), (xmax, ymax), color, thickness)
                cv2.addWeighted(screen1, transparency, screen, 1 - transparency, 0, screen)

    def draw_button_validate_grid(self, screen : np.ndarray) -> None:
        '''Draw the button "Validate grid"'''
        screen1 = screen.copy()
        if self.validate_grid_is_active:
            color_text = constants.BUTTON_VALIDATE_GRID_TEXT_COLOR_ACTIVE
            transparency = constants.BUTTONS_TRANSPARENCY_ACTIVE
        else:
            color_text = constants.BUTTON_VALIDATE_GRID_TEXT_COLOR_INACTIVE
            transparency = constants.BUTTONS_TRANSPARENCY_INACTIVE
        cv2.rectangle(screen1,((constants.BUTTON_VALIDATE_GRID_COORDINATES[0], constants.BUTTON_VALIDATE_GRID_COORDINATES[2])), ((constants.BUTTON_VALIDATE_GRID_COORDINATES[1], constants.BUTTON_VALIDATE_GRID_COORDINATES[3])), constants.BUTTON_VALIDATE_GRID_COLOR, constants.BUTTONS_THICKNESS)
        cv2.addWeighted(screen1, transparency, screen, 1 - transparency, 0, screen)
        cv2.putText(screen, constants.BUTTON_VALIDATE_GRID_TEXT, (self.main_coordinates[1] + int(1/20*(constants.WIDTH_CAMERA - self.main_coordinates[1])) + int(2/20*(constants.WIDTH_CAMERA - self.main_coordinates[1])), self.main_coordinates[2] + int(13/56*(self.main_coordinates[3] - self.main_coordinates[2]))), cv2.FONT_HERSHEY_SIMPLEX, constants.BUTTONS_FONTSCALE, color_text, constants.BUTTONS_TEXT_THICKNESS, cv2.LINE_AA)

    def draw_button_draw_digit(self, screen : np.ndarray) -> None:
        '''Draw the button "Draw digit"'''
        screen1 = screen.copy()
        if self.draw_digit_is_active:
            color_text = constants.BUTTON_DRAW_DIGIT_TEXT_COLOR_ACTIVE
            transparency = constants.BUTTONS_TRANSPARENCY_ACTIVE
        else:
            color_text = constants.BUTTON_DRAW_DIGIT_TEXT_COLOR_INACTIVE
            transparency = constants.BUTTONS_TRANSPARENCY_INACTIVE
        cv2.rectangle(screen1,(constants.BUTTON_DRAW_DIGIT_COORDINATES[0], constants.BUTTON_DRAW_DIGIT_COORDINATES[2]), (constants.BUTTON_DRAW_DIGIT_COORDINATES[1], constants.BUTTON_DRAW_DIGIT_COORDINATES[3]), constants.BUTTON_DRAW_DIGIT_COLOR, constants.BUTTONS_THICKNESS)
        cv2.addWeighted(screen1, transparency, screen, 1 - transparency, 0, screen)
        cv2.putText(screen, constants.BUTTON_DRAW_DIGIT_TEXT, (self.main_coordinates[1] + int(1/20*(constants.WIDTH_CAMERA - self.main_coordinates[1])) + int(2/20*(constants.WIDTH_CAMERA - self.main_coordinates[1])), self.main_coordinates[2] + int(29/56*(self.main_coordinates[3] - self.main_coordinates[2]))), cv2.FONT_HERSHEY_SIMPLEX, constants.BUTTONS_FONTSCALE, color_text, constants.BUTTONS_TEXT_THICKNESS, cv2.LINE_AA)

    def draw_button_delete_cell(self, screen : np.ndarray) -> None:
        '''Draw the button "Delete cell"'''
        screen1 = screen.copy()
        if self.delete_cell_is_active:
            color_text = constants.BUTTON_DELETE_CELL_TEXT_COLOR_ACTIVE
            transparency = constants.BUTTONS_TRANSPARENCY_ACTIVE
        else:
            color_text = constants.BUTTON_DELETE_CELL_TEXT_COLOR_INACTIVE
            transparency = constants.BUTTONS_TRANSPARENCY_INACTIVE
        cv2.rectangle(screen1,(constants.BUTTON_DELETE_CELL_COORDINATES[0], constants.BUTTON_DELETE_CELL_COORDINATES[2]), (constants.BUTTON_DELETE_CELL_COORDINATES[1], constants.BUTTON_DELETE_CELL_COORDINATES[3]), constants.BUTTON_DELETE_CELL_COLOR, constants.BUTTONS_THICKNESS)
        cv2.addWeighted(screen1, transparency, screen, 1 - transparency, 0, screen)
        cv2.putText(screen, constants.BUTTON_DELETE_CELL_TEXT, (self.main_coordinates[1] + int(1/20*(constants.WIDTH_CAMERA - self.main_coordinates[1])) + int(2/20*(constants.WIDTH_CAMERA - self.main_coordinates[1])), self.main_coordinates[2] + int(45/56*(self.main_coordinates[3] - self.main_coordinates[2]))), cv2.FONT_HERSHEY_SIMPLEX, constants.BUTTONS_FONTSCALE, color_text, constants.BUTTONS_TEXT_THICKNESS, cv2.LINE_AA)

    def draw_buttons_sudoku(self, screen : np.ndarray) -> None:
        '''Draw the buttons of the sudoku interface'''
        # draw the button "Validate grid"
        self.draw_button_validate_grid(screen)

        # draw the button "Draw a digit"
        self.draw_button_draw_digit(screen)

        # draw the button "Delete a digit"
        self.draw_button_delete_cell(screen)

    def draw_buttons_numbers(self, screen : np.ndarray) -> None:
        '''Draw the buttons of the numbers interface'''
        pass

    def display_digits_grid(self, screen : np.ndarray) -> None:
        '''Display the digits of the grid'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                self.cells[i][j].display_cell(screen)

    def find_clicked_cell(self, coordinates_click : tuple[int]) -> ic.Cell:
        '''Find the cell that has been clicked'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                if self.cells[i][j].is_clicked(coordinates_click):
                    self.cells[i][j].is_active = True
                    return self.cells[i][j]
                else :
                    continue
        return None
    
    def activate_buttons(self, coordinates_click : tuple[int]) -> None:
        '''Activate the button "Validate grid" if it is clicked'''
        pass

    def activate_validate_grid(self, coordinates_click : tuple[int]) -> None:
        pass

    def activate_draw_digit(self, coordinates_click : tuple[int]) -> None:
        pass

    def activate_delete_cell(self, coordinates_click : tuple[int]) -> None:
        pass

    def ask_digit(self, cell:ic.Cell) -> None:
        '''Ask the user to put a digit in the grid via the terminal'''
        if cell is not None:
            cell.value = int(input("Enter a digit for the cell ({}, {}) : ".format(cell.position_in_grid[0], cell.position_in_grid[1])))
            print("You have entered the digit {} for the cell ({}, {})".format(cell.value, cell.position_in_grid[0], cell.position_in_grid[1]))
            cell.is_active = False



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
            cv2.putText(screen, "Sudoku Completed !", (constants.WIDTH_CAMERA//10, constants.HEIGHT_CAMERA//2), cv2.FONT_HERSHEY_DUPLEX, constants.COMPLETION_FONTSCALE, constants.COMPLETION_COLOR, constants.COMPLETION_THICKNESS, cv2.LINE_AA)