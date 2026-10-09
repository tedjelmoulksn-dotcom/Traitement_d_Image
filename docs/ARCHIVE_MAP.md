# Archive Map and Implementation Notes

## Sources

The repository consolidates the supplied `traitement_dimages_tp_1.rar` and `tp2.rar` Drive archives. Their folder names did not reliably indicate laboratory content: the TP1 archive also contained `partie1_tp2.py` and smoothing code for TP2. Files are now grouped by experiment rather than by archive label.

The TP1 PDF, complete TP2 DOCX and spatial-exercise DOCX were already present in GitHub and have been moved without changing their bytes. Likewise, the existing nine quantisation screenshots were retained. The earlier mixed folders are replaced by `labs/`.

## Recovered executable code

The following 11 source files were recovered from the supplied archives. The source author metadata is preserved wherever present; account labels such as `greg7` are retained as source metadata rather than interpreted as a verified person's identity. Paths, output handling and the numerical corrections listed below were adapted for reproducible execution.

| Archive filename | Repository module | Original Git blob SHA-1 |
| --- | --- | --- |
| `partie1_tp2.py` | [`spatial_operator_comparison`](../labs/tp2_filtering/src/spatial_operator_comparison.py) | `e6cbe59060bcf585d8eb80c26afa4eb07d1f37df` |
| `sanstitre8.py` | [`smoothing_filters`](../labs/tp2_filtering/src/smoothing_filters.py) | `6b5af7821430eb9c7da4dcb4402808b3cd0c89da` |
| `sanstitre9.py` | [`contrast_basic`](../labs/tp1_image_analysis/src/contrast_basic.py) | `ab182d53a71bda2b22ecd0c228c0f2c95cde59f3` |
| `sanstitre10.py` | [`contrast_equalisation`](../labs/tp1_image_analysis/src/contrast_equalisation.py) | `144cc857828e940184e47562dd38eb9ba3727074` |
| `sanstitre11.py` | [`edge_operators`](../labs/tp1_image_analysis/src/edge_operators.py) | `eca399a6e7f541743a0c61644cbb6c867b4f0404` |
| `sanstitre12.py` | [`sobel_thresholds`](../labs/tp1_image_analysis/src/sobel_thresholds.py) | `1e3816a67e54d361a2c9d88c208e41789c6dce76` |
| `sanstitre13.py` | [`laplacian_response`](../labs/tp1_image_analysis/src/laplacian_response.py) | `95ebe3a7c9cca12e1da8d8d9a374f98a15565e99` |
| `sanstitre14.py` | [`cross_mask_dtft`](../labs/tp1_image_analysis/src/cross_mask_dtft.py) | `32b0555d3816afd2a897670f8f12288256dfab2f` |
| `sanstitre15.py` | [`cross_mask_fft`](../labs/tp1_image_analysis/src/cross_mask_fft.py) | `9d0f2d6e109208428bb831c4721e9fe4fea65978` |
| `sanstitre16.py` | [`composed_kernels`](../labs/tp1_image_analysis/src/composed_kernels.py) | `53ccaceeffc4cdcfb97e145d1535b327f6a9e356` |
| `sanstitre17.py` | [`diagonal_mask_response`](../labs/tp1_image_analysis/src/diagonal_mask_response.py) | `30f78b6f78cec5b104b215fea2734018c74b2215` |

## Reconstructed entry points

- [Frequency filtering](../labs/tp2_filtering/src/frequency_filtering.py): a new implementation based on the TP2 report and recovered FFT, inverse-FFT and circular-mask screenshots. It uses NumPy's complex FFT and inverse normalisation, and saves both low-pass and high-pass experiments.
- [Quantisation](../labs/sampling_quantisation/src/quantisation.py): a new implementation based on the existing quantisation and MSE/PSNR screenshots. It preserves the floor-bin reconstruction rule and supplied level counts.

These are reconstructed runnable implementations, not source files recovered verbatim from the archives. Shared functions in `image_lab/` and numerical tests were added alongside them.

## Execution and numerical corrections

