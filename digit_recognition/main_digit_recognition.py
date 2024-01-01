import numpy as np
import cv2
from tensorflow.keras.models import load_model

from digit_recognition import model_edges as me
import graphical_user_interface as gui

def main_digit_recognition(img : np.ndarray, method : str = "main") -> int:
    """This function is the main function of the digit recognition.
    
    Parameters :
        img (np.ndarray) : image of the digit
        
    Returns :
        digit (int) : The recognized digit
    """
    if method == "main":
        model_used = load_model('digit_recognition/model_digit_recognition.h5') 
        # Resize the image to 28x28 pixels
        img_resized = cv2.resize(img, (28, 28))

        # Check if the image has multiple channels (e.g., BGR)
        if len(img_resized.shape) == 3 and img_resized.shape[2] == 3:
            img_gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
        else:
            img_gray = img_resized  # If it's already a single-channel image, no need to convert
        
        # Normalize pixel values
        img_array = img_gray.reshape((28, 28, 1)) / 255.0

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # Make the prediction
        prediction = model_used.predict(img_array)
    
    else:
        if method == "Canny":
            model_used = load_model('digit_recognition/model_Canny.h5')
        elif method == "Sobel":
            model_used = load_model('digit_recognition/model_Sobel.h5')
        elif method == "Laplacian":
            model_used = load_model('digit_recognition/model_Laplacian.h5')

        # Resize the image to 28x28 pixels
        img_resized = cv2.resize(img, (28, 28))

        # Smooth the image
        img_filtered = cv2.filter2D(img_resized, -1, gui.KERNEL_FILTER)

        # Extract the edges
        img_edges = me.extract_edges(img_filtered, method)

        # Normalize pixel values
        img_normalized = img_edges.reshape((28, 28, 1)) 

        # Add batch dimension
        img_array = np.expand_dims(img_normalized, axis=0)

        # Make the prediction
        prediction = model_used.predict(img_array)

    # Get the index of the predicted class (the recognized digit)
    digit = np.argmax(prediction)

    return digit