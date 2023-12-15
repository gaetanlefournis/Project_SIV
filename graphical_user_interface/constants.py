import numpy as np

###################################
#  GENERAL PARAMETERS OF THE GUI  #
###################################

WIDTH_CAMERA = 1280
HEIGHT_CAMERA = 720

# INITIAL DIGITS
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

# MAIN_GRID
MAIN_GRID_SIZE = 4
MAIN_GRID_COLOR = (0, 0, 0)
MAIN_GRID_THICKNESS = 10
MAIN_GRID_COORDINATES = [WIDTH_CAMERA//2 - HEIGHT_CAMERA//2, WIDTH_CAMERA//2 + HEIGHT_CAMERA//2, HEIGHT_CAMERA//20, 19*HEIGHT_CAMERA//20]

# MAIN LINES
MAIN_LINES_COLOR = (0, 0, 0)
MAIN_LINES_THICKNESS = 4

# OTHER LINES
OTHER_LINES_COLOR = (0, 0, 0)
OTHER_LINES_THICKNESS = 1

# CELLS
CELLS_COLOR = (255, 255, 255)
CELLS_THICKNESS = -1
CELL_TRANSPARENCY = 0.3

# DIGITS
INITIAL_DIGITS_COLOR = (0, 0, 0)
OTHER_DIGITS_COLOR = (255, 0, 0)
DIGITS_THICKNESS = 2
DIGITS_FONTSCALE = 4 - np.sqrt(MAIN_GRID_SIZE) if np.sqrt(MAIN_GRID_SIZE) < 3 else 1

# DISPLAY COMPLETION
COMPLETION_COLOR = (0, 255, 0)
COMPLETION_FONTSCALE = 4
COMPLETION_THICKNESS = 2




