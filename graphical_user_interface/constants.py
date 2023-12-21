import numpy as np

###################################
#  GENERAL PARAMETERS OF THE GUI  #
###################################

WIDTH_CAMERA = 1280
HEIGHT_CAMERA = 720

# INITIAL DIGITS
################
LIST_DIGITS_INITIAL_4 = [[0, 0, 0, 3],
                        [0, 4, 0, 0],
                        [0, 0, 3, 2],
                        [0, 0, 0, 0]]
LIST_DIGITS_INITIAL_9 = [[1, 0, 0, 0, 0, 0, 0, 0, 6],
                       [0, 0, 6, 0, 2, 0, 7, 0, 0],
                       [7, 8, 9, 4, 5, 0, 1, 0, 3],
                       [0, 0, 0, 8, 0, 7, 0, 0, 4],
                       [0, 0, 0, 0, 3, 0, 0, 0, 0],
                       [0, 9, 0, 0, 0, 4, 2, 0, 1],
                       [3, 1, 2, 9, 7, 0, 0, 4, 0],
                       [0, 4, 0, 0, 1, 2, 0, 7, 8],
                       [9, 0, 8, 0, 0, 0, 0, 0, 0]]

# GRID INTERFACE
################

# MAIN_GRID
MAIN_GRID_SIZE = 4
MAIN_GRID_COLOR = (0, 0, 0)
MAIN_GRID_THICKNESS = 10

# MAIN LINES
MAIN_LINES_COLOR = (0, 0, 0)
MAIN_LINES_THICKNESS = 4

# OTHER LINES
OTHER_LINES_COLOR = (0, 0, 0)
OTHER_LINES_THICKNESS = 1

# CELLS
CELLS_COLOR = (255, 255, 255)
CELLS_COLOR_ACTIVE = (255, 0, 0)
CELLS_THICKNESS = -1
CELL_TRANSPARENCY = 0.3

# DIGITS
INITIAL_DIGITS_COLOR = (0, 0, 0)
OTHER_DIGITS_COLOR = (0, 0, 255)
DIGITS_THICKNESS = 2
DIGITS_FONTSCALE = 4 - np.sqrt(MAIN_GRID_SIZE) if np.sqrt(MAIN_GRID_SIZE) < 3 else 1

# DISPLAY COMPLETION
COMPLETION_COLOR = (0, 255, 0)
COMPLETION_FONTSCALE = 3
COMPLETION_THICKNESS = 3

# COORDINATES
#############

# MAIN GRID
MAIN_GRID_COORDINATES = [WIDTH_CAMERA//2 - HEIGHT_CAMERA//2, WIDTH_CAMERA//2 + HEIGHT_CAMERA//2, HEIGHT_CAMERA//20, 19*HEIGHT_CAMERA//20]

# BUTTON VALIDATE GRID
BUTTON_VALIDATE_GRID_COORDINATES = [int(1/20*(WIDTH_CAMERA - MAIN_GRID_COORDINATES[1])) + MAIN_GRID_COORDINATES[1], int(19/20*(WIDTH_CAMERA - MAIN_GRID_COORDINATES[1])) + MAIN_GRID_COORDINATES[1], MAIN_GRID_COORDINATES[2] + int(1/7*(MAIN_GRID_COORDINATES[3] - MAIN_GRID_COORDINATES[2])), MAIN_GRID_COORDINATES[2] + int(2/7*(MAIN_GRID_COORDINATES[3] - MAIN_GRID_COORDINATES[2]))]

# BUTTON DRAW DIGIT
BUTTON_DRAW_DIGIT_COORDINATES = [int(1/20*(WIDTH_CAMERA - MAIN_GRID_COORDINATES[1])) + MAIN_GRID_COORDINATES[1], int(19/20*(WIDTH_CAMERA - MAIN_GRID_COORDINATES[1])) + MAIN_GRID_COORDINATES[1], MAIN_GRID_COORDINATES[2] + int(3/7*(MAIN_GRID_COORDINATES[3] - MAIN_GRID_COORDINATES[2])), MAIN_GRID_COORDINATES[2] + int(4/7*(MAIN_GRID_COORDINATES[3] - MAIN_GRID_COORDINATES[2]))]

# BUTTON DELETE CELL
BUTTON_DELETE_CELL_COORDINATES = [int(1/20*(WIDTH_CAMERA - MAIN_GRID_COORDINATES[1])) + MAIN_GRID_COORDINATES[1], int(19/20*(WIDTH_CAMERA - MAIN_GRID_COORDINATES[1])) + MAIN_GRID_COORDINATES[1], MAIN_GRID_COORDINATES[2] + int(5/7*(MAIN_GRID_COORDINATES[3] - MAIN_GRID_COORDINATES[2])), MAIN_GRID_COORDINATES[2] + int(6/7*(MAIN_GRID_COORDINATES[3] - MAIN_GRID_COORDINATES[2]))]

# BUTTONS
#########

# GENERAL (for all buttons)
BUTTONS_THICKNESS = -1
BUTTONS_FONTSCALE = 1
BUTTONS_TEXT_THICKNESS = 2
BUTTONS_TRANSPARENCY_ACTIVE = 0.5
BUTTONS_TRANSPARENCY_INACTIVE = 0.2

# VALIDATE THE ENTIRE GRID
BUTTON_VALIDATE_GRID_COLOR = (0, 255, 0)
BUTTON_VALIDATE_GRID_TEXT_COLOR_ACTIVE = (0, 0, 0)
BUTTON_VALIDATE_GRID_TEXT_COLOR_INACTIVE = (255, 255, 255)
BUTTON_VALIDATE_GRID_TEXT = "Validate Grid"

# DRAW A DIGIT
BUTTON_DRAW_DIGIT_COLOR = (0, 255, 0)
BUTTON_DRAW_DIGIT_TEXT_COLOR_ACTIVE = (0, 0, 0)
BUTTON_DRAW_DIGIT_TEXT_COLOR_INACTIVE = (255, 255, 255)
BUTTON_DRAW_DIGIT_TEXT = "Draw Digit"

# DELETE A DIGIT
BUTTON_DELETE_CELL_COLOR = (0, 255, 0)
BUTTON_DELETE_CELL_TEXT_COLOR_ACTIVE = (0, 0, 0)
BUTTON_DELETE_CELL_TEXT_COLOR_INACTIVE = (255, 255, 255)
BUTTON_DELETE_CELL_TEXT = "Delete Digit"

# VALIDATE A DIGIT
BUTTON_VALIDATE_DIGIT_COLOR = (0, 255, 0)
BUTTON_VALIDATE_DIGIT_TEXT_COLOR_ACTIVE = (0, 0, 0)
BUTTON_VALIDATE_DIGIT_TEXT_COLOR_INACTIVE = (255, 255, 255)
BUTTON_VALIDATE_DIGIT_TEXT = "validate digit"

# ERASE A DIGIT
BUTTON_ERASE_DIGIT_COLOR = (0, 255, 0)
BUTTON_ERASE_DIGIT_TEXT_COLOR_ACTIVE = (0, 0, 0)
BUTTON_ERASE_DIGIT_TEXT_COLOR_INACTIVE = (255, 255, 255)
BUTTON_ERASE_DIGIT_TEXT = "erase digit"







