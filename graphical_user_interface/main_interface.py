import time

import cv2
import numpy as np

from graphical_user_interface import constants
from graphical_user_interface import interface_grid as ig
from graphical_user_interface import interface_digit as id



def main_interface(img:np.ndarray, grid:ig, coordinates_click: tuple[int], coordinates_hand: tuple[int]) -> np.ndarray:
    '''This function is the main function of the graphical user interface.
    
    Args:
        img (np.ndarray): image
        grid (ig.Grid): grid of the sudoku
        coordinates_click (tuple[int]): coordinates of the click
        coordinates_hand (tuple[int]): coordinates of the hand
        
    Returns:
        img (np.ndarray): image
    '''
    if grid.interface_digit.is_active:
        # We draw the main digit interface
        grid.interface_digit.draw_main(img)

        if coordinates_click is not None:
            grid.interface_digit.click_on_grid(coordinates_click)

            constants.digit = grid.interface_digit.click_on_buttons(coordinates_click)

        else:
            grid.interface_digit.draw_digit(img, coordinates_hand)  

        grid.interface_digit.update_buttons_status()      

    else:
        # We draw the grid
        grid.draw_grid(img)

        if constants.digit is not None:
            if grid.active_cell is not None:
                grid.active_cell.value = constants.digit
                grid.active_cell.is_active = False
                grid.active_cell = None

        grid.display_digits_grid(img)

        # We check where the click is (if there was one)
        if coordinates_click is not None:
            grid.find_clicked_cell(coordinates_click)

            grid.update_buttons_status()  
            # We ask the user to put a digit in the grid via the terminal
            # grid.ask_digit() 

            grid.click_on_buttons(coordinates_click)

            grid.update_buttons_status() 

        grid.update_buttons_status()  
        constants.digit = None

    return img
    

if __name__ == '__main__':
    # Use the built-in webcam to capture video
    # wait for 1 second before the webcam starts
    time.sleep(1)
    cap = cv2.VideoCapture(0)

    # Set the webcam resolution (we have to put it bigger to display the sudoku)
    cap.set(3, constants.WIDTH_CAMERA)
    cap.set(4, constants.HEIGHT_CAMERA)

    while True:
        # Read the image from the webcam
        _, img = cap.read()

        # Resize the image in function of the webcam resolution
        img = cv2.resize(img, (constants.WIDTH_CAMERA, constants.HEIGHT_CAMERA))

        # We convert the image to RGB 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # We create the grid
        if constants.MAIN_GRID_SIZE == 4:
            grid = ig.Grid(constants.MAIN_GRID_COORDINATES, constants.LIST_DIGITS_INITIAL_4)
        elif constants.MAIN_GRID_SIZE == 9:
            grid = ig.Grid(constants.MAIN_GRID_COORDINATES, constants.LIST_DIGITS_INITIAL_9)

        # We draw the grid and the digits inside
        grid.draw_grid(img)
        grid.display_digits_grid(img)

        # We convert the image back to BGR
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # We display the resulting frame
        cv2.imshow("Image", img)

        # if 'q' is pressed, quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # We check if the sudoku is completed
        grid.display_completion(img)

    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
