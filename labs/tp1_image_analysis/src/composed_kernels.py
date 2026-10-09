# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:49:59 2024

@author: greg7
"""

from image_lab.runtime import data_path, finish, michelson
import numpy as np
from scipy.signal import convolve2d
import matplotlib.pyplot as plt

# Définir les masques
M = np.array([[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]])

M1 = np.array([[1, 1, 1],
               [0, 0, 0],
               [-1, -1, -1]])

M2 = np.array([[1, 0, -1],
               [1, 0, -1],
               [1, 0, -1]])

# Calculer D1 et D2 par convolution
D1 = convolve2d(M, M1, mode='full')
D2 = convolve2d(M, M2, mode='full')

print("Masque D1 :\n", D1)
print("Masque D2 :\n", D2)

# Calcul de la réponse fréquentielle (FFT 2D)
D1_fft = np.fft.fftshift(np.fft.fft2(D1))
D2_fft = np.fft.fftshift(np.fft.fft2(D2))

# Magnitude du spectre de fréquence
D1_magnitude = np.abs(D1_fft)
D2_magnitude = np.abs(D2_fft)

# Affichage des réponses fréquentielles
plt.figure(figsize=(12, 6))

# Réponse fréquentielle de D1
plt.subplot(1, 2, 1)
plt.title("Réponse fréquentielle de D1")
plt.imshow(D1_magnitude, cmap='gray')
plt.colorbar()

# Réponse fréquentielle de D2
plt.subplot(1, 2, 2)
plt.title("Réponse fréquentielle de D2")
plt.imshow(D2_magnitude, cmap='gray')
plt.colorbar()

finish(__file__)
