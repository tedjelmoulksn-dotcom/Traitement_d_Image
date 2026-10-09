from image_lab.runtime import data_path, finish, michelson
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger l'image en niveaux de gris
img = cv2.imread(str(data_path('flowers.tif')), cv2.IMREAD_GRAYSCALE)

# Appliquer le filtre Sobel
sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

# Magnitude des gradients (combinaison des directions X et Y)
sobel_magnitude = np.sqrt(sobelx**2 + sobely**2)

# Appliquer un seuil
seuil_bas = 50  # seuil inférieur
seuil_haut = 100  # seuil supérieur

_, sobel_threshold_low = cv2.threshold(sobel_magnitude, seuil_bas, 255, cv2.THRESH_BINARY)
_, sobel_threshold_high = cv2.threshold(sobel_magnitude, seuil_haut, 255, cv2.THRESH_BINARY)

# Afficher les résultats
plt.figure(figsize=(12, 6))

# Afficher l'image originale
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Image Originale')

# Afficher les images filtrées (Sobel X, Sobel Y, Magnitude)
plt.subplot(2, 3, 2), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X (filtré)')
plt.subplot(2, 3, 3), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y (filtré)')
plt.subplot(2, 3, 4), plt.imshow(sobel_magnitude, cmap='gray'), plt.title('Sobel Magnitude')

# Afficher les images après application des seuils
plt.subplot(2, 3, 5), plt.imshow(sobel_threshold_low, cmap='gray'), plt.title(f'Seuil {seuil_bas}')
plt.subplot(2, 3, 6), plt.imshow(sobel_threshold_high, cmap='gray'), plt.title(f'Seuil {seuil_haut}')

plt.tight_layout()
finish(__file__)
