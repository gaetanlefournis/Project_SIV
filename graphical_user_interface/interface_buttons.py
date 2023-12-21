from typing import Callable

import numpy as np
import cv2

class Button():
    '''This class represents a button in the graphical user interface.
    
    Attributes :
        coordinates : list[int]
        color : tuple[int]
        thickness : int
        text : str
        text_font_scale : int
        text_thickness : int
        text_color_active : tuple[int]
        text_color_inactive : tuple[int]
        transparency_active : int
        transparency_inactive : int
        is_active : bool
        
    Methods :
        draw : draw the button in the screen
        update_button_status : update the status of the button
        is_clicked : check if the button is clicked
    '''

    def __init__(self, coordinates: list[int], color: tuple[int], thickness: int, text: str, text_font_scale: int, text_thickness: int, font_color_active: tuple[int], font_color_inactive: tuple[int], transparency_active: int, transparency_inactive: int):
        self.coordinates = coordinates
        self.color = color
        self.thickness = thickness
        self.text = text
        self.text_font_scale = text_font_scale
        self.text_thickness = text_thickness
        self.text_color_active = font_color_active
        self.text_color_inactive = font_color_inactive
        self.transparency_active = transparency_active
        self.transparency_inactive = transparency_inactive
        self.is_active = False

    def draw(self, screen:np.ndarray) -> None:
        '''Draw the button in the screen'''
        screen1 = screen.copy()
        if self.is_active:
            color_text = self.text_color_active
            transparency = self.transparency_active
        else:
            color_text = self.text_color_inactive
            transparency = self.transparency_inactive
        cv2.rectangle(screen1,(self.coordinates[0], self.coordinates[2]), (self.coordinates[1], self.coordinates[3]), self.color, self.thickness)
        cv2.addWeighted(screen1, transparency, screen, 1 - transparency, 0, screen)
        cv2.putText(screen, self.text, (self.coordinates[0] + int(1/20*(self.coordinates[1] - self.coordinates[0])), self.coordinates[2] + int(13/20*(self.coordinates[3] - self.coordinates[2]))), cv2.FONT_HERSHEY_SIMPLEX, self.text_font_scale, color_text, self.text_thickness, cv2.LINE_AA)

    def update_button_status(self, activation_button: Callable) -> None:
        '''Update the status of the button'''
        if activation_button():
            self.is_active = True
        else:
            self.is_active = False

    def is_clicked(self, coordinates_click: tuple[int]) -> bool:
        '''Check if the button is clicked'''
        if self.is_active:
            if coordinates_click[0] >= self.coordinates[0] and coordinates_click[0] < self.coordinates[1] and coordinates_click[1] >= self.coordinates[2] and coordinates_click[1] < self.coordinates[3]:
                return True
        return False