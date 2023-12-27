import numpy as np

from graphical_user_interface import interface_grid as ig
from graphical_user_interface import global_variable as gv


def main_interface(img:np.ndarray, grid:ig, coordinates_click: tuple[int], coordinates_hand: tuple[int]) -> np.ndarray:
    '''This function is the main function of the graphical user interface.
    
    Parameters :
        img (np.ndarray) : image on which we draw the interface
        grid (InterfaceGrid) : interface of the grid
        coordinates_click (tuple[int]) : coordinates of the click
        coordinates_hand (tuple[int]) : coordinates of the hand

    Returns :
        img (np.ndarray) : image on which we draw the interface
    '''
    if grid.interface_digit.is_active:
        # We draw the main digit interface
        grid.interface_digit.draw_main(img)

        if coordinates_click is not None:
            grid.interface_digit.click_on_grid(coordinates_click)

            gv.digit = grid.interface_digit.click_on_buttons(coordinates_click)

        else:
            grid.interface_digit.draw_digit(img, coordinates_hand)  

        grid.interface_digit.update_buttons_status()      

    else:
        # We draw the grid
        grid.draw_grid(img)

        if gv.digit is not None:
            if grid.active_cell is not None:
                grid.active_cell.value = gv.digit
                grid.active_cell.is_active = False
                grid.active_cell = None

        if grid.completed:
            grid.display_completion(img)


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
        gv.digit = None

    return img

