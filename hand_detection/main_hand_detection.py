import numpy as np

from hand_detection import hand_detector as htm
from hand_detection import hand_display as hdi
from hand_detection import hand_properties as hp 
from hand_detection import constants


def main_hand_detection(img : np.ndarray, detector : htm.HandDetector, display : hdi.Display) -> [np.ndarray, tuple[int], tuple[int]]:
    '''This function is the main function of the hand detection.

    Parameters :
        img (np.ndarray) : image in which we detect hands
        detector (HandDetector) : object used to detect hands
        display (Display) : object used to display the results

    Returns :
        img (np.ndarray) : image in which we detect hands
        coordinates_click (tuple[int]) : coordinates of the click
        coordinates_hand (tuple[int]) : coordinates of the hand
    '''

    # We set the image attribute of the detector object
    detector.img = img

    # We process the image in order to detect hands in it
    detector.process_image()

    # We initialize the coordinates of the click
    coordinates_click = None
    coordinates_hand = None

    # If there are hands detected, we get the one designed by HAND_NUMBER
    if detector.results.multi_hand_landmarks:
        hand_lm = detector.results.multi_hand_landmarks[constants.HAND_NUMBER]

        # We create an Hand object
        hand = hp.Hand(hand_lm.landmark)

        # We calculate the real position of each landmark, and put it in the form of a list: [[id, x, y], ...]
        hand.find_position(detector.img)

        # We calculate the barycenter of the hand
        hand.calculate_barycenter()

        # We calculate the state of each finger except thumb, and put it in the form of a list: [index, middle, ring, pinky]
        hand.fingers_up()

        # We draw the landmarks that we want
        display.draw_landmarks(detector.img, hand.lmList)

        # We draw the barycenter
        display.draw_barycenter(detector.img, hand.barycenter)

        # We check if we are clicking
        detector.fingers_bent(hand)
        if detector.click():
            print("clicking")
            coordinates_click = hand.barycenter
        else:
            print("not clicking")
        
        # We keep the coordinates of the hand if there is one.
        coordinates_hand = hand.barycenter

    return img, coordinates_click, coordinates_hand
