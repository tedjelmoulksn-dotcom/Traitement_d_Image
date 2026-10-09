# Sampling and Quantisation

Explore the distinction between spatial sampling and intensity quantisation, using the archived Lenna experiments and a reproducible quantisation script.

![Archived quantisation levels](assets/quantisation_levels.png)

## Run uniform quantisation

```bash
python -m labs.sampling_quantisation.src.quantisation
```

The script uses the shared 8-bit `lenna512.bmp` input and evaluates **128, 64, 32, 16, 8 and 2 levels**. It exports a visual comparison and MSE/PSNR curves to `outputs/sampling_quantisation/quantisation/`.

For `L` levels, the bin width is `Δ = 256 / L` and the reconstruction is `Q(x) = floor(x / Δ) × Δ`. This matches the floor-bin operation shown in the archived code screenshot. It is not nearest-bin or midpoint reconstruction: quantisation errors are correspondingly one-sided. The implementation accepts integer level counts that divide 256, from 2 to 256.

## Error metrics

For images of identical shape, mean squared error is the mean of `(original - reconstruction)²`. Subtraction is performed in floating point, avoiding unsigned wraparound. PSNR is `10 log10(255² / MSE)` for the 8-bit intensity range, and is infinite when MSE is zero.

The error curves characterise this input and this reconstruction rule. PSNR measures pixelwise distortion; it does not independently measure perceptual image quality.

## Spatial sampling

The archived captures compare sample reduction, image resizing and local-mean downscaling. These alter spatial resolution, whereas quantisation alters the number of available intensity levels. Direct subsampling may alias high-frequency detail; averaging before reduction and interpolation during resizing change the resulting pixel values.

The sampling code is preserved in [screenshots](assets/sampling_code.png) and [resizing captures](assets/resizing_code.png). The runnable quantisation script was reconstructed from the original quantisation and metric screenshots; its provenance is recorded in the [archive map](../../docs/ARCHIVE_MAP.md).

## Evidence

`assets/` groups the original quantisation code, MSE/PSNR plots, noisy-image capture and recovered resampling figures. Archived screenshots are historical evidence; newly generated figures stay in `outputs/`.
