# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:52:18 2024

@author: greg7
"""

from image_lab.runtime import data_path, finish, michelson
import cv2
from skimage import io
import matplotlib.pyplot as plt
import numpy as np


# Charger l'image en niveaux de gris
image_path=str(data_path('flowers.tif'))
img=io.imread(image_path, as_gray=True)
img_uint8 = (img * 255).astype(np.uint8)

# Application des différents filtres
blur = cv2.blur(src=img_uint8, ksize=(5,5))
gaussian_blur = cv2.GaussianBlur(src= img_uint8, ksize=(5,5), sigmaX=0, sigmaY=0)
median_blur = cv2.medianBlur(src=img_uint8, ksize=5)
bilateral_filter = cv2.bilateralFilter(src= img_uint8, d=9, sigmaColor=75, sigmaSpace=75)

# Affichage des résultats
plt.figure(figsize=(20, 10))

# Image originale
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Image Originale')
plt.axis('off')

# Filtre moyenneur (blur)
plt.subplot(2, 3, 2)
plt.imshow(blur, cmap='gray')
plt.title('Filtre Moyenneur (cv2.blur)')
plt.axis('off')

# Filtre Gaussien
plt.subplot(2, 3, 3)
plt.imshow(gaussian_blur, cmap='gray')
plt.title('Filtre Gaussien (cv2.GaussianBlur)')
plt.axis('off')

# Filtre Médian
plt.subplot(2, 3, 4)
plt.imshow(median_blur, cmap='gray')
plt.title('Filtre Médian (cv2.medianBlur)')
plt.axis('off')

# Filtre Bilatéral
plt.subplot(2, 3, 5)
plt.imshow(bilateral_filter, cmap='gray')
plt.title('Filtre Bilatéral (cv2.bilateralFilter)')
plt.axis('off')

finish(__file__)
