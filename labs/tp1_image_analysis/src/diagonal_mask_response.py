# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 2024

@author: greg7
"""

from image_lab.runtime import data_path, finish, michelson
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Définir le masque diagonal kernel M0
M0 = np.array([[0, 1, 1],
               [-1, 0, 1],
               [-1, -1, 0]])

# Augmenter la taille du masque en ajoutant des zéros autour (padding)
large_M0 = np.pad(M0, pad_width=((20, 20), (20, 20)), mode='constant')

# Calculer la réponse fréquentielle (FFT 2D)
M0_fft = np.fft.fftshift(np.fft.fft2(large_M0))

# Magnitude du spectre de fréquence
M0_magnitude = np.abs(M0_fft)

# Obtenir la taille du masque étendu
N, M = large_M0.shape

# Créer une grille de fréquences normalisées (de -1 à 1)
X = np.fft.fftshift(np.fft.fftfreq(M))
Y = np.fft.fftshift(np.fft.fftfreq(N))
X, Y = np.meshgrid(X, Y)

# Tracer la réponse fréquentielle en 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, M0_magnitude, cmap='viridis', edgecolor='none')

# Ajouter des étiquettes et un titre
ax.set_title('Réponse fréquentielle du masque diagonal kernel M0 en 3D')
ax.set_xlabel('Frequency X (cycles/pixel)')
ax.set_ylabel('Frequency Y (cycles/pixel)')
ax.set_zlabel('Magnitude')

# Affichage de la figure
finish(__file__)
