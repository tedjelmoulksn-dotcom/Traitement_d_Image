"""Reconstruction of TP2's circular-mask FFT experiment from its report."""
from image_lab.runtime import data_path, finish
from image_lab.operations import frequency_filter
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

image = io.imread(data_path("flowers.tif"), as_gray=True)
for radius in [10, 100, 200]:
    for highpass in [False, True]:
        output, spectrum, mask = frequency_filter(image, radius, highpass)
        kind = "High-pass" if highpass else "Low-pass"
        fig, axes = plt.subplots(1, 4, figsize=(14, 4))
        axes[0].imshow(image, cmap="gray", vmin=0, vmax=1)
        axes[1].imshow(np.log1p(np.abs(spectrum)), cmap="gray")
        axes[2].imshow(mask, cmap="gray", vmin=0, vmax=1)
        axes[3].imshow(output, cmap="gray")
        for axis, title in zip(axes, ["Input", "Log spectrum", "Mask", "Signed output"]):
            axis.set_title(title); axis.axis("off")
        fig.suptitle(f"{kind}: radius {radius} frequency bins")
        fig.tight_layout()
finish(__file__)
