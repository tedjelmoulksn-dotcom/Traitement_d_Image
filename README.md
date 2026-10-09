# Image Processing Laboratory

Python experiments in image representation, contrast enhancement, edge detection, spatial convolution, Fourier filtering and quantisation. The repository brings together the Instrumentation 2 practical work by **Tedj El Moulk Sinacer and Dahmoun** (2024–2025), with the reports, recovered scripts, shared input images and experimental figures organised by topic.

![Fourier-domain filtering experiment](labs/tp2_filtering/assets/frequency/filtering_overview.png)

## Explore the experiments

| Laboratory | Technical focus | Starting point |
| --- | --- | --- |
| TP1 — Image analysis | Pixel arrays and colour spaces in the report; executable contrast, histogram equalisation, CLAHE, gradient/Laplacian and kernel-response experiments | [TP1 guide](labs/tp1_image_analysis/README.md) |
| TP2 — Spatial and frequency filtering | Convolution versus correlation, boundary handling, smoothing operators, centred spectra and circular low/high-pass masks | [TP2 guide](labs/tp2_filtering/README.md) |
| TP3 — Edge detection | Sobel, Prewitt, Roberts and Laplacian captures; shared executable derivative experiments | [TP3 guide](labs/tp3_edge_detection/README.md) |
| Sampling and quantisation | Archived resampling experiments; runnable uniform quantisation with MSE and PSNR | [Quantisation guide](labs/sampling_quantisation/README.md) |

## Run locally

Use Python 3.11 or newer. Run commands from the repository root.

```bash
git clone https://github.com/tedjelmoulksn-dotcom/Traitement_d_Image.git
cd Traitement_d_Image
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python -m labs.tp2_filtering.src.frequency_filtering
python -m labs.sampling_quantisation.src.quantisation
```

Scripts save PNG figures under `outputs/<laboratory>/<script>/` without opening windows. Add `--show` to display plots on a machine with a graphical session, or `--output-dir /path/to/results` to select another destination. `make demos` executes all 13 experiments; `make test` runs the numerical checks.

## Repository layout

- `labs/`: four laboratory guides, executable scripts, original reports and archived figures.
- `data/input/`: six shared images, stored once and resolved independently of the shell's working directory by the runtime helper.
- `image_lab/`: shared plotting, metric, quantisation and Fourier-mask functions.
- `tests/`: numerical invariants for quantisation, unsigned arithmetic, FFT reconstruction and cross-library convolution equivalence.
- [Archive map](docs/ARCHIVE_MAP.md): source filenames, destination paths and the distinction between recovered code and reconstructed implementations.

## Additional evidence from `cle`

A content-hash comparison of 92 files in the image-processing folder identified 38 additional captures: 9 image-representation figures, 12 contrast/equalisation captures, 4 TP3 derivative figures, 11 sampling/quantisation captures and 2 smoothing-filter captures. Existing images and the TP2 archive were consolidated rather than copied again. Four regression/Iris-classification scripts found under `diagnostic` concern data analysis and are listed separately in the [Drive comparison](docs/CLE_IMAGE_REVIEW.md).

## Numerical conventions

Image intensity, data type and boundary conditions are part of the experiment. Signed filter responses use floating-point arrays; OpenCV and SciPy convolution comparisons use the same reflected boundaries and kernel orientation. Fourier plots use `log1p(abs(spectrum))`; masking acts on the complex spectrum before inverse transformation. Quantisation uses floor-bin reconstruction, with errors calculated after floating-point conversion.

The 11 recovered scripts retain their original author metadata. The Fourier-filtering and quantisation entry points were reconstructed from the supplied reports and code screenshots; the archive map records their provenance. Original reports and screenshots remain unchanged, including their French text. The English guides describe the runnable implementation and make its conventions explicit.

## Validation

The four numerical tests and all 13 script entry points were executed successfully with the versions in `requirements.txt`. These checks establish reproducibility of the software experiments; the original report figures remain historical laboratory results.
