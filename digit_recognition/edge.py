import cv2
import matplotlib.pyplot as plt

image = cv2.imread("digit_recognition/model1.png", 0)

# Edges detection method : Canny
edges_canny = cv2.Canny(image, 100, 200)

# Edges detection method : Sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
edges_sobel = cv2.magnitude(sobel_x, sobel_y)

# Edges detection method : Laplacian
edges_laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Results
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Originale picture')
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
