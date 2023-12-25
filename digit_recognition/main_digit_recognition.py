import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

def main():
    # Charger le modèle pré-entraîné pour la reconnaissance des chiffres
    model = load_model('modele_reconnaissance_chiffres.h5')  # Assure-toi de remplacer 'modele_reconnaissance_chiffres.h5' par le chemin de ton propre modèle

    # Charger et prétraiter l'image avec le chiffre manuscrit
    img_path = "C:\\Users\\danhe\\OneDrive\\Documents\\Projetstrento\\Project_SIV\\digit_recognition\\model1.png"
    img = image.load_img(img_path, target_size=(28, 28), color_mode='grayscale')

    img_array = image.img_to_array(img)
    img_array /= 255.0  # Normalisation des valeurs des pixels

    # Redimensionner l'image pour correspondre au format attendu par le modèle (28x28 pixels)
    img_input = np.expand_dims(img_array, axis=0)

    # Faire la prédiction
    prediction = model.predict(img_input)

    # Obtenir l'indice de la classe prédite (le chiffre reconnu)
    predicted_class = np.argmax(prediction)

    print("Le chiffre reconnu est :", predicted_class)

if __name__ == '__main__':
    main()