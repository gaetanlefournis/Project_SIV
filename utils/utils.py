import time

import numpy as np
import cv2

def calculate_frame_rate(pTime: float) -> float:
    """Calculate the frame rate of the video.

    Args:
        pTime (float): time before calculation

    Returns:
        fps (float): frame rate
        pTime (float): the current time that will be used as the previous time in the next iteration
    """
    cTime = time.time() # current time
    fps = 1 / (cTime - pTime) # frames per second
    pTime = cTime # update the previous time
    return fps, pTime

def convert_to_RGB(img: np.ndarray) -> np.ndarray:
    """Convert an image to RGB and into a numpy array."""
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def convert_to_BGR(img: np.ndarray) -> np.ndarray:
    """Convert an image to BGR and into a numpy array."""
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img
    