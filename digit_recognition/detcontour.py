import cv2
import matplotlib.pyplot as plt

# Charger une image en niveaux de gris
image = cv2.imread("C:\\Users\\danhe\\OneDrive\\Documents\\Projetstrento\\Project_SIV\\digit_recognition\\model1.png", 0)

# Méthode de détection de contours : Canny
edges_canny = cv2.Canny(image, 100, 200)

# Méthode de détection de contours : Sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = cv2.magnitude(sobel_x, sobel_y)

# Méthode de détection de contours : Laplacian
edges_laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Affichage des résultats
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Image Originale')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(edges_canny, cmap='gray')
plt.title('Contours (Canny)')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(edges_sobel, cmap='gray')
plt.title('Contours (Sobel)')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(edges_laplacian, cmap='gray')
plt.title('Contours (Laplacian)')
plt.axis('off')

plt.tight_layout()
plt.show()
