import cv2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, Concatenate
from tensorflow.keras.utils import to_categorical
import numpy as np

def extract_edges(image,meth):
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

def preprocess_with_contours(x_data, meth):
    x_processed = []
    for img in x_data:
        contours = extract_edges(img, meth)
        contours_resized = cv2.resize(contours, (28, 28))
        combined_features = np.concatenate((img[..., np.newaxis], contours_resized[..., np.newaxis]), axis=-1)
        x_processed.append(combined_features)
    return x_processed

def evaluate_model(model_file, x_test_processed, y_test):
    model = load_model(model_file)
    _, accuracy = model.evaluate(x_test_processed, y_test, verbose=0)
    return accuracy

def main():

    #CANNY
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # Preproccessing
    x_train_processed = preprocess_with_contours(x_train, "Canny")
    x_test_processed = preprocess_with_contours(x_test, "Canny")

    x_train_processed = np.array(x_train_processed)
    x_test_processed = np.array(x_test_processed)

    x_train_processed = x_train_processed.astype('float32') / 255.0
    x_test_processed = x_test_processed.astype('float32') / 255.0

    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    # Creation of the model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 2)), 
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    # build and train the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train_processed, y_train, epochs=20, batch_size=128, validation_data=(x_test_processed, y_test))
    model.save('model_Canny.h5')


    #SOBEL
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # Preproccessing
    x_train_processed = preprocess_with_contours(x_train, "Sobel")
    x_test_processed = preprocess_with_contours(x_test, "Sobel")

    x_train_processed = np.array(x_train_processed)
    x_test_processed = np.array(x_test_processed)

    x_train_processed = x_train_processed.astype('float32') / 255.0
    x_test_processed = x_test_processed.astype('float32') / 255.0

    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    # Creation of the model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 2)), 
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    # build and train the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train_processed, y_train, epochs=20, batch_size=128, validation_data=(x_test_processed, y_test))
    model.save('model_Sobel.h5')
    
    #LAPLACIAN
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # Preproccessing
    x_train_processed = preprocess_with_contours(x_train, "Laplacian")
    x_test_processed = preprocess_with_contours(x_test, "Laplacian")

    x_train_processed = np.array(x_train_processed)
    x_test_processed = np.array(x_test_processed)

    x_train_processed = x_train_processed.astype('float32') / 255.0
    x_test_processed = x_test_processed.astype('float32') / 255.0

    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    # Creation of the model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 2)), 
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])

    # build and train the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(x_train_processed, y_train, epochs=20, batch_size=128, validation_data=(x_test_processed, y_test))
    model.save('model_Laplacian.h5')

    #Precision of the different models
    methods = ["Canny", "Sobel", "Laplacian"]
    for method in methods:
        x_test_processed = preprocess_with_contours(x_test, method)
        x_test_processed = np.array(x_test_processed)
        x_test_processed = x_test_processed.astype('float32') / 255.0

        accuracy = evaluate_model(f'model_{method}.h5', x_test_processed, y_test)
        print(f"Precision of the model with edges ({method}): {accuracy}")

    


if __name__ == '__main__':
    main()