# Image Processing Laboratory

Python experiments exploring image representation, intensity transforms, spatial and frequency filtering, and edge detection. Shared functions are separated from laboratory entry points, datasets and reports.

## Laboratory guide

| Folder | Topics |
| --- | --- |
| [Sampling and quantisation](labs/sampling_quantisation/) | Spatial sampling and intensity quantisation |
| [TP1: image analysis](labs/tp1_image_analysis/) | Contrast, histogram equalisation, kernels and Fourier analysis |
| [TP2: filtering](labs/tp2_filtering/) | Smoothing, spatial operators and frequency-domain filtering |
| [TP3: edge detection](labs/tp3_edge_detection/) | Available experiment captures and guide |

[image_lab](image_lab/) contains reusable operations and runtime support. [data/input](data/input/) holds the demonstration images; laboratory folders contain their reports and results. [archive](archive/) preserves original code variants and source archives.

## Run

Install the Python dependencies from the repository root:

```sh
python -m pip install -r requirements.txt
python -m labs.tp2_filtering.src.frequency_filtering
```

Module execution keeps shared imports and relative resource paths consistent. A graphical environment is needed for interactive figure windows.

Use `make demos` for the configured examples and `make test` for the shared-operation tests. These checks cover the implemented Python functions, not the correctness of every historical report or capture.

TP3 currently contains supporting material rather than a complete runnable edge-detection lab. The distinction is documented in its guide.
