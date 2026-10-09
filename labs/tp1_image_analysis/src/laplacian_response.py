# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:14:32 2024

@author: greg7
"""

from image_lab.runtime import data_path, finish, michelson
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy.fft import fft2, fftshift

# Charger l'image de Lena en niveaux de gris
img = cv2.imread(str(data_path('lenna512.bmp')), cv2.IMREAD_GRAYSCALE)

# Définir la réponse impulsionnelle du filtre
h = np.array([[0, 1, 0],
              [1, -4, 1],
              [0, 1, 0]])

# Appliquer le filtre sur l'image avec la convolution
filtered_img = cv2.filter2D(src=img, ddepth=cv2.CV_64F, kernel=h)

# Calcul de la réponse fréquentielle du filtre
H = fft2(h, s=(img.shape[0], img.shape[1]))
H_shifted = fftshift(H)  # Centrer la fréquence 0

# Magnitude de la réponse fréquentielle (pour la visualisation)
H_magnitude = np.abs(H_shifted)

# Afficher les résultats
plt.figure(figsize=(12, 8))

# Image originale
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Image originale (Lena)")

# Image filtrée
plt.subplot(2, 2, 2)
plt.imshow(filtered_img, cmap='gray')
plt.title("Image filtrée")

# Réponse impulsionnelle du filtre
plt.subplot(2, 2, 3)
plt.imshow(h, cmap='gray', extent=[-1, 1, -1, 1])
plt.title("Réponse impulsionnelle du filtre")

# Réponse fréquentielle (magnitude)
plt.subplot(2, 2, 4)
plt.imshow(np.log(1 + H_magnitude), cmap='gray')
plt.title("Réponse fréquentielle (magnitude)")

plt.tight_layout()
finish(__file__)
