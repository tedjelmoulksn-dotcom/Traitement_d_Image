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

The available evidence is organised as method captures, processed-image examples and working reports. Use the code screenshots to follow the operations and the error plots to compare their effects; executable reconstruction requires transcribing the method into a chosen environment.

## Reviewing the material

```bash
git clone https://github.com/tedjelmoulksn-dotcom/Traitement_d_Image.git
cd Traitement_d_Image
```

Start with the quantisation module README, inspect the corresponding figures, then read the filtering documents. Reimplementation should record image provenance, numeric range, colour conversion, boundary treatment and metric definitions.

## Reproducibility

A meaningful image comparison fixes the input, intensity range, channel treatment and boundary rules before changing an algorithm parameter. Quantisation error and spatial reduction should be evaluated separately so that PSNR reflects the operation being studied.

A reproducible continuation stores the executable method, input provenance, dependencies and parameter settings beside each comparison figure.

## Licence

No project-wide licence has been defined. Existing reports and images retain their original attribution.
