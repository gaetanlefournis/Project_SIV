import numpy as np
import cv2

from graphical_user_interface import constants
from graphical_user_interface import interface_buttons as ib
from digit_recognition import main_digit_recognition as mdr


class InterfaceDigit():
    '''This class represents the interface of a digit in the graphical user interface.

    Attributes :
        main_coordinates (tuple[int]) : coordinates of the main interface
        buttons (np.ndarray) : buttons of the interface
        pixels (list[list[int]]) : pixels of the digit
        final_image_digit (np.ndarray) : final image of the digit
        digit (int) : digit drawn
        is_active (bool) : True if the interface is active, False otherwise
        is_drawing (bool) : True if the digit is being drawn, False otherwise
        is_drawn (bool) : True if the digit is drawn, False otherwise

    Methods :
        create_buttons : create the buttons of the interface
        initialize_final_image_digit : create the final image of the digit
        initialize_interface : initialize the interface
        draw_main : draw the interface and the buttons
        draw_interface : draw the interface
        draw_buttons : draw the buttons
        click_on_grid : check if the click is on the grid. We don't return anything, but we know if we are drawing or if the draw is over
        update_buttons_status : update the status of the buttons
        activate_validate_digit : activate the button "validate digit" if the digit is drawn
        activate_erase_digit : activate the button "erase digit" if the list of pixels is not empty
        click_on_buttons : return the digit if the button "validate digit" is clicked, None otherwise
        draw_digit : draw the digit
        keep_pixels : memorize the pixels of the digit in order to plot them afterwards
        modify_final_image : modify the final image
        draw_digit_on_screen : draw the final image of the digit on the screen, with transparency
    '''

    def __init__(self, main_coordinates : tuple[int]):
        self.main_coordinates = main_coordinates
        self.buttons = np.ndarray(2, dtype=ib.Button)
        self.pixels = []
        self.final_image_digit = None
        self.digit = None
        self.is_active = False
        self.is_drawing = False
        self.is_drawn = False
        self.create_buttons()
        self.initialize_final_image_digit() 

    def create_buttons(self) -> None:
        '''Create the buttons of the interface'''
        # Button validate digit
        self.buttons[0] = ib.Button(constants.BUTTON_VALIDATE_DIGIT_COORDINATES, constants.BUTTON_VALIDATE_DIGIT_COLOR, constants.BUTTONS_THICKNESS, constants.BUTTON_VALIDATE_DIGIT_TEXT, constants.BUTTONS_FONTSCALE, constants.BUTTONS_TEXT_THICKNESS, constants.BUTTON_VALIDATE_DIGIT_TEXT_COLOR_ACTIVE, constants.BUTTON_VALIDATE_DIGIT_TEXT_COLOR_INACTIVE, constants.BUTTONS_TRANSPARENCY_ACTIVE, constants.BUTTONS_TRANSPARENCY_INACTIVE)

        # Button erase digit
        self.buttons[1] = ib.Button(constants.BUTTON_ERASE_DIGIT_COORDINATES, constants.BUTTON_ERASE_DIGIT_COLOR, constants.BUTTONS_THICKNESS, constants.BUTTON_ERASE_DIGIT_TEXT, constants.BUTTONS_FONTSCALE, constants.BUTTONS_TEXT_THICKNESS, constants.BUTTON_ERASE_DIGIT_TEXT_COLOR_ACTIVE, constants.BUTTON_ERASE_DIGIT_TEXT_COLOR_INACTIVE, constants.BUTTONS_TRANSPARENCY_ACTIVE, constants.BUTTONS_TRANSPARENCY_INACTIVE)

    def initialize_final_image_digit(self) -> None:
        '''Create the final image of the digit'''
        self.final_image_digit = np.zeros((self.main_coordinates[3] - self.main_coordinates[2], self.main_coordinates[1] - self.main_coordinates[0]), dtype=np.uint8)

    def initialize_interface(self) -> None:
        '''Initialize the interface'''
        self.pixels = []
        self.final_image_digit = np.zeros((self.main_coordinates[3] - self.main_coordinates[2], self.main_coordinates[1] - self.main_coordinates[0]), dtype=np.uint8)
        self.digit = None
        self.is_active = True
        self.is_drawing = False
        self.is_drawn = False

    def draw_main(self, screen : np.ndarray) -> None:
        '''Draw the interface and the buttons'''
        self.draw_interface(screen)
        self.draw_buttons(screen)

    def draw_interface(self, screen : np.ndarray) -> None:
        '''Draw the interface'''
        screen1 = screen.copy()
        cv2.rectangle(screen1,(self.main_coordinates[0], self.main_coordinates[2]), (self.main_coordinates[1], self.main_coordinates[3]), constants.MAIN_INTERFACE_DIGIT_COLOR, constants.MAIN_INTERFACE_DIGIT_THICKNESS)
        cv2.addWeighted(screen1, constants.MAIN_INTERFACE_DIGIT_TRANSPARENCY, screen, 1 - constants.MAIN_INTERFACE_DIGIT_TRANSPARENCY, 0, screen)

    def draw_buttons(self, screen : np.ndarray) -> None:
        '''Draw the buttons'''
        for i in range(len(self.buttons)):
            self.buttons[i].draw(screen)

    def click_on_grid(self, coordinates_click : tuple[int]) -> None:
        '''Check if the click is on the grid. We don't return anything, but we know if we are drawing or if the draw is over'''
        if self.main_coordinates[0] <= coordinates_click[0] < self.main_coordinates[1] and self.main_coordinates[2] <= coordinates_click[1] < self.main_coordinates[3] and not self.is_drawing:
            self.is_drawing = True
            self.is_drawn = False
        elif self.main_coordinates[0] <= coordinates_click[0] < self.main_coordinates[1] and self.main_coordinates[2] <= coordinates_click[1] < self.main_coordinates[3] and self.is_drawing and self.pixels != []:
            self.is_drawing = False
            self.is_drawn = True

    def update_buttons_status(self) -> None:
        '''Update the status of the buttons'''
        self.buttons[0].update_button_status(self.activate_validate_digit)
        self.buttons[1].update_button_status(self.activate_erase_digit)

    def activate_validate_digit(self) -> bool:
        '''Activate the button "validate digit" if the digit is drawn'''
        return self.is_drawn 
    
    def activate_erase_digit(self) -> bool:
        '''Activate the button "erase digit" if the list of pixels is not empty'''
        return self.pixels != []
    
    def click_on_buttons(self, coordinates_click : tuple[int]) -> int:
        '''Return the digit if the button "validate digit" is clicked, None otherwise'''
        for i in range(len(self.buttons)):
            if self.buttons[i].is_clicked(coordinates_click):
                if i == 0:
                    self.digit = mdr.main_digit_recognition(self.final_image_digit, "main")
                    print("The recognized digit is :", self.digit)
                    self.is_active = False
                    return self.digit
                elif i == 1:
                    self.pixels = []
                    self.is_drawn = False
                    self.is_drawing = False
                    self.initialize_final_image_digit()
        return None

    def draw_digit(self, img : np.ndarray, coordinates_hand : tuple[int]) -> None:
        '''Draw the digit'''
        if self.is_drawing:
            if coordinates_hand is not None:
                # We memorize the pixels of the digit
                self.keep_pixels(coordinates_hand)

                # We modify final image to color the pixels in black
                self.modify_final_image()

        if self.is_drawn or self.is_drawing:
            # We draw the digit
            self.draw_digit_on_screen(img)

    def keep_pixels(self, coordinates_hand : tuple[int]) -> None:
        '''Memorize the pixels of the digit in order to plot them afterwards'''
        for i in range(coordinates_hand[0] - constants.RADIUS_PIXELS, coordinates_hand[0] + constants.RADIUS_PIXELS + 1):
            for j in range(coordinates_hand[1] - constants.RADIUS_PIXELS, coordinates_hand[1] + constants.RADIUS_PIXELS + 1):
                if self.main_coordinates[0] <= i < self.main_coordinates[1] and self.main_coordinates[2] <= j < self.main_coordinates[3] and np.sqrt((i - coordinates_hand[0])**2 + (j - coordinates_hand[1])**2) <= constants.RADIUS_PIXELS:
                    self.pixels.append([i, j])

    def modify_final_image(self) -> None:
        '''Modify the final image'''
        for pixel in self.pixels:
            self.final_image_digit[pixel[1] - self.main_coordinates[2], pixel[0] - self.main_coordinates[0]] = 255

    def draw_digit_on_screen(self, img : np.ndarray) -> None:
        '''Draw the final image of the digit on the screen, with transparency'''
        for pixel in self.pixels:
            img[pixel[1], pixel[0]] = 0

        

    
        

    