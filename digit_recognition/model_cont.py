import cv2
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout, Concatenate
from tensorflow.keras.utils import to_categorical
import numpy as np

def extract_contours(image,meth):
    # Utilisez les méthodes de détection de contours d'OpenCV ici (Sobel, Canny, Laplacian)
    # Par exemple, pour la méthode Canny :
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

def preprocess_with_contours(x_data):
    x_processed = []
    for img in x_data:
        contours = extract_contours(img, "Canny")
        contours_resized = cv2.resize(contours, (28, 28))
        # Combiner les caractéristiques de contour avec les images originales
        combined_features = np.concatenate((img[..., np.newaxis], contours_resized[..., np.newaxis]), axis=-1) # Concaténez les caractéristiques de contour avec l'image
        x_processed.append(combined_features)
    return x_processed

def main():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Prétraitement des données avec contours
    x_train_processed = preprocess_with_contours(x_train)
    x_test_processed = preprocess_with_contours(x_test)

    # Conversion en tableaux numpy
    x_train_processed = np.array(x_train_processed)
    x_test_processed = np.array(x_test_processed)

    # Normalisation des valeurs des pixels
    x_train_processed = x_train_processed.astype('float32') / 255.0
    x_test_processed = x_test_processed.astype('float32') / 255.0

    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    # Création du modèle CNN prenant en compte les contours
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 2)),  # L'image a maintenant deux canaux (original + contour)
        MaxPooling2D((2, 2)),
        Dropout(0.25),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(10, activation='softmax')
        # Ajoutez des couches pour traiter les caractéristiques de contour ici
        # Par exemple, Conv2D, MaxPooling2D, Flatten, etc.
        # Assurez-vous de modifier l'architecture pour fusionner les caractéristiques de contour avec les images MNIST

        # Ensuite, ajoutez les couches CNN existantes pour traiter les données combinées
    ])

    # Compiler et entraîner le modèle
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Entraînement du modèle
    history = model.fit(x_train_processed, y_train, epochs=20, batch_size=128, validation_data=(x_test_processed, y_test))


    model.save('modele_reconnaissance_chiffres_contours.h5')

if __name__ == '__main__':
    main()
