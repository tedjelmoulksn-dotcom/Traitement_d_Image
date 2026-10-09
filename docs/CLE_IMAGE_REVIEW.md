# Drive `cle` — Image Processing Comparison

## Scope and result

Source: the supplied [cle folder](https://drive.google.com/drive/folders/15qml8mkLEVRrOhONMAbYb6ts0XzfO80L), specifically its `traitement d'image` subtree, including the nested `tp2/partie C` and `tp2/exercice 2` folders. File bytes were compared using Git blob SHA-1 rather than filenames alone.

92 files were examined: **38 additional captures**, **48 files already present byte-for-byte**, **one original Python script already represented by its adapted runnable version**, **one byte-identical TP2 archive**, and **four scripts belonging to data analysis**. No additional PDF or Word report, and no additional image-processing Python source, was found in this subtree.

## Additions

| Source group | New captures | Repository destination |
| --- | --- | --- |
| `tp1` | 9 | `labs/tp1_image_analysis/assets/representation/` |
| `tp2/partie C` | 12 | `labs/tp1_image_analysis/assets/contrast/` |
| `tp2/exercice 2` | 2 | `labs/tp2_filtering/assets/spatial/` |
| `tp3` | 4 | `labs/tp3_edge_detection/assets/` |
| `photo_tp` | 11 | `labs/sampling_quantisation/assets/evidence/` |

Existing captures and input images were not duplicated. `photo_tp_prime` contained only already integrated resampling captures. The `tp2.rar` file is identical to the previously imported archive.

## Topic mismatch

The Drive `diagnostic` folder contains `tp2.py`, `exo1.py`, `exo2.py` and `exo3.py`. Their content covers synthetic regression, the Iris feature dataset, train/test splitting, k-nearest-neighbour classification and cross-validation. These are data-analysis exercises, not image-processing source files; they were not inserted into this repository.

## Captures and current calculations

All imported PNG bytes are preserved. Some original console results use unsigned image arithmetic and contain Michelson values outside the valid nonnegative-intensity range. The runnable scripts already calculate extrema in floating point. Historical MSE and PSNR annotations are retained as original session evidence, while the current metric helper performs subtraction and squaring in floating point. Fresh outputs and archived screenshots remain distinct.

## File-level comparison

| Drive relative path | Status / repository location | Source Git blob SHA-1 |
| --- | --- | --- |
| `tp3/3_flowers avec filtre et seuil.png` | `labs/tp3_edge_detection/assets/sobel_threshold_comparison.png` | `126ca46b54fad98cedc79acb63cc06223728d5cc` |
| `tp3/2_lenna apres noyau.png` | `labs/tp3_edge_detection/assets/lenna_edge_operators.png` | `1c47ca0e6aa0c0428dc2f56447982bf98a64e099` |
| `tp3/1_flowers apres noyau.png` | `labs/tp3_edge_detection/assets/flowers_edge_operators.png` | `207ba0b91c204da2b4bc052f10f171bdf8534339` |
| `tp3/0_reponsefrqu de chaque noyaux.png` | `labs/tp3_edge_detection/assets/frequency_response_comparison.png` | `91cb887f1a25f2b8a5c8a6ea34ba4904017a9d06` |
| `tp2/partie1_tp2.py` | `Adapted as labs/tp2_filtering/src/spatial_operator_comparison.py` | `e6cbe59060bcf585d8eb80c26afa4eb07d1f37df` |
| `tp2/12_limage quand maskarea=1.PNG` | `Already present: labs/tp2_filtering/assets/frequency/low_pass_result.png` | `50c62928e8e5814873b47a98eafec863d6a68032` |
| `tp2/12_masque a un rayon de 200.PNG` | `Already present: labs/tp2_filtering/assets/frequency/mask_radius_200.png` | `5f1dacb3b073bcaa62f845243ceabaed30b14c8b` |
| `tp2/11_masque a un rayon de 10 laisse passe plus de chose.PNG` | `Already present: labs/tp2_filtering/assets/frequency/mask_radius_10.png` | `eb2bb8a08de95bbe4725637d10dfa6fee0c439a0` |
| `tp2/10_code pour afficher tout dans une seule figure.PNG` | `Already present: labs/tp2_filtering/assets/frequency/combined_figure_code.png` | `5588422e47a3ac3d9b35a91793faa88e0e004386` |
| `tp2/9_affichage de limage originbal,lespectre,lemadque,limage finale.PNG` | `Already present: labs/tp2_filtering/assets/frequency/filtering_overview.png` | `39207df7c765ba132979f788dd4b29c701fc356a` |
| `tp2/8_affichage du masque a r=100.PNG` | `Already present: labs/tp2_filtering/assets/frequency/mask_radius_100.png` | `46e1591a9ff87b74e009c7ed29c144e06c5cf856` |
| `tp2/7_code masque circulaire.PNG` | `Already present: labs/tp2_filtering/assets/frequency/circular_mask_code.png` | `8c37ca0d7e5292d34b7eb2ed6d1297906cbf13f2` |
| `tp2/6_affichage du spectre de lamplitude.PNG` | `Already present: labs/tp2_filtering/assets/frequency/spectrum_display.png` | `ff2fe4a115b3e357bbc7d2c7924a30329ea9ff6d` |
| `tp2/5_code calcul et affichage de lamplitude de specte.PNG` | `Already present: labs/tp2_filtering/assets/frequency/spectrum_code.png` | `1e5ec96b6801a11e3133047ce7df8c39bd1fd2a9` |
| `tp2/4_taille de chaque variable.PNG` | `Already present: labs/tp2_filtering/assets/frequency/array_shapes.png` | `6dd208d75316ddb6f1e784fc5d36e8acd8df37da` |
| `tp2/3_code idft.PNG` | `Already present: labs/tp2_filtering/assets/frequency/inverse_fft_code.png` | `28659aef86094f4919268db808420ffb72de1fd8` |
| `tp2/1_code de tf.PNG` | `Already present: labs/tp2_filtering/assets/frequency/fft_code.png` | `e379dc6e83061aba6a450653ddda38fa8000c1be` |
| `tp2/2_resulatats de tf.PNG` | `Already present: labs/tp2_filtering/assets/frequency/fft_result.png` | `b98b349c5f50380edea30c7a56e53a9a5842a70e` |
| `tp2/0_lire flower.PNG` | `Already present: labs/tp2_filtering/assets/frequency/input_loading.png` | `d6830d03a03b19d956f81d2aecb51cd9782447db` |
| `tp2/dim de lenna resized.PNG` | `Already present: labs/sampling_quantisation/assets/resized_shape.png` | `7ded1e756e8efd2c362a695d57ef64ea28812d9e` |
| `tp2/lenna resized.PNG` | `Already present: labs/sampling_quantisation/assets/resized_result.png` | `998b17440d765029842dfcc1b87226621dcf1760` |
| `tp2/code_resize.PNG` | `Already present: labs/sampling_quantisation/assets/resizing_code.png` | `1c079f8e67351e87779f0e8cef0684891c5db5ec` |
| `tp2/lenna reduite par un facteur de 1 par 4.PNG` | `Already present: labs/sampling_quantisation/assets/quarter_size_result.png` | `80e5231a7a281be6c115559b5afd578bf1586bc3` |
| `tp2/code_echantillonage_reduction.PNG` | `Already present: labs/sampling_quantisation/assets/sampling_code.png` | `716b8aceb8e4438a44a3648af5c2ee8c16501cea` |
| `tp2/sanscranetest100bruit9%.png` | `Already present: data/input/crane.png` | `426c88f47af764b76c29dbfe42ff92854d70beee` |
| `tp2/200px-Blobs-blur.png` | `Already present: data/input/200px-Blobs-blur.png` | `ee4766a263129e119000e5a51e3b43481ef7c27c` |
| `tp2/lenna512.bmp` | `Already present: data/input/lenna512.bmp` | `bcffc810c8bb08984b54f13e6ab208add47bf344` |
| `tp2/peppers2.bmp` | `Already present: data/input/peppers2.bmp` | `94698da26f6801f7572bf1573b74531cba75f04b` |
| `tp2/poupee.tif` | `Already present: data/input/poupee.tif` | `a598db0bc13a639b51620cf388435906873d5454` |
| `tp2/flowers.tif` | `Already present: data/input/flowers.tif` | `5bd7d6ff3149f59b285c7a9c3f2ab5334fe12f8e` |
| `tp1/dim_lena.PNG` | `labs/tp1_image_analysis/assets/representation/lenna_shape.png` | `43ee5a45e45c78d98712bd80418c39d2f1585425` |
| `tp1/exo1.C_dim_image_lenna.PNG` | `labs/tp1_image_analysis/assets/representation/lenna_loading_code.png` | `92a6b821bd1d2e9f5a5a3891268a43e635555db2` |
| `tp1/fft pour d=32.PNG` | `labs/tp1_image_analysis/assets/representation/sinusoid_fft_period_32.png` | `84cc675a82ec783fe67d972e47e8426b5e52bf40` |
| `tp1/d=8.PNG` | `labs/tp1_image_analysis/assets/representation/sinusoid_period_8.png` | `848dfb27a8c92eaa94f57d2ff1f0383bff925c32` |
| `tp1/d=10000.PNG` | `labs/tp1_image_analysis/assets/representation/sinusoid_period_10000.png` | `4c1b56b604e23e5b4bbff892b3b1c1b6bd7ec30c` |
| `tp1/d=500.PNG` | `labs/tp1_image_analysis/assets/representation/sinusoid_period_500.png` | `16ed22741554aa7020e050f10683448a44b1bc14` |
| `tp1/code_generation de limùage _exo4_èquestion1.PNG` | `labs/tp1_image_analysis/assets/representation/sinusoid_generation_code.png` | `57539ceb3b9ca41d0a15833328ffc20bae2f15bc` |
| `tp1/2.PNG` | `labs/tp1_image_analysis/assets/representation/hsv_channels.png` | `4b60761f7ba713ef54b749da98a496b1cbb72bd9` |
| `tp1/1.PNG` | `labs/tp1_image_analysis/assets/representation/hsv_conversion_code.png` | `f8cf41ffe2e01cc2157a5e8bded7caf60dadfc29` |
| `photo_tp_prime/dim de lenna resized.PNG` | `Already present: labs/sampling_quantisation/assets/resized_shape.png` | `7ded1e756e8efd2c362a695d57ef64ea28812d9e` |
| `photo_tp_prime/lenna resized.PNG` | `Already present: labs/sampling_quantisation/assets/resized_result.png` | `998b17440d765029842dfcc1b87226621dcf1760` |
| `photo_tp_prime/code_resize.PNG` | `Already present: labs/sampling_quantisation/assets/resizing_code.png` | `1c079f8e67351e87779f0e8cef0684891c5db5ec` |
| `photo_tp_prime/lenna reduite par un facteur de 1 par 4.PNG` | `Already present: labs/sampling_quantisation/assets/quarter_size_result.png` | `80e5231a7a281be6c115559b5afd578bf1586bc3` |
| `photo_tp_prime/code_echantillonage_reduction.PNG` | `Already present: labs/sampling_quantisation/assets/sampling_code.png` | `716b8aceb8e4438a44a3648af5c2ee8c16501cea` |
| `photo_tp/psnr de chacun des bruit.PNG` | `labs/sampling_quantisation/assets/evidence/noise_psnr_console.png` | `921dc91b123f5e221ed346e8818fd5c1638478f7` |
| `photo_tp/lenna bruite.PNG` | `Already present: labs/sampling_quantisation/assets/noisy_lenna.png` | `6dd4cadeb8f8f174ac62913cfe639dc1b36e977e` |
| `photo_tp/leqm en fct de pas.PNG` | `labs/sampling_quantisation/assets/evidence/mse_by_step_legacy.png` | `ddd24afed0fa2715374790d70b23a9c431dd19fe` |
| `photo_tp/psnr en fct de pas de quantif.PNG` | `Already present: labs/sampling_quantisation/assets/psnr_by_quantisation_step.png` | `9b8739a176dc3d5de43296fb8280e1e5d95e169e` |
| `photo_tp/code_pour_eqm en fct de pas de quantif.PNG` | `Already present: labs/sampling_quantisation/assets/mse_psnr_code.png` | `9eb3af59cf5c9c78ce8769c4a367839fe85d482e` |
| `photo_tp/eqm en fct de du pas de quantif.PNG` | `Already present: labs/sampling_quantisation/assets/mse_by_quantisation_step.png` | `dff46a2616fdbff03fc3e57b1265977cc4eb3032` |
| `photo_tp/eqm de chaque nv.PNG` | `labs/sampling_quantisation/assets/evidence/quantisation_mse_console.png` | `b7724e77bc2d70e929217edb68fdae384d0709d7` |
| `photo_tp/lenna , chaque nv de quantif , eqm pour chaque nv de quantif.PNG` | `labs/sampling_quantisation/assets/evidence/quantisation_with_mse.png` | `b39a6b1e81b1ad0fa9292d91c91fb40794974f1b` |
| `photo_tp/calcul de leqm pour chaque nv.PNG` | `labs/sampling_quantisation/assets/evidence/quantisation_mse_plot_code.png` | `cb16398a30f2ba5d6e987e16a9115f9398065805` |
| `photo_tp/lenna en diff niveauy de quatification.PNG` | `Already present: labs/sampling_quantisation/assets/quantisation_levels.png` | `174b88161ba61eae07ab29aa84b805f6238f6b4f` |
| `photo_tp/code quantif en diff niveau.PNG` | `Already present: labs/sampling_quantisation/assets/quantisation_code.png` | `e7c90fd8ab29b5a475dceeff92a7855037504640` |
| `photo_tp/nb de niveau de gris de lenna.PNG` | `labs/sampling_quantisation/assets/evidence/lenna_gray_levels_console.png` | `fb1e0b1d1dae9985c4dda7acffa7fda0f4881a6c` |
| `photo_tp/code pour trouver le nb de gris de lenna.PNG` | `labs/sampling_quantisation/assets/evidence/lenna_gray_levels_code.png` | `16733c30810dfb6c9395e038f7749c5b49e072fb` |
| `photo_tp/dim apres 2 iterzatio n .png` | `labs/sampling_quantisation/assets/evidence/downsampling_two_steps_shape.png` | `0e259053a944fe396f6b3579f415e53563f5d027` |
| `photo_tp/dim apres 5 iterations .png` | `labs/sampling_quantisation/assets/evidence/downsampling_five_steps_shape.png` | `cdefdc7841ba835db184d0cea317a92a55e6e2de` |
| `photo_tp/lenna reduite 5 fois .png` | `labs/sampling_quantisation/assets/evidence/downsampling_five_steps_result.png` | `11be100b3ed1220ddfa12dd33172b17b654c2a72` |
| `photo_tp/lenna reduite 2 fois.png` | `Already present: labs/sampling_quantisation/assets/half_size_lenna.png` | `8dcd9d7cd4045fa46c037ee95a328944b4be1c13` |
| `photo_tp/code pour reduire lenna n fois.png` | `Already present: labs/sampling_quantisation/assets/image_reduction_code.png` | `15fa6ad746ce683ea07d8aed59c2605289204ece` |
| `photo_tp/code_echantillonnage.png` | `Already present: labs/sampling_quantisation/assets/sampling_code_original.png` | `9b334e5f380bcf634306177b58a8df7b76f34a74` |
| `photo_tp/taille_image_echantillonee.png` | `labs/sampling_quantisation/assets/evidence/downsampling_shape.png` | `106023473853a76b7038522f341e87e7d89d2d66` |
| `diagnostic/tp2.py` | `Data analysis; excluded from this repository` | `12080b8e152022bb577acaa49243a6ad060602ba` |
| `diagnostic/exo3.py` | `Data analysis; excluded from this repository` | `43976240b33ce339e0d947413efb3424dca3680d` |
| `diagnostic/exo1.py` | `Data analysis; excluded from this repository` | `09c535efa5d1aff5b45c28ca0a1e539ad13ceff5` |
| `diagnostic/exo2.py` | `Data analysis; excluded from this repository` | `5f1931fca1d9900ef09bb07a0c07923d8472a849` |
| `partie C/12_calcul du contraste en clahe.PNG` | `labs/tp1_image_analysis/assets/contrast/clahe_metrics_console.png` | `c267e76627942360207f2b95e2085bf589201f9d` |
| `partie C/11_image avec clahe.PNG` | `labs/tp1_image_analysis/assets/contrast/clahe_images.png` | `5d025785000f69d335722593641f1e630382dbda` |
| `partie C/10_clahe code.PNG` | `labs/tp1_image_analysis/assets/contrast/clahe_metrics_code.png` | `fa95c5881d4fc4a23c3591096668c561ba85117c` |
| `partie C/9_resultats image egalise.PNG` | `labs/tp1_image_analysis/assets/contrast/equalised_metrics_console.png` | `eaf5628f5ed7e7c74e75e53e4ea57e25e94a3f6e` |
| `partie C/8_images_egalise.PNG` | `labs/tp1_image_analysis/assets/contrast/equalised_images.png` | `f7996ff171d012cadd8dd0a2a7b7361a490bb30e` |
| `partie C/7_code d'egalisation.PNG` | `labs/tp1_image_analysis/assets/contrast/equalised_display_code.png` | `8da3b5683dd189f91341d259281c6fdd6bb660dc` |
| `partie C/6_image avec histogramme egalise.PNG` | `labs/tp1_image_analysis/assets/contrast/equalised_histograms.png` | `138f66eeac2b9c527af2860d0f992ecdffc865d3` |
| `partie C/5_egalisation de lhistogramme.PNG` | `labs/tp1_image_analysis/assets/contrast/equalisation_code.png` | `322f368fc7eecdfe11a731b7714d3ec3da1fa1b2` |
| `partie C/4_histogrammes avec bins.PNG` | `labs/tp1_image_analysis/assets/contrast/input_histograms.png` | `5416e6aab5c4842f8db7b3382ee7a831466c168c` |
| `partie C/3_code des histogramme.PNG` | `labs/tp1_image_analysis/assets/contrast/histogram_code.png` | `46ae60b47bb49f79c4bb934458b33cffbd4c32f1` |
| `partie C/2_valeur des contraste.PNG` | `labs/tp1_image_analysis/assets/contrast/contrast_metrics_console.png` | `fee56ee4335abb95be5d7541b9c39f51d1886d6e` |
| `partie C/1_code_pur le contraste.PNG` | `labs/tp1_image_analysis/assets/contrast/contrast_metrics_code.png` | `6dc8c68b72bd341f342bf1facca39cdf30b2f75d` |
| `exercice 2/11_image avec tout les filtres.PNG` | `labs/tp2_filtering/assets/spatial/smoothing_filters_result.png` | `101bc03405f3bb38a8354a7719cf8093a9896c0b` |
| `exercice 2/10_tout type de filtre.PNG` | `labs/tp2_filtering/assets/spatial/smoothing_filters_code.png` | `fdd1d9ecba1b1aa211867d59420fc051dc765d94` |
| `exercice 2/9_image avec deux noyau pour les deux methode.PNG` | `Already present: labs/tp2_filtering/assets/spatial/operator_comparison.png` | `0c2063b5830bc766498324d423717e4988f82251` |
| `exercice 2/8_code pour la question 6.PNG` | `Already present: labs/tp2_filtering/assets/spatial/comparison_code.png` | `803d99e5f655fe7c9e21d14d429e0ca5ae697f2e` |
| `exercice 2/7_image en filtre 9x9.PNG` | `Already present: labs/tp2_filtering/assets/spatial/filter_9x9.png` | `e10c240842a567a0bb2c0447b6088dbab515bb76` |
| `exercice 2/6_image en filtre 7x7.PNG` | `Already present: labs/tp2_filtering/assets/spatial/filter_7x7.png` | `fa21554f656af921c294641355639f32ede74ac2` |
| `exercice 2/5_image en filtre 5x5.PNG` | `Already present: labs/tp2_filtering/assets/spatial/filter_5x5.png` | `828f0bc749fab55cdd496e616cfdf16b913a61b0` |
| `exercice 2/4_image avec le deuxieme noyau.PNG` | `Already present: labs/tp2_filtering/assets/spatial/second_kernel_result.png` | `45e7c774b005c261c46b62c412ea83531aea84ed` |
| `exercice 2/3_code avec le deuxieme noyau.PNG` | `Already present: labs/tp2_filtering/assets/spatial/second_kernel_code.png` | `a721ad25ff6332691a26d734eec4f5d492d398bb` |
| `exercice 2/1_codefiltre.PNG` | `Already present: labs/tp2_filtering/assets/spatial/kernel_code.png` | `aa02b131def4d53e66d8d0d9d4414f27cce4c9d4` |
| `exercice 2/2_image obtenue apres convolution.PNG` | `Already present: labs/tp2_filtering/assets/spatial/convolution_result.png` | `b0f76cbf93fda61556e4b833789718670abacd77` |
| `root/tp2.rar` | `Duplicate TP2 archive; contents already integrated` | `c8bdfc62d6ba26d7391c67a8d934c273f2d92aea` |
