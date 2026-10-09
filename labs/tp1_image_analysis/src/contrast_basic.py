# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:11:26 2024

@author: greg7
"""

from image_lab.runtime import data_path, finish, michelson
import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal
from mpl_toolkits import mplot3d

# Charger les images
image1 = cv2.imread(str(data_path('poupee.tif')), cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(str(data_path('crane.png')), cv2.IMREAD_GRAYSCALE)

# 1. Calculer trois contrastes possibles : Michelson, Global, RMS
def michelson_contrast(img):
    I_min = np.min(img)
    I_max = np.max(img)
    return michelson(img)

def global_contrast(img):
    return np.std(img)

def rms_contrast(img):
    return np.sqrt(np.mean(np.square(img - np.mean(img))))

def print_contrasts(image, name):
    michelson = michelson_contrast(image)
    global_contrast_value = global_contrast(image)
    rms = rms_contrast(image)
    print(f'Contrastes pour {name}:')
    print(f'Michelson: {michelson:.4f}')
    print(f'Global: {global_contrast_value:.4f}')
    print(f'RMS: {rms:.4f}\n')

# Afficher les contrastes pour chaque image
print_contrasts(image1, "pouppe")
print_contrasts(image2, "crane")

# 2. Calculer la brillance (ou luminance)
def luminance(img):
    return np.mean(img)

print(f'Brillance pour pouppe: {luminance(image1):.4f}')
print(f'Brillance pour crane: {luminance(image2):.4f}\n')

# 3. Visualiser l'histogramme
def show_histogram(img, name, bins=256):
    plt.hist(img.flat, bins=bins, range=(0, 255))
    plt.title(f'Histogramme de {name}')
    finish(__file__)

# Visualiser les histogrammes des images
show_histogram(image1, "pouppe")
show_histogram(image2, "crane")

# 4. Explication de l'égalisation d'histogramme
'''
L'égalisation d'histogramme est une technique qui redistribue les niveaux de gris de l'image
de manière à mieux répartir les pixels sur toute la gamme possible. Cela améliore le contraste global de l'image.
'''

# 5. Visualiser les histogrammes des images égalisées
equalized_image1 = cv2.equalizeHist(image1)
equalized_image2 = cv2.equalizeHist(image2)

show_histogram(equalized_image1, "pouppe égalisée")
show_histogram(equalized_image2, "crane égalisée")

# 6. Visualiser les images égalisées
def show_image(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.axis('off')
    finish(__file__)

show_image(equalized_image1, "pouppe égalisée")
show_image(equalized_image2, "crane égalisée")

# 7. Mesurer le contraste des images égalisées
print_contrasts(equalized_image1, "pouppe égalisée")
print_contrasts(equalized_image2, "crane égalisée")

# 8. Explication de l'égalisation adaptative d’histogramme (CLAHE)
'''
L'égalisation adaptative d'histogramme (CLAHE) applique une égalisation sur de petites régions de l'image
appelées "tiles", puis combine ces régions pour créer une image contrastée globalement. Cela permet d'améliorer
localement le contraste sans surexposer certaines parties.
'''

# 9. Visualiser les images égalisées de manière adaptative
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_image1 = clahe.apply(image1)
clahe_image2 = clahe.apply(image2)

show_image(clahe_image1, "pouppe avec CLAHE")
show_image(clahe_image2, "crane avec CLAHE")

# 10. Mesurer le contraste des images CLAHE
print_contrasts(clahe_image1, "pouppe avec CLAHE")
print_contrasts(clahe_image2, "crane avec CLAHE")
