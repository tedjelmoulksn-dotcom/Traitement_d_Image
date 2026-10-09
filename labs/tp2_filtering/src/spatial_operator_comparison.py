# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:51:54 2024

@author: 12108993
"""
from image_lab.runtime import data_path, finish, michelson
import cv2
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal




image_path=str(data_path('flowers.tif'))
img=io.imread(image_path,as_gray=True)


# 2. Créer le noyau de filtre 3x3 (kernel1)
kernel1 =np.array([[0, -1, 0],
                   [1, 1, 1],
                    [0, -1, 0]]
                          )
kernel2 =np.array([[0, -1, 0],
                   [-1, 1, 1],
                    [0, 1, 0]]
                          )

filtered_image_cv2_kernel1=cv2.filter2D(src=img.astype(np.float64), ddepth=cv2.CV_64F, kernel=np.flip(kernel1), borderType=cv2.BORDER_REFLECT)
filtered_image_convolve_kernel1=signal.convolve2d(img.astype(np.float64), kernel1, mode='same', boundary = 'symm')

filtered_image_cv2_kernel2=cv2.filter2D(src=img.astype(np.float64), ddepth=cv2.CV_64F, kernel=np.flip(kernel2), borderType=cv2.BORDER_REFLECT)
filtered_image_convolve_kernel2=signal.convolve2d(img.astype(np.float64), kernel2, mode='same', boundary = 'symm')

# Affichage des résultats
plt.figure(figsize=(20, 10))

# Image originale
plt.subplot(2, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Image Originale')
plt.axis('off')

# Image filtrée avec cv2.filter2D (kernel1)
plt.subplot(2, 3, 2)
plt.imshow(filtered_image_cv2_kernel1, cmap='gray')
plt.title('Filtre avec cv2.filter2D (kernel1)')
plt.axis('off')

# Image filtrée avec convolve2d (kernel1)
plt.subplot(2, 3, 3)
plt.imshow(filtered_image_convolve_kernel1, cmap='gray')
plt.title('Filtre avec convolve2d (kernel1)')
plt.axis('off')

# Image filtrée avec cv2.filter2D (kernel2)
plt.subplot(2, 3, 4)
plt.imshow(filtered_image_cv2_kernel2, cmap='gray')
plt.title('Filtre avec cv2.filter2D (kernel2)')
plt.axis('off')

# Image filtrée avec convolve2d (kernel2)
plt.subplot(2, 3, 5)
plt.imshow(filtered_image_convolve_kernel2, cmap='gray')
plt.title('Filtre avec convolve2d (kernel2)')
plt.axis('off')

finish(__file__)