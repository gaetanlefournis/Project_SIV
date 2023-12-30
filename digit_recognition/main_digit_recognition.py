import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def main_digit_recognition(img : np.ndarray) -> int:
    """This function is the main function of the digit recognition.
    
    Parameters :
        img (np.ndarray) : image of the digit
        
    Returns :
        digit (int) : The recognized digit
    """
    
    model = load_model('digit_recognition/model_Sobel.h5') 
    model1 = load_model('digit_recognition/model_Canny.h5') 
    model2 = load_model('digit_recognition/model_Sobel.h5')
    model3 = load_model('digit_recognition/model_Laplacian.h5')
    # Convert the image into a 28x28 image in grayscale
    
    # Convert the image to a numpy array
    img_array = image.img_to_array(img)
    img_array /= 255.0  # Normalization of pixel values

    # Resize the image to match the format expected by the model (28x28 pixels)
    img_array = np.expand_dims(img_array, axis=0)

    # Make the prediction
    prediction = model.predict(img_array) #most effective model

    # Get the index of the predicted class (the recognized digit)
    digit = np.argmax(prediction)

    return digit