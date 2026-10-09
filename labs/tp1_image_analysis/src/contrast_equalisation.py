from image_lab.runtime import data_path, finish, michelson
import cv2
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal
from skimage import io

# Chargement des images
img1 = io.imread(str(data_path('poupee.tif')))
img2 = io.imread(str(data_path('crane.png')))

# Si les images sont en couleur, conversion en niveaux de gris
if len(img1.shape) == 3:
    img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
if len(img2.shape) == 3:
    img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

# Calcul du contraste de Michelson
michelson_contrast_img1 = michelson(img1)
michelson_contrast_img2 = michelson(img2)

# Calcul du contraste global
global_contrast_img1 = np.std(img1) / np.mean(img1)
global_contrast_img2 = np.std(img2) / np.mean(img2)

# Calcul du contraste RMS
rms_contrast_img1 = np.sqrt(np.mean(np.square(img1 - np.mean(img1))))
rms_contrast_img2 = np.sqrt(np.mean(np.square(img2 - np.mean(img2))))

# Calcul de la brillance (luminance)
brillance_img1 = np.mean(img1)
brillance_img2 = np.mean(img2)

# Affichage des résultats
print("Image: pouppe.tif")
print("Contraste Michelson:", michelson_contrast_img1)
print("Contraste Global:", global_contrast_img1)
print("Contraste RMS:", rms_contrast_img1)
print("Brillance:", brillance_img1)

print("\nImage: crane.tif")
print("Contraste Michelson:", michelson_contrast_img2)
print("Contraste Global:", global_contrast_img2)
print("Contraste RMS:", rms_contrast_img2)
print("Brillance:", brillance_img2)

# Visualisation des histogrammes
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(img1.flat, bins=256, range=(0, 255))
plt.title('Histogramme de pouppe.tif')

plt.subplot(1, 2, 2)
plt.hist(img2.flat, bins=256, range=(0, 255))
plt.title('Histogramme de crane.tif')

finish(__file__)
# Égalisation d'histogramme
img1_equalized = cv2.equalizeHist(img1)
img2_equalized = cv2.equalizeHist(img2)

# Affichage des histogrammes des images égalisées
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(img1_equalized.flat, bins=256, range=(0, 255))
plt.title('Histogramme égalisé de pouppe.tif')

plt.subplot(1, 2, 2)
plt.hist(img2_equalized.flat, bins=256, range=(0, 255))
plt.title('Histogramme égalisé de crane.tif')

finish(__file__)
# Affichage des images égalisées
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img1_equalized, cmap='gray')
plt.title('Image égalisée de pouppe.tif')

plt.subplot(1, 2, 2)
plt.imshow(img2_equalized, cmap='gray')
plt.title('Image égalisée de crane.tif')

finish(__file__)
# Calcul du contraste pour les images égalisées
michelson_contrast_img1_eq = michelson(img1_equalized)
global_contrast_img1_eq = np.std(img1_equalized) / np.mean(img1_equalized)
rms_contrast_img1_eq = np.sqrt(np.mean(np.square(img1_equalized - np.mean(img1_equalized))))

michelson_contrast_img2_eq = michelson(img2_equalized)
global_contrast_img2_eq = np.std(img2_equalized) / np.mean(img2_equalized)
rms_contrast_img2_eq = np.sqrt(np.mean(np.square(img2_equalized - np.mean(img2_equalized))))

# Affichage des résultats
print("Image égalisée: pouppe.tif")
print("Contraste Michelson:", michelson_contrast_img1_eq)
print("Contraste Global:", global_contrast_img1_eq)
print("Contraste RMS:", rms_contrast_img1_eq)

print("\nImage égalisée: crane.tif")
print("Contraste Michelson:", michelson_contrast_img2_eq)
print("Contraste Global:", global_contrast_img2_eq)
print("Contraste RMS:", rms_contrast_img2_eq)
# Application de CLAHE (égalisation adaptative)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
img1_clahe = clahe.apply(img1)
img2_clahe = clahe.apply(img2)

# Affichage des images égalisées de manière adaptative
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img1_clahe, cmap='gray')
plt.title('Image CLAHE de pouppe.tif')

plt.subplot(1, 2, 2)
plt.imshow(img2_clahe, cmap='gray')
plt.title('Image CLAHE de crane.tif')

finish(__file__)


# Calcul du contraste pour les images CLAHE
michelson_contrast_img1_clahe = michelson(img1_clahe)
global_contrast_img1_clahe = np.std(img1_clahe) / np.mean(img1_clahe)
rms_contrast_img1_clahe = np.sqrt(np.mean(np.square(img1_clahe - np.mean(img1_clahe))))

michelson_contrast_img2_clahe = michelson(img2_clahe)
global_contrast_img2_clahe = np.std(img2_clahe) / np.mean(img2_clahe)
rms_contrast_img2_clahe = np.sqrt(np.mean(np.square(img2_clahe - np.mean(img2_clahe))))

# Affichage des résultats
print("Image CLAHE: pouppe.tif")
print("Contraste Michelson:", michelson_contrast_img1_clahe)
print("Contraste Global:", global_contrast_img1_clahe)
print("Contraste RMS:", rms_contrast_img1_clahe)

print("\nImage CLAHE: crane.tif")
print("Contraste Michelson:", michelson_contrast_img2_clahe)
print("Contraste Global:", global_contrast_img2_clahe)
print("Contraste RMS:", rms_contrast_img2_clahe)

