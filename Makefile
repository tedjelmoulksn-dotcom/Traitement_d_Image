PYTHON ?= python

.PHONY: test demos
test:
	$(PYTHON) -m unittest discover -s tests -v

demos:
	$(PYTHON) -m labs.sampling_quantisation.src.quantisation
	$(PYTHON) -m labs.tp1_image_analysis.src.composed_kernels
	$(PYTHON) -m labs.tp1_image_analysis.src.contrast_basic
	$(PYTHON) -m labs.tp1_image_analysis.src.contrast_equalisation
	$(PYTHON) -m labs.tp1_image_analysis.src.cross_mask_dtft
	$(PYTHON) -m labs.tp1_image_analysis.src.cross_mask_fft
	$(PYTHON) -m labs.tp1_image_analysis.src.diagonal_mask_response
	$(PYTHON) -m labs.tp1_image_analysis.src.edge_operators
	$(PYTHON) -m labs.tp1_image_analysis.src.laplacian_response
	$(PYTHON) -m labs.tp1_image_analysis.src.sobel_thresholds
	$(PYTHON) -m labs.tp2_filtering.src.frequency_filtering
	$(PYTHON) -m labs.tp2_filtering.src.smoothing_filters
	$(PYTHON) -m labs.tp2_filtering.src.spatial_operator_comparison