- Resolve image paths from one shared input directory; correct filename spelling and case for Linux.
- Remove obsolete `scipy.misc` and unused imports; export figures consistently with an optional interactive mode.
- Convert scikit-image RGB inputs with `COLOR_RGB2GRAY` in the equalisation experiment.
- Calculate Michelson extrema in floating point to prevent unsigned addition/subtraction overflow.
- Compare convolution on matching float64 inputs, flip the OpenCV correlation kernel, and align OpenCV `BORDER_REFLECT` with SciPy `boundary='symm'`.
- Keep signed Laplacian output in float64.
- Use cycles/pixel on the DTFT grid and shifted FFT-bin coordinates for the diagonal mask plot.
- Describe the supplied diagonal mask as a diagonal derivative mask, rather than identifying it as a canonical horizontal Prewitt mask.

The original reports and captures remain unchanged. Reproduction follows the conventions of the current code; legacy screenshots can therefore differ from newly generated plots.

## Existing file moves

| Previous path | Current path |
| --- | --- |
| `Traitement_Image_Quantification/.gitignore` | `labs/sampling_quantisation/.gitignore` |
| `Traitement_Image_Quantification/assets/code_echantillonnage.png` | `labs/sampling_quantisation/assets/sampling_code_original.png` |
| `Traitement_Image_Quantification/assets/code_eqm_psnr.png` | `labs/sampling_quantisation/assets/mse_psnr_code.png` |
| `Traitement_Image_Quantification/assets/code_quantification.png` | `labs/sampling_quantisation/assets/quantisation_code.png` |
| `Traitement_Image_Quantification/assets/code_reduction_image.png` | `labs/sampling_quantisation/assets/image_reduction_code.png` |
| `Traitement_Image_Quantification/assets/eqm_fonction_pas_quantification.png` | `labs/sampling_quantisation/assets/mse_by_quantisation_step.png` |
| `Traitement_Image_Quantification/assets/lenna_bruitee.png` | `labs/sampling_quantisation/assets/noisy_lenna.png` |
| `Traitement_Image_Quantification/assets/lenna_niveaux_de_quantification.png` | `labs/sampling_quantisation/assets/quantisation_levels.png` |
| `Traitement_Image_Quantification/assets/lenna_reduite_2_fois.png` | `labs/sampling_quantisation/assets/half_size_lenna.png` |
| `Traitement_Image_Quantification/assets/psnr_fonction_pas_quantification.png` | `labs/sampling_quantisation/assets/psnr_by_quantisation_step.png` |
| `filtrage_spatial_frequentiel/tp1_analyse_images.pdf` | `labs/tp1_image_analysis/docs/report_tp1.pdf` |
| `filtrage_spatial_frequentiel/tp1_exercice2_filtrage_spatial.docx` | `labs/tp2_filtering/docs/spatial_filtering_draft.docx` |
| `filtrage_spatial_frequentiel/tp2_filtrage_frequentiel.docx` | `labs/tp2_filtering/docs/report_tp2.docx` |

## Recovered input data and captures

The six shared inputs appear in both archives. Exact byte duplicates were consolidated by Git blob SHA-1, including `sanscranetest100bruit9%.png`, which matches `crane.png`. `partie1_tp2.py` also appears identically in both archives and is imported once. No noise percentage is inferred from an input filename.

