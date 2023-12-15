import numpy as np
import constants


class Hand():
    '''This class is used to modelize a hand object, and all its properties.

    Attributes:
        landmarks: list of landmarks
        lmList: list of landmarks in the form of a list: [[id, x, y], ...]
        barycenter: barycenter of the hand
        fingers: state of each finger except thumb

    Methods:
        find_position: calculates the real position of each landmark, and put it in the form of a list: [[id, x, y], ...]
        calculate_barycenter: calculates the barycenter of the hand
        fingers_up: calculates the state of each finger except thumb, and put it in the form of a list: [index, middle, ring, pinky]
    '''

    def __init__(self, landmarks: list) -> None:
        self.landmarks = landmarks
        self.lmList = []
        self.barycenter = None
        self.fingers = np.ndarray(constants.NB_FINGERS_CLICK, dtype=bool)

    def find_position(self, img:np.ndarray) -> None:
        '''This function calculates the real position of each landmark, and put it in the form of a list: [[id, x, y], ...]'''
        h, w, _ = img.shape
        for id, lm in enumerate(self.landmarks):
            # real coordinates of the landmark
            x_pixel, y_pixel = int(lm.x * w), int(lm.y * h)
            self.lmList.append([id, x_pixel, y_pixel])
    
    def calculate_barycenter(self) -> tuple:
        '''This function calculates the barycenter of the hand, based on 5 special landmarks: 
            - thumb CMC
            - index finger MCP
            - middle finger MCP
            - ring finger MCP
            - pinky MCP.
        '''
        if self.lmList:
            x1 = self.lmList[constants.LANDMARKS["THUMB_CMC"]][1]
            y1 = self.lmList[constants.LANDMARKS["THUMB_CMC"]][2]
            x2 = self.lmList[constants.LANDMARKS["INDEX_FINGER_MCP"]][1]
            y2 = self.lmList[constants.LANDMARKS["INDEX_FINGER_MCP"]][2]
            x3 = self.lmList[constants.LANDMARKS["MIDDLE_FINGER_MCP"]][1]
            y3 = self.lmList[constants.LANDMARKS["MIDDLE_FINGER_MCP"]][2]
            x4 = self.lmList[constants.LANDMARKS["RING_FINGER_MCP"]][1]
            y4 = self.lmList[constants.LANDMARKS["RING_FINGER_MCP"]][2]
            x5 = self.lmList[constants.LANDMARKS["PINKY_MCP"]][1]
            y5 = self.lmList[constants.LANDMARKS["PINKY_MCP"]][2]
        self.barycenter = (int((x1 + x2 + x3 + x4 + x5) / constants.NB_FINGERS_BARYCENTER), int((y1 + y2 + y3 + y4 + y5) / constants.NB_FINGERS_BARYCENTER))
        return self.barycenter
    
    def fingers_up(self) -> np.ndarray[bool]:
        '''This function returns the state of each finger thanks to a list of booleans.
        it is based on the y coordinates of the landmarks of two articulations of each finger:
            - the TIP
            - the PIP
        If the y coordinate of the tip is lower than the y coordinate of the PIP, the finger is bent.
        '''
        if self.lmList:
            # Index
            if self.lmList[constants.LANDMARKS["INDEX_FINGER_TIP"]][2] < self.lmList[constants.LANDMARKS["INDEX_FINGER_PIP"]][2]:
                self.fingers[0] = 1
            else:
                self.fingers[0] = 0
            # Middle
            if self.lmList[constants.LANDMARKS["MIDDLE_FINGER_TIP"]][2] < self.lmList[constants.LANDMARKS["MIDDLE_FINGER_PIP"]][2]:
                self.fingers[1] = 1
            else:
                self.fingers[1] = 0
            # Ring
            if self.lmList[constants.LANDMARKS["RING_FINGER_TIP"]][2] < self.lmList[constants.LANDMARKS["RING_FINGER_PIP"]][2]:
                self.fingers[2] = 1
            else:
                self.fingers[2] = 0
            # Pinky
            if self.lmList[constants.LANDMARKS["PINKY_TIP"]][2] < self.lmList[constants.LANDMARKS["PINKY_PIP"]][2]:
                self.fingers[3] = 1
            else:    
                self.fingers[3] = 0