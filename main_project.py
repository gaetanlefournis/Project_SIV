import cv2
import time
import hand_detection as hd
import graphical_user_interface as gui
import utils.utils as utils

def main():
    '''This function is the main function of the project.'''

    # Initialize the webcam
    #######################
    time.sleep(1) 
    cap = cv2.VideoCapture(0)
    cap.set(3, gui.WIDTH_CAMERA)
    cap.set(4, gui.HEIGHT_CAMERA)

    # Initialize the objects
    ########################
    detector = hd.hand_detector.HandDetector()
    display = hd.hand_display.Display()
    if gui.MAIN_GRID_SIZE == 4:
        grid = gui.interface_grid.Grid(gui.MAIN_GRID_COORDINATES, gui.LIST_DIGITS_INITIAL_4)
    elif gui.MAIN_GRID_SIZE == 9:
        grid = gui.interface_grid.Grid(gui.MAIN_GRID_COORDINATES, gui.LIST_DIGITS_INITIAL_9)

    # initialize the time to calculate the frame rate
    #################################################
    pTime = 0 

    while True:

        # Acquisition of the image
        ##########################
        _, img = cap.read()
        img = cv2.flip(img, 1)  # 1 for horizontal flip
        img = cv2.resize(img, (gui.WIDTH_CAMERA, gui.HEIGHT_CAMERA))
        img = utils.convert_to_RGB(img)

        # main_detector
        ###############
        img, coordinates_click, hand_barycenter = hd.main_hand_detection.main_hand_detection(img, detector, display)

        # main_interface
        ################
        gui.main_interface.main_interface(img, grid, coordinates_click, hand_barycenter)

        # Display the image and the frame rate
        ######################################
        detector.img = utils.convert_to_BGR(detector.img)
        fps, pTime = utils.calculate_frame_rate(pTime)
        display.draw_frame_rate(detector.img, fps)
        cv2.imshow("Image", detector.img)

        # Quit if 'q' is pressed
        ########################
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    #########################################
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()