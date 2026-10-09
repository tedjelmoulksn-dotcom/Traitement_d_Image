# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 18:30:19 2024

@author: greg7
"""

from image_lab.runtime import data_path, finish, michelson
import numpy as np
import matplotlib.pyplot as plt

# Masque M
M = np.array([[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]])

# Dimensions du masque
rows, cols = M.shape

# Créer une grille de fréquences normalisées dans [-1, 1]
u = np.linspace(-0.5, 0.5, 100)
v = np.linspace(-0.5, 0.5, 100)
U, V = np.meshgrid(u, v)

# Calculer la réponse fréquentielle H(u, v)
H = np.zeros(U.shape, dtype=complex)

# Transformée de Fourier discrète pour chaque fréquence (u, v)
for x in range(rows):
    for y in range(cols):
        H += M[x, y] * np.exp(-2j * np.pi * (U * x + V * y))

# Calculer le module de la réponse fréquentielle
H_magnitude = np.abs(H)

# Tracer la réponse fréquentielle en 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Surface 3D de la réponse fréquentielle
ax.plot_surface(U, V, H_magnitude, cmap='viridis')

# Étiquettes des axes
ax.set_title("Réponse fréquentielle du masque M")
ax.set_xlabel('Frequency u (cycles/pixel)')
ax.set_ylabel('Frequency v (cycles/pixel)')
ax.set_zlabel('|H(u, v)|')

finish(__file__)
