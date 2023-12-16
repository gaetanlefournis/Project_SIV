import numpy as np
import cv2

from hand_detection import constants

class Display():
    '''This class is used to perform all the display actions.

    Methods:
        draw_landmark: draws a single landmark on an image
        draw_landmarks: draws the landmarks given by the list of articulations
        draw_barycenter: draws the barycenter of the hand on the image
        draw_frame_rate: displays the frame rate on the image
    '''


    def __init__(self) -> None:
        pass

    def draw_landmark(self, img:np.ndarray, lmList:list, index: int) -> None:
        '''This function draws a single landmark on an image.
        
        Args:
            img (np.ndarray): image
            lmList (list): list of landmarks
            index (int): number associated with the articulation to draw
            
        Returns:
            None
        '''
        cv2.circle(img, (lmList[index][1], lmList[index][2]), 3, (255, 0, 255), cv2.FILLED)
    
    def draw_landmarks(self, img:np.ndarray, lmList: list, list_articulations: list[str] = "all") -> None:
        '''This function draws the landmarks given by the list of articulations. If no list is given, it draws all the landmarks.
        
        Args:
            img (np.ndarray): image
            lmList (list): list of all the landmarks
            list_articulations (list): list of the articulations to draw

        Returns:
            None
        '''
        if lmList:
            if list_articulations == "all":
                for articulation in constants.LANDMARKS.values():
                    self.draw_landmark(img, lmList, articulation)

            else:
                for articulation1 in list_articulations:
                    articulation = constants.LANDMARKS[articulation1]
                    self.draw_landmark(img, lmList, articulation)

    def draw_barycenter(self, img:np.ndarray, barycenter: tuple) -> None:
        '''This function draws the barycenter of the hand on the image.
        
        Args:
            img (np.ndarray): image
            barycenter (tuple): barycenter of the hand

        Returns:
            None
        '''
        cv2.circle(img, barycenter, 4, (0, 255, 0), cv2.FILLED)
    
    def draw_frame_rate(self, img:np.ndarray, fps:int) -> None:
        '''This function displays the frame rate on the image.
        
        Args:
            img (np.ndarray): image
            fps (int): frame rate

        Returns:
            None
        '''
        cv2.putText(img, str(int(fps)), (10,40), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)