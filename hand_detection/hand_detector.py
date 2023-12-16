import mediapipe as mp
import numpy as np

from hand_detection import hand_properties as hp

class HandDetector():
    '''This class is used to detect hands in an image/video and perform actions.
    
    Attributes:
        img: image
        mpHands: mediapipe hands object
        hands: mediapipe hands object
        results: results of the mediapipe hands object after processing
        
    Methods:
        process_image: process an image in order to detect hands in it
        click: returns True if at least three of the fingers are bent
    '''

    def __init__(self):
        self.img = None
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.results = None

    def process_image(self) -> np.ndarray:
        '''This function processes an image in order to detect hands in it.'''
        self.results = self.hands.process(self.img)

    def click(self, hand: hp.Hand) -> bool: 
        '''This function returns True if at least three of the fingers are bent.
        That position means that we are clicking at the position of the barycenter of the hand.
        
        Args:
            hand (Hand): hand
            
        Returns:
            True if at least three of the fingers are bent, False otherwise
        '''
        if hand.fingers.sum() >= 2:
            return False
        else:
            return True
