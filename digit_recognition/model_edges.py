import cv2
import numpy as np
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.backend import clear_session


def extract_edges(image :np.ndarray, meth : str) -> np.ndarray:
    '''This function is the function that extracts the edges of an image, in function of the given method.'''
    if meth == "Canny":
        edges = cv2.Canny(image, 100, 200)
    elif meth == "Sobel":
        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        edges = cv2.magnitude(sobel_x, sobel_y)
    elif meth == "Laplacian":
        edges = cv2.Laplacian(image, cv2.CV_64F)
    else:
        return False
    return edges

def preprocess_with_contours(x_data : list, meth : str) -> list:
    '''This function is the function that preprocesses the data with contours.'''
    x_processed = []
    for img in x_data:
        contours = extract_edges(img, meth)
        contours_resized = cv2.resize(contours, (28, 28))
        contours_resized = contours_resized.reshape((28, 28, 1)) 
        x_processed.append(contours_resized)
    return x_processed

def evaluate_model(model_file : str, x_test_processed : np.ndarray, y_test : np.ndarray) -> float:
    '''This function is the function that evaluates the models for digit recognition.'''
    model = load_model(model_file)
    _, accuracy = model.evaluate(x_test_processed, y_test, verbose=0)
    return accuracy

def train_and_save_model(x_train_processed : np.ndarray, x_test_processed : np.ndarray, y_train : np.ndarray, y_test : np.ndarray, model_filename : str) -> Sequential:
    '''This function is the function that create and train the model for digit recognition.'''
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    _ = model.fit(x_train_processed, y_train, epochs=20, batch_size=128, validation_data=(x_test_processed, y_test))
    model.save(model_filename)
    return model

def main():
    '''This function is the function that creates the different models for digit recognition.'''
    methods = ["Canny", "Sobel", "Laplacian"]
    
    for method in methods:
        clear_session()  # Clear previous model's state
        
        # Load MNIST data
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        
        # Preprocess data
        x_train_processed = preprocess_with_contours(x_train, "Laplacian")
        x_test_processed = preprocess_with_contours(x_test, method)

        x_train_processed = np.array(x_train_processed)
        x_test_processed = np.array(x_test_processed)

        x_train_processed = x_train_processed.astype('float32') / 255.0
        x_test_processed = x_test_processed.astype('float32') / 255.0

        y_train = to_categorical(y_train, num_classes=10)
        y_test = to_categorical(y_test, num_classes=10)

        # Train and save the model
        model_filename = f'digit_recognition/model_{method}.h5'
        train_and_save_model(x_train_processed, x_test_processed, y_train, y_test, model_filename)

        # Evaluate the model
        x_test_processed_current = preprocess_with_contours(x_test, method)
        x_test_processed_current = np.array(x_test_processed_current)
        x_test_processed_current = x_test_processed_current.astype('float32') / 255.0

        accuracy = evaluate_model(model_filename, x_test_processed_current, y_test)
        print(f"Accuracy of the model with edges ({method}): {accuracy}")


if __name__ == '__main__':
    main()