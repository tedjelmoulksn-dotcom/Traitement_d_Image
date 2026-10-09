# Image Processing — Quantisation and Filtering Studies

Academic image-processing material covering sampling, grey-level quantisation, distortion metrics and spatial/frequency-domain filtering.

## Repository map

| Module | Available material |
|---|---|
| [Sampling and quantisation](Traitement_Image_Quantification/) | Code screenshots, reconstructed-image figures and error/PSNR plots |
| [Spatial and frequency filtering](filtrage_spatial_frequentiel/) | PDF exercise material and working DOCX reports |

## Technical focus

The quantisation study relates the number of representable intensity levels to image distortion. Mean squared error (MSE) measures pixel-domain error, while peak signal-to-noise ratio (PSNR) expresses that error relative to the chosen peak intensity.

The filtering reports provide the separate coursework on local spatial operators and frequency-domain treatment. Their assumptions and results should be read from the reports rather than inferred from repository names.

## Available evidence

The archive contains figures and documents, not a complete runnable image-processing codebase. Code screenshots preserve implementation details but are not a substitute for source files or a reproducible environment. No source archive is currently present.

## Reviewing the material

```bash
git clone https://github.com/tedjelmoulksn-dotcom/Traitement_d_Image.git
cd Traitement_d_Image
```

Start with the quantisation module README, inspect the corresponding figures, then read the filtering documents. Reimplementation should record image provenance, numeric range, colour conversion, boundary treatment and metric definitions.

## Reproducibility

No new MSE/PSNR values or filter comparisons were computed during this README update. A reproducible continuation should add scripts, input licensing information, dependencies and exact parameter settings.

## Licence

No project-wide licence has been defined. Existing reports and images retain their original attribution.
