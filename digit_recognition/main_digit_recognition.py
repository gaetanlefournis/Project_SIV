import numpy as np
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def main_digit_recognition(img : np.ndarray) -> int:
    """This function is the main function of the digit recognition.
    
    Parameters :
        img (np.ndarray) : image of the digit
        
    Returns :
        digit (int) : The recognized digit
    """
    
    model = load_model('digit_recognition/model_digit_recognition.h5') 
    model1 = load_model('digit_recognition/model_Canny.h5') 
    model2 = load_model('digit_recognition/model_Sobel.h5')
    model3 = load_model('digit_recognition/model_Laplacian.h5')

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
    prediction = model2.predict(img_array)

    # Get the index of the predicted class (the recognized digit)
    digit = np.argmax(prediction)

    return digit