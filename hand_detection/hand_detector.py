import mediapipe as mp
import numpy as np

from hand_detection import hand_properties as hp

class HandDetector():
    '''This class is used to detect hands in an image/video and perform actions.
    
    Attributes:
        img (np.ndarray): image in which we detect hands
        mpHands (mediapipe.solutions.hands): object used to detect hands
        hands (mediapipe.solutions.hands.Hands): object used to detect hands
        results (mediapipe.framework.formats.landmark.LandmarkList): results of the hand detection
        list_actions (np.ndarray): list of the actions performed by the hand

    Methods:
        process_image: process an image in order to detect hands in it
        fingers_bent: return True if at least three of the fingers are bent
        click: return True if the hand is in a click position
    '''

    def __init__(self):
        self.img = None
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.results = None
        self.list_actions = np.asarray([False, False, False, False, False])

    def process_image(self) -> None:
        '''This function processes an image in order to detect hands in it.'''
        self.results = self.hands.process(self.img)

    def fingers_bent(self, hand:hp.Hand) -> None:
        '''This function returns True if at least three of the fingers are bent.'''
        self.list_actions = np.roll(self.list_actions, -1)
        if hand.fingers.sum() >= 2:
            self.list_actions[4] = False
        else:
            self.list_actions[4] = True

    def click(self) -> bool: 
        if not self.list_actions[0] and not self.list_actions[1] and not self.list_actions[2] and not self.list_actions[3] and self.list_actions[4]:
            return True
        else:
            return False
