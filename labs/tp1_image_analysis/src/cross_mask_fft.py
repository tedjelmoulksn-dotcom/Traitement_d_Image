from image_lab.runtime import data_path, finish, michelson
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft2, fftshift
from mpl_toolkits.mplot3d import Axes3D

# Définir le masque M
M = np.array([[0, 1, 0],
              [1, 1, 1],
              [0, 1, 0]])

# Taille de la FFT : on peut ajouter du padding pour visualiser plus de détails
padding_size = 20  # Taille du padding (zéro-padding) pour augmenter la résolution de la FFT
M_padded = np.pad(M, ((padding_size, padding_size), (padding_size, padding_size)), mode='constant')

# Calculer la transformée de Fourier 2D et la centrer
M_fft = fft2(M_padded)
M_fft_shifted = fftshift(M_fft)  # Centrer la FFT pour visualiser les basses fréquences au centre

# Calculer le module (amplitude) de la réponse fréquentielle
M_magnitude = np.abs(M_fft_shifted)

# Générer les coordonnées de fréquences
freq_x = np.fft.fftfreq(M_padded.shape[1])
freq_y = np.fft.fftfreq(M_padded.shape[0])
freq_x_shifted = fftshift(freq_x)  # On centre les fréquences
freq_y_shifted = fftshift(freq_y)

# Créer une grille de coordonnées pour le tracé 3D
X, Y = np.meshgrid(freq_x_shifted, freq_y_shifted)

# Création de la figure 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Tracer la surface 3D
ax.plot_surface(X, Y, M_magnitude, cmap='viridis')

# Ajouter des labels et un titre
ax.set_title('Réponse fréquentielle du masque M (en 3D)')
ax.set_xlabel('Fréquence u')
ax.set_ylabel('Fréquence v')
ax.set_zlabel('Amplitude')

# Afficher la figure
finish(__file__)
