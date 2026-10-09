# Image Sampling and Quantisation Study

An archived study of spatial reduction, grey-level quantisation and image distortion, preserved through figures and code screenshots.

## Available figures

| Location | Content |
|---|---|
| [`assets/code_echantillonnage.png`](assets/code_echantillonnage.png) | Sampling code capture |
| [`assets/code_quantification.png`](assets/code_quantification.png) | Quantisation code capture |
| [`assets/code_eqm_psnr.png`](assets/code_eqm_psnr.png) | MSE/PSNR code capture |
| [`assets/lenna_niveaux_de_quantification.png`](assets/lenna_niveaux_de_quantification.png) | Quantisation comparison |
| [`assets/lenna_reduite_2_fois.png`](assets/lenna_reduite_2_fois.png) | Spatial reduction |
| [`assets/lenna_bruitee.png`](assets/lenna_bruitee.png) | Noisy image example |
| [All figures](assets/) | Additional code and error plots |

## Metrics

For aligned images, MSE is the average squared pixel difference. PSNR is `10*log10(MAX^2/MSE)`, where `MAX` must match the intensity representation. For unsigned 8-bit intensity data, `MAX = 255`; normalised floating-point images require a different peak convention.

Compute differences in a suitable numeric type to avoid unsigned subtraction artifacts.

## Interpretation

Fewer intensity levels generally increase quantisation distortion. Spatial downsampling is a separate operation and should include an explicit treatment of aliasing. Compare images using the same size, intensity scale and colour representation.

## Archive status

Only screenshots and result figures are currently included. There are no executable scripts or source archive, so the module is not directly runnable. Reproduction requires transcribing or reimplementing the method and documenting input provenance and parameters.

No new PSNR/MSE values were computed for this README update.

## Licence

No project-wide licence has been defined. Original images and reports retain their own attribution.
