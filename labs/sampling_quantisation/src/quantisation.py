"""Runnable reconstruction of the quantisation code preserved in screenshots."""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from image_lab.runtime import data_path, finish
from image_lab.operations import quantize_u8, mse_psnr

image = cv2.imread(str(data_path("lenna512.bmp")), cv2.IMREAD_GRAYSCALE)
levels = [128, 64, 32, 16, 8, 2]
errors, psnrs = [], []
fig, axes = plt.subplots(2, 4, figsize=(12, 7))
axes.flat[0].imshow(image, cmap="gray", vmin=0, vmax=255)
axes.flat[0].set_title("Original")
for index, count in enumerate(levels, 1):
    quantized = quantize_u8(image, count)
    mse, psnr = mse_psnr(image, quantized)
    errors.append(mse); psnrs.append(psnr)
    axes.flat[index].imshow(quantized, cmap="gray", vmin=0, vmax=255)
    axes.flat[index].set_title(f"{count} levels")
    print(f"levels={count}, MSE={mse:.6f}, PSNR={psnr:.6f} dB")
for axis in axes.flat: axis.axis("off")
fig.tight_layout()
fig2, axes2 = plt.subplots(1, 2, figsize=(10, 4))
steps = 256 / np.array(levels)
axes2[0].plot(steps, errors, "o-"); axes2[0].set_ylabel("MSE")
axes2[1].plot(steps, psnrs, "o-"); axes2[1].set_ylabel("PSNR (dB)")
for axis in axes2:
    axis.set_xlabel("Quantisation step"); axis.grid(True)
fig2.tight_layout()
finish(__file__)