| Archive member | Destination | Original Git blob SHA-1 |
| --- | --- | --- |
| `tp1.rar: crane.png` | `data/input/crane.png` | `426c88f47af764b76c29dbfe42ff92854d70beee` |
| `tp1.rar: flowers.tif` | `data/input/flowers.tif` | `5bd7d6ff3149f59b285c7a9c3f2ab5334fe12f8e` |
| `tp1.rar: lenna512.bmp` | `data/input/lenna512.bmp` | `bcffc810c8bb08984b54f13e6ab208add47bf344` |
| `tp1.rar: peppers2.bmp` | `data/input/peppers2.bmp` | `94698da26f6801f7572bf1573b74531cba75f04b` |
| `tp1.rar: poupee.tif` | `data/input/poupee.tif` | `a598db0bc13a639b51620cf388435906873d5454` |
| `tp1.rar: 200px-Blobs-blur.png` | `data/input/200px-Blobs-blur.png` | `ee4766a263129e119000e5a51e3b43481ef7c27c` |
| `tp1.rar: carreau noir into carreaux blanc.PNG` | `labs/tp1_image_analysis/assets/pixel_patch.png` | `182a32b34a9699530d82d6aa740385b743223777` |
| `tp1.rar: code carreau noir into carreau blanc.PNG` | `labs/tp1_image_analysis/assets/pixel_patch_code.png` | `2dcae1b415a67ebe9e3fc2794815275a9ec8f0b4` |
| `tp1.rar: exo3_imagette.PNG` | `labs/tp1_image_analysis/assets/synthetic_pattern.png` | `441eec947f506280982ba54c25e1dc8dbc98d0f5` |
| `tp1.rar: Figure 2024-10-11 183046.png` | `labs/tp1_image_analysis/assets/experiment_2024_10_11.png` | `7e3b56912a0e30e76ebe607a424d93df634001a8` |
| `tp1.rar: figure1_damier.PNG` | `labs/tp1_image_analysis/assets/checkerboard.png` | `d61913dacd30e678eb2e75439da028db8fae7ffd` |
| `tp1.rar: imagette en couleur.PNG` | `labs/tp1_image_analysis/assets/colour_patch.png` | `526a391f8df73661e97de2c7a5c0c1b7300f14da` |
| `tp1.rar: rep_frequ de M.png` | `labs/tp1_image_analysis/assets/kernel_response.png` | `a1602b5291fa8d940092d6fc8a9c8af9593e5423` |
| `tp1.rar: show_damier.PNG` | `labs/tp1_image_analysis/assets/checkerboard_display.png` | `60d5bbe44b3964d555cf3f31b70d47e4d3c32a6f` |
| `tp1.rar: taillememeodimagette.PNG` | `labs/tp1_image_analysis/assets/colour_patch_memory.png` | `91d4b54f61a20634ac82bc2c3bfc8cabbca54aff` |
| `tp1.rar: taillememo.PNG` | `labs/tp1_image_analysis/assets/array_memory.png` | `d2fadbc0be8e54540ebb6d6b758281f59a32265c` |
| `tp1.rar: calcul de la taille memo dud amier.PNG` | `labs/tp1_image_analysis/assets/checkerboard_memory_calculation.png` | `d48f5f482569d9faa307d3f6f330a6c2a030c57c` |
| `tp2.rar: tp2/0_lire flower.PNG` | `labs/tp2_filtering/assets/frequency/input_loading.png` | `d6830d03a03b19d956f81d2aecb51cd9782447db` |
| `tp2.rar: tp2/1_code de tf.PNG` | `labs/tp2_filtering/assets/frequency/fft_code.png` | `e379dc6e83061aba6a450653ddda38fa8000c1be` |
| `tp2.rar: tp2/2_resulatats de tf.PNG` | `labs/tp2_filtering/assets/frequency/fft_result.png` | `b98b349c5f50380edea30c7a56e53a9a5842a70e` |
| `tp2.rar: tp2/3_code idft.PNG` | `labs/tp2_filtering/assets/frequency/inverse_fft_code.png` | `28659aef86094f4919268db808420ffb72de1fd8` |
| `tp2.rar: tp2/4_taille de chaque variable.PNG` | `labs/tp2_filtering/assets/frequency/array_shapes.png` | `6dd208d75316ddb6f1e784fc5d36e8acd8df37da` |
| `tp2.rar: tp2/5_code calcul et affichage de lamplitude de specte.PNG` | `labs/tp2_filtering/assets/frequency/spectrum_code.png` | `1e5ec96b6801a11e3133047ce7df8c39bd1fd2a9` |
| `tp2.rar: tp2/6_affichage du spectre de lamplitude.PNG` | `labs/tp2_filtering/assets/frequency/spectrum_display.png` | `ff2fe4a115b3e357bbc7d2c7924a30329ea9ff6d` |
| `tp2.rar: tp2/7_code masque circulaire.PNG` | `labs/tp2_filtering/assets/frequency/circular_mask_code.png` | `8c37ca0d7e5292d34b7eb2ed6d1297906cbf13f2` |
| `tp2.rar: tp2/8_affichage du masque a r=100.PNG` | `labs/tp2_filtering/assets/frequency/mask_radius_100.png` | `46e1591a9ff87b74e009c7ed29c144e06c5cf856` |
| `tp2.rar: tp2/9_affichage de limage originbal,lespectre,lemadque,limage finale.PNG` | `labs/tp2_filtering/assets/frequency/filtering_overview.png` | `39207df7c765ba132979f788dd4b29c701fc356a` |
| `tp2.rar: tp2/10_code pour afficher tout dans une seule figure.PNG` | `labs/tp2_filtering/assets/frequency/combined_figure_code.png` | `5588422e47a3ac3d9b35a91793faa88e0e004386` |
| `tp2.rar: tp2/11_masque a un rayon de 10 laisse passe plus de chose.PNG` | `labs/tp2_filtering/assets/frequency/mask_radius_10.png` | `eb2bb8a08de95bbe4725637d10dfa6fee0c439a0` |
| `tp2.rar: tp2/12_masque a un rayon de 200.PNG` | `labs/tp2_filtering/assets/frequency/mask_radius_200.png` | `5f1dacb3b073bcaa62f845243ceabaed30b14c8b` |
| `tp2.rar: tp2/12_limage quand maskarea=1.PNG` | `labs/tp2_filtering/assets/frequency/low_pass_result.png` | `50c62928e8e5814873b47a98eafec863d6a68032` |
| `tp2.rar: tp2/code_echantillonage_reduction.PNG` | `labs/sampling_quantisation/assets/sampling_code.png` | `716b8aceb8e4438a44a3648af5c2ee8c16501cea` |
| `tp2.rar: tp2/code_resize.PNG` | `labs/sampling_quantisation/assets/resizing_code.png` | `1c079f8e67351e87779f0e8cef0684891c5db5ec` |
| `tp2.rar: tp2/dim de lenna resized.PNG` | `labs/sampling_quantisation/assets/resized_shape.png` | `7ded1e756e8efd2c362a695d57ef64ea28812d9e` |
| `tp2.rar: tp2/lenna reduite par un facteur de 1 par 4.PNG` | `labs/sampling_quantisation/assets/quarter_size_result.png` | `80e5231a7a281be6c115559b5afd578bf1586bc3` |
| `tp2.rar: tp2/lenna resized.PNG` | `labs/sampling_quantisation/assets/resized_result.png` | `998b17440d765029842dfcc1b87226621dcf1760` |
| `tp2.rar: tp2/exercice 2/1_codefiltre.PNG` | `labs/tp2_filtering/assets/spatial/kernel_code.png` | `aa02b131def4d53e66d8d0d9d4414f27cce4c9d4` |
| `tp2.rar: tp2/exercice 2/2_image obtenue apres convolution.PNG` | `labs/tp2_filtering/assets/spatial/convolution_result.png` | `b0f76cbf93fda61556e4b833789718670abacd77` |
| `tp2.rar: tp2/exercice 2/3_code avec le deuxieme noyau.PNG` | `labs/tp2_filtering/assets/spatial/second_kernel_code.png` | `a721ad25ff6332691a26d734eec4f5d492d398bb` |
| `tp2.rar: tp2/exercice 2/4_image avec le deuxieme noyau.PNG` | `labs/tp2_filtering/assets/spatial/second_kernel_result.png` | `45e7c774b005c261c46b62c412ea83531aea84ed` |
| `tp2.rar: tp2/exercice 2/5_image en filtre 5x5.PNG` | `labs/tp2_filtering/assets/spatial/filter_5x5.png` | `828f0bc749fab55cdd496e616cfdf16b913a61b0` |
| `tp2.rar: tp2/exercice 2/6_image en filtre 7x7.PNG` | `labs/tp2_filtering/assets/spatial/filter_7x7.png` | `fa21554f656af921c294641355639f32ede74ac2` |
| `tp2.rar: tp2/exercice 2/7_image en filtre 9x9.PNG` | `labs/tp2_filtering/assets/spatial/filter_9x9.png` | `e10c240842a567a0bb2c0447b6088dbab515bb76` |
| `tp2.rar: tp2/exercice 2/8_code pour la question 6.PNG` | `labs/tp2_filtering/assets/spatial/comparison_code.png` | `803d99e5f655fe7c9e21d14d429e0ca5ae697f2e` |
| `tp2.rar: tp2/exercice 2/9_image avec deux noyau pour les deux methode.PNG` | `labs/tp2_filtering/assets/spatial/operator_comparison.png` | `0c2063b5830bc766498324d423717e4988f82251` |

## Excluded material

The `ipython.html` console export is omitted: it duplicates the script session and contains machine-specific paths. The similarly named Drive `tp1.odt` and `tp 1.pdf` concern analogue electronics, and `images tp 2.rar` contains control-system captures; these belong to other projects and were not imported into the image-processing repository. No IGN or PanoX5 material was changed.
