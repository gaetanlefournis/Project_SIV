import time

import numpy as np
import cv2

def calculate_frame_rate(pTime: float) -> float:
    """Calculate the frame rate of the video."""
    cTime = time.time() 
    fps = 1 / (cTime - pTime) 
    pTime = cTime 
    return fps, pTime

def convert_to_RGB(img: np.ndarray) -> np.ndarray:
    """Convert an image to RGB"""
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def convert_to_BGR(img: np.ndarray) -> np.ndarray:
    """Convert an image to BGR"""
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img
    