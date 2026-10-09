from image_lab.runtime import data_path, finish, michelson
import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Charger l'image en niveaux de gris
img = cv2.imread(str(data_path('lenna512.bmp')), cv2.IMREAD_GRAYSCALE)

# Appliquer les filtres Sobel, Prewitt, Roberts, et Laplacien
# Sobel
sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # Sobel en x (horizontal)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)  # Sobel en y (vertical)

# Prewitt
prewitt_kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
prewitt_kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
prewittx = signal.convolve2d(img, prewitt_kernel_x, boundary='symm', mode='same')
prewitty = signal.convolve2d(img, prewitt_kernel_y, boundary='symm', mode='same')

# Roberts
roberts_kernel_x = np.array([[1, 0], [0, -1]])
roberts_kernel_y = np.array([[0, 1], [-1, 0]])
robertsx = signal.convolve2d(img, roberts_kernel_x, boundary='symm', mode='same')
robertsy = signal.convolve2d(img, roberts_kernel_y, boundary='symm', mode='same')

# Laplacien
laplacian = cv2.Laplacian(src=img, ddepth=cv2.CV_64F)

# Afficher les résultats
plt.figure(figsize=(12, 8))

plt.subplot(2, 4, 1), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
plt.subplot(2, 4, 2), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y')

plt.subplot(2, 4, 3), plt.imshow(prewittx, cmap='gray'), plt.title('Prewitt X')
plt.subplot(2, 4, 4), plt.imshow(prewitty, cmap='gray'), plt.title('Prewitt Y')

plt.subplot(2, 4, 5), plt.imshow(robertsx, cmap='gray'), plt.title('Roberts X')
plt.subplot(2, 4, 6), plt.imshow(robertsy, cmap='gray'), plt.title('Roberts Y')

plt.subplot(2, 4, 7), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')

plt.tight_layout()
finish(__file__)
