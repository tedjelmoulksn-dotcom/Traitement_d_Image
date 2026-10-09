# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:51:54 2024

@author: 12108993
"""
import cv2
from skimage import io
from skimage.transform import downscale_local_mean
import matplotlib.pyplot as plt
from skimage.transform import rescale
import numpy as np
from scipy.signal import convolve2d
import scipy.signal as signal




image_path='Flowers.tif'
img=io.imread(image_path,as_gray=True)

# OpenCV fonctionne avec des images en format uint8, donc il faut convertir l'image
img_uint8 = (img * 255).astype(np.uint8)

# 2. Créer le noyau de filtre 3x3 (kernel1)
kernel1 =np.array([[0, -1, 0],
                   [1, 1, 1],
                    [0, -1, 0]]
                          )
kernel2 =np.array([[0, -1, 0],
                   [-1, 1, 1],
                    [0, 1, 0]]
                          )

filtered_image_cv2_kernel1=cv2.filter2D(src=img_uint8, ddepth=-1,kernel=kernel1)
filtered_image_convolve_kernel1=signal.convolve2d(np.float32(img), kernel1, mode='same', boundary = 'fill')

filtered_image_cv2_kernel2=cv2.filter2D(src=img_uint8, ddepth=-1,kernel=kernel2)
filtered_image_convolve_kernel2=signal.convolve2d(np.float32(img), kernel2, mode='same', boundary = 'fill')

# 3. Appliquer le filtre avec OpenCV filter2D
#filtered_image_cv2 = cv2.filter2D(src=img_uint8, ddepth=-1, kernel=kernel1)

# 4. Afficher l'image originale et filtrée
#plt.figure(figsize=(10, 5))

#plt.subplot(1, 2, 1)
#plt.imshow(img, cmap='gray')
#plt.title('Image originale')

#plt.subplot(1, 2, 2)
#plt.imshow(filtered_image_cv2, cmap='gray')
#plt.title('Image filtrée avec cv2.filter2D')

#plt.show()
# Affichage des résultats
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

plt.show()