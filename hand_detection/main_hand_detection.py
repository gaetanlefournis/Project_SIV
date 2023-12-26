import time

import cv2
import numpy as np

from hand_detection import hand_detector as htm
from hand_detection import hand_display as hdi
from hand_detection import hand_properties as hp 
from utils import utils
from hand_detection import constants


def main_hand_detection(img : np.ndarray, detector : htm.HandDetector, display : hdi.Display) -> np.ndarray:

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

    

if __name__ == '__main__':
    # Use the built-in webcam to capture video
    time.sleep(2) # wait for the camera to warm up
    cap = cv2.VideoCapture(0)

    # create a hand detector object and a hand display object
    detector = htm.HandDetector()
    display = hdi.Display()

    # initialize the time that will serve to calculate the frame rate
    pTime = 0 

    while True:

        # We read the image from the webcam
        _, img = cap.read()

        # We convert the image to RGB 
        img = utils.convert_to_RGB(img)

        # We set the image attribute of the detector object
        detector.img = img

        # We process the image in order to detect hands in it
        detector.process_image()

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
            if detector.click(hand):
                print("clicking")
                print(hand.barycenter)
            else:
                print("not clicking")

        # Calculate the frame rate
        fps, pTime = utils.calculate_frame_rate(pTime)

        # convert the image back to BGR
        detector.img = utils.convert_to_BGR(detector.img)

        # display the frame rate
        display.draw_frame_rate(detector.img, fps)

        # display the resulting frame
        cv2.imshow("Image", detector.img)

        # if 'q' is pressed, quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
