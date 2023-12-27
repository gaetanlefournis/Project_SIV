import numpy as np
import cv2

from graphical_user_interface import constants
from graphical_user_interface import interface_cell as ic
from graphical_user_interface import interface_buttons as ib
from graphical_user_interface import interface_digit as id

class Grid():
    '''This class represents the grid of the sudoku. It is composed of cells.
    The grid is represented by a numpy array of cells.
    The grid is completed when all the cells have a value.
    
    Attributes : 
        main_coordinates (list[int]) : coordinates of the main grid
        list_cells_origin (list[list[int]]) : list of the cells of the grid
        cells (np.ndarray) : cells of the grid
        buttons (np.ndarray) : buttons of the sudoku interface
        interface_digit (id.InterfaceDigit) : interface to write the digit
        completed (bool) : True if the grid is completed, False otherwise
        active_cell (ic.Cell) : cell that is active

    Methods :
        create_cells : create the objects "cell" of the grid
        create_buttons : create the buttons of the sudoku interface
        create_interface_digit : create the interface to write the digit
        draw_grid : draw the grid on the screen and the empty cells
        draw_lines : draw the main lines of the grid
        draw_cells : draw the cells of the grid
        draw_buttons : draw the buttons of the sudoku interface
        display_digits_grid : display the digits of the grid
        find_clicked_cell : find the cell that has been clicked
        update_buttons_status : update the status of the buttons
        activate_validate_grid : activate the button "Validate grid" if the grid is completed
        activate_draw_digit : activate the button "Draw digit" if a cell is active and if it has not been drawn
        activate_delete_cell : activate the button "Delete cell" if there a cell is drawn and if it's not an initial cell
        click_on_buttons : check if the user has clicked on a button, and execute the action associated
        display_completion : display the message "Sudoku Completed" if the grid is completed
        is_validate : check if the sudoku grid is correct
        is_list_correct : check if a list of values is correct, which means not twice the same number and a max value of size_grid
    '''

    def __init__(self, main_coordinates:list[int], list_cells_origin :list[list[int]]):
        self.main_coordinates = main_coordinates
        self.list_cells_origin = list_cells_origin
        self.cells = np.ndarray((constants.MAIN_GRID_SIZE, constants.MAIN_GRID_SIZE), dtype=ic.Cell)
        self.buttons = np.ndarray(3, dtype=ib.Button)
        self.interface_digit = None
        self.completed = False
        self.active_cell = None
        self.create_cells()
        self.create_buttons()
        self.create_interface_digit()

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

    def create_buttons(self) -> None:
        '''Create the buttons of the sudoku interface'''
        # Create the button "Validate grid"
        self.buttons[0] = ib.Button(constants.BUTTON_VALIDATE_GRID_COORDINATES, constants.BUTTON_VALIDATE_GRID_COLOR, constants.BUTTONS_THICKNESS, constants.BUTTON_VALIDATE_GRID_TEXT, constants.BUTTONS_FONTSCALE, constants.BUTTONS_TEXT_THICKNESS, constants.BUTTON_VALIDATE_GRID_TEXT_COLOR_ACTIVE, constants.BUTTON_VALIDATE_GRID_TEXT_COLOR_INACTIVE, constants.BUTTONS_TRANSPARENCY_ACTIVE, constants.BUTTONS_TRANSPARENCY_INACTIVE)

        # Create the button "Draw digit"
        self.buttons[1] = ib.Button(constants.BUTTON_DRAW_DIGIT_COORDINATES, constants.BUTTON_DRAW_DIGIT_COLOR, constants.BUTTONS_THICKNESS, constants.BUTTON_DRAW_DIGIT_TEXT, constants.BUTTONS_FONTSCALE, constants.BUTTONS_TEXT_THICKNESS, constants.BUTTON_DRAW_DIGIT_TEXT_COLOR_ACTIVE, constants.BUTTON_DRAW_DIGIT_TEXT_COLOR_INACTIVE, constants.BUTTONS_TRANSPARENCY_ACTIVE, constants.BUTTONS_TRANSPARENCY_INACTIVE)

        # Create the button "Delete cell"
        self.buttons[2] = ib.Button(constants.BUTTON_DELETE_CELL_COORDINATES, constants.BUTTON_DELETE_CELL_COLOR, constants.BUTTONS_THICKNESS, constants.BUTTON_DELETE_CELL_TEXT, constants.BUTTONS_FONTSCALE, constants.BUTTONS_TEXT_THICKNESS, constants.BUTTON_DELETE_CELL_TEXT_COLOR_ACTIVE, constants.BUTTON_DELETE_CELL_TEXT_COLOR_INACTIVE, constants.BUTTONS_TRANSPARENCY_ACTIVE, constants.BUTTONS_TRANSPARENCY_INACTIVE)

    def create_interface_digit(self):
        '''Create the interface to write the digit'''
        self.interface_digit = id.InterfaceDigit(constants.MAIN_GRID_COORDINATES)
    
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
        self.draw_buttons(screen)

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

    def draw_buttons(self, screen : np.ndarray) -> None:
        '''Draw the buttons of the sudoku interface'''
        for i in range(len(self.buttons)):
            self.buttons[i].draw(screen)

    def display_digits_grid(self, screen : np.ndarray) -> None:
        '''Display the digits of the grid'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                self.cells[i][j].display_cell(screen)

    def find_clicked_cell(self, coordinates_click: tuple[int]) -> None:
        '''Find the cell that has been clicked'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                if self.cells[i][j].is_clicked(coordinates_click):
                    if not self.active_cell is None:
                        self.active_cell.is_active = False
                    self.cells[i][j].is_active = True
                    self.active_cell = self.cells[i][j]
                    break
        
    def update_buttons_status(self) -> None:
        '''Return the status of the buttons'''
        self.buttons[0].update_button_status(self.activate_validate_grid)
        self.buttons[1].update_button_status(self.activate_draw_digit)
        self.buttons[2].update_button_status(self.activate_delete_cell)

    def activate_validate_grid(self) -> bool:
        '''Activate the button "Validate grid" if the grid is completed'''
        for i in range(constants.MAIN_GRID_SIZE):
            for j in range(constants.MAIN_GRID_SIZE):
                if not self.cells[i][j].is_drawn:
                    self.completed = False
                    return False
        return True

    def activate_draw_digit(self) -> bool:
        '''Activate the button "Draw digit" if a cell is active and if it has not been drawn'''
        if self.active_cell is not None and self.active_cell.is_active and not self.active_cell.is_drawn:
            return True
        return False

    def activate_delete_cell(self) -> bool:
        '''Activate the button "Delete cell" if there a cell is drawn and if it's not an initial cell'''
        if self.active_cell is not None and self.active_cell.is_drawn and not self.active_cell.initial:
            return True
        return False
    
    def click_on_buttons(self, coordinates_click : tuple[int]) -> None:
        '''Check if the user has clicked on a button, and execute the action associated'''
        for i in range(len(self.buttons)):
            if self.buttons[i].is_active and self.buttons[i].is_clicked(coordinates_click):
                if i == 0:
                    self.completed = True
                    if self.active_cell is not None:
                        self.active_cell.is_active = False
                        self.active_cell = None
                elif i == 1:
                    self.interface_digit.initialize_interface()
                elif i == 2:
                    self.active_cell.erase_cell()
                    self.active_cell.is_active = False
                    self.active_cell = None
    
    def display_completion(self, screen : np.ndarray) -> None:
        '''Display the message "Sudoku Completed" if the grid is completed'''
        if self.is_validate():
            cv2.putText(screen, "Sudoku Completed !", (constants.WIDTH_CAMERA//10, constants.HEIGHT_CAMERA//2), cv2.FONT_HERSHEY_DUPLEX, constants.COMPLETION_FONTSCALE, constants.COMPLETION_COLOR_TRUE, constants.COMPLETION_THICKNESS, cv2.LINE_AA)
        else:
            cv2.putText(screen, "Sudoku Wrong !", (constants.WIDTH_CAMERA//10, constants.HEIGHT_CAMERA//2), cv2.FONT_HERSHEY_DUPLEX, constants.COMPLETION_FONTSCALE, constants.COMPLETION_COLOR_FALSE, constants.COMPLETION_THICKNESS, cv2.LINE_AA)

    def is_validate(self) -> bool:
        '''Check if the sudoku grid is correct'''
        # Check the lines
        for i in range(constants.MAIN_GRID_SIZE):
            list_values = []
            for j in range(constants.MAIN_GRID_SIZE):
                if self.cells[i][j].is_drawn:
                    list_values.append(self.cells[i][j].value)
            if not self.is_list_correct(list_values, constants.MAIN_GRID_SIZE):
                return False
            
        # Check the columns
        for j in range(constants.MAIN_GRID_SIZE):
            list_values = []
            for i in range(constants.MAIN_GRID_SIZE):
                if self.cells[i][j].is_drawn:
                    list_values.append(self.cells[i][j].value)
            if not self.is_list_correct(list_values, constants.MAIN_GRID_SIZE):
                return False
            
        # Check the squares
        sqrt_sudoku_size = int(np.sqrt(constants.MAIN_GRID_SIZE))
        for i in range(sqrt_sudoku_size):
            for j in range(sqrt_sudoku_size):
                list_values = []
                for k in range(sqrt_sudoku_size):
                    for l in range(sqrt_sudoku_size):
                        if self.cells[i*sqrt_sudoku_size + k][j*sqrt_sudoku_size + l].is_drawn:
                            list_values.append(self.cells[i*sqrt_sudoku_size + k][j*sqrt_sudoku_size + l].value)
                if not self.is_list_correct(list_values, constants.MAIN_GRID_SIZE):
                    return False
        
        return True
    
    def is_list_correct(self, list_values : list[int], size_grid:int) -> bool:
        '''Check if a list of values is correct, which means not twice the same number and a max value of size_grid'''
        if len(list_values) != len(set(list_values)):
            return False
        for i in range(len(list_values)):
            if list_values[i] > size_grid or list_values[i] < 1:
                return False
        return True