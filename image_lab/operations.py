"""Explicit numeric conventions for quantisation and frequency filtering."""
import numpy as np

def quantize_u8(image, levels):
    if image.dtype != np.uint8:
        raise ValueError("Quantisation expects unsigned 8-bit intensities")
    if not isinstance(levels, (int, np.integer)) or levels < 2 or levels > 256 or 256 % levels:
        raise ValueError("Levels must be an integer divisor of 256, between 2 and 256")
    step = 256 // levels
    return (image // step) * step

def mse_psnr(reference, result, peak=255.0):
    if reference.shape != result.shape or not reference.size:
        raise ValueError("Images must have identical, nonempty shapes")
    if not np.isfinite(peak) or peak <= 0:
        raise ValueError("Peak intensity must be finite and positive")
    error = reference.astype(np.float64) - result.astype(np.float64)
    if not np.isfinite(error).all():
        raise ValueError("Image values must be finite")
    mse = float(np.mean(error * error))
    psnr = float("inf") if mse == 0 else float(10 * np.log10(peak * peak / mse))
    return mse, psnr

def circular_mask(shape, radius, highpass=False):
    if len(shape) != 2 or min(shape) <= 0 or not np.isfinite(radius) or radius < 0:
        raise ValueError("A positive 2-D shape and finite nonnegative radius are required")
    rows, cols = np.ogrid[:shape[0], :shape[1]]
    inside = (rows - shape[0]//2)**2 + (cols - shape[1]//2)**2 <= radius**2
    return ~inside if highpass else inside

def frequency_filter(image, radius, highpass=False):
    if image.ndim != 2 or not image.size or not np.isfinite(image).all():
        raise ValueError("Expected a finite, nonempty grayscale image")
    spectrum = np.fft.fftshift(np.fft.fft2(image.astype(np.float64)))
    mask = circular_mask(image.shape, radius, highpass)
    restored = np.fft.ifft2(np.fft.ifftshift(spectrum * mask))
    return restored.real, spectrum, mask
