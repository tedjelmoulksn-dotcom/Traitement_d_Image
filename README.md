# Image Processing Laboratories

Python laboratory collection for image analysis, contrast enhancement, spatial and frequency-domain filtering, edge detection, sampling and quantisation. Shared operations support reproducible demonstrations and unit tests.

## Repository guide

| Location | Contents |
|---|---|
| [labs/](labs/) | Study scripts, reports and figures |
| [image_lab/](image_lab/) | Shared image operations and runtime helpers |
| [data/](data/) | Input images and dataset notes |
| [tests/](tests/) | Image-operation tests |
| [docs/](docs/) | Reports and source mapping |
| [archive/](archive/) | Original script variants and source package |

## Getting started

From the repository root:

```bash
python -m pip install -r requirements.txt
make test
python -m labs.tp2_filtering.src.frequency_filtering
```

Use `make demos` to run the complete demonstration set.

## Project context

Runnable labs are separate from original captures and earlier script variants. The Iris machine-learning exercises are grouped in the data-analysis repository.
